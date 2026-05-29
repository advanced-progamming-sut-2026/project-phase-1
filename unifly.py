#!/usr/bin/env python3
"""
embed_sections.py

Usage:
    python embed_sections.py path/to/main.md

What it does:
- Scans `main.md` for lines matching: - [label](relative/path.md#anchor-id)
- For each match:
  - Resolves the path relative to main.md
  - Opens the target file and finds the section whose heading has the matching anchor id
    (supports explicit `{#id}` anchors, HTML anchors <a id="id">, or slugified heading)
  - Extracts that heading and its content until the next heading of same-or-higher level
  - Replaces the single TOC line in main.md with:
      <a id="anchor-id"></a>
      <extracted markdown section>
- Writes main.md back in place (creates a backup main.md.bak)

Notes:
- If the anchor is not found, the whole target file is included as a fallback.
- Adjust `TOC_START_MARKER` / `TOC_END_MARKER` if your region markers differ.
"""

import sys
import re
import io
import os
import base64
import mimetypes
from pathlib import Path

TOC_START_MARKER = "# فهرست مطالب"
TOC_END_MARKER = '<div class="page-break">'  # stop replacing when this marker appears

link_re = re.compile(r'^\s*-\s*\[([^\]]+)\]\(\s*([^)#]+)(?:#([^)]+))?\s*\)\s*$', flags=re.UNICODE)

def slugify(text: str) -> str:
    text = text.strip().lower()
    # simple slug: keep alnum and spaces, replace others with spaces
    text = re.sub(r'[^\w\s-]', '', text, flags=re.UNICODE)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

def find_anchor_section(content_lines, anchor_id):
    # 1) look for explicit {#anchor_id} on heading line
    heading_idx = None
    heading_level = None
    for i, ln in enumerate(content_lines):
        m = re.match(r'^(#{1,6})\s+.*\{\#' + re.escape(anchor_id) + r'\}\s*$', ln)
        if m:
            heading_idx = i
            heading_level = len(m.group(1))
            return heading_idx, heading_level

    # 2) look for HTML anchor then a heading after it
    for i, ln in enumerate(content_lines):
        if re.search(r'<a\s+id=["\']' + re.escape(anchor_id) + r'["\']\s*>', ln):
            # find next heading line
            for j in range(i+1, min(i+6, len(content_lines))):
                mh = re.match(r'^(#{1,6})\s+.*$', content_lines[j])
                if mh:
                    return j, len(mh.group(1))
            # if no heading, anchor itself may precede content: return next line as start
            return i, 1

    # 3) find heading whose slugified text equals anchor_id
    for i, ln in enumerate(content_lines):
        mh = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if mh:
            heading_text = mh.group(2).strip()
            # remove trailing {#...} if any
            heading_text = re.sub(r'\{\#.*\}\s*$', '', heading_text)
            if slugify(heading_text) == anchor_id:
                return i, len(mh.group(1))

    return None, None

def extract_section_from_file(file_path: Path, anchor_id: str):
    text = file_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    start_idx, level = find_anchor_section(lines, anchor_id)
    if start_idx is None:
        # fallback: return entire file
        return text + "\n"
    # find end: next heading with level <= current level (but skip start line)
    end_idx = len(lines)
    for i in range(start_idx+1, len(lines)):
        m = re.match(r'^(#{1,6})\s+.*$', lines[i])
        if m and len(m.group(1)) <= level:
            end_idx = i
            break
    section = "\n".join(lines[start_idx:end_idx]) + "\n"
    section = embed_images_as_base64(section, Path("C:\\\\Users\\m1382\\Desktop\\CTR\\ta\\ap\\project-documents"))
    return section

def process_main(main_path: Path, out_path: Path):
    content = main_path.read_text(encoding='utf-8')
    lines = content.splitlines()

    # find TOC region
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == TOC_START_MARKER)
    except StopIteration:
        print("TOC start marker not found. Exiting.")
        return
    try:
        end = next(i for i, ln in enumerate(lines[start+1:], start+1) if ln.strip() == TOC_END_MARKER)
    except StopIteration:
        # if end marker not found, operate until end of file
        end = len(lines)

    out_lines = lines[:start+1]  # keep the TOC header line
    toc_links = []
    section_anchors = []
    i = start + 1
    while i < end:
        ln = lines[i]
        m = link_re.match(ln)
        if m:
            label = m.group(1)
            rel_path = m.group(2).strip()
            anchor = m.group(3) or ""
            target_path = (main_path.parent / rel_path).resolve()
            if not target_path.exists():
                out_lines.append(f"<!-- missing file: {rel_path} -->")
                i += 1
                continue
            if not anchor:
                # no anchor: just link to file
                anchor_id = slugify(label)
                toc_links.append((label, anchor_id))
                section_anchors.append((target_path, None, anchor_id, label))
                out_lines.append(f'- [{label}](#{anchor_id})')
            else:
                toc_links.append((label, anchor))
                section_anchors.append((target_path, anchor, anchor, label))
                out_lines.append(f'- [{label}](#{anchor})')
            i += 1
        else:
            out_lines.append(ln)
            i += 1

    # append the rest of the file unchanged
    out_lines.extend(lines[end:])   

    # Now, after TOC, embed each section with anchor and pointer
    already_added = []
    
    for target_path, anchor, anchor_id, label in section_anchors:
        if target_path in already_added:
            continue
        if anchor:
            section = extract_section_from_file(target_path, anchor)
        else:
            section = target_path.read_text(encoding='utf-8')
        already_added += [target_path]
        # Embed images as base64
        out_lines.append(f'<!-- Start of section: {label} -->\n\n')
        out_lines.extend(section[1:].splitlines())
        out_lines.append(f'<!-- End of section: {label} -->\n')

    out_lines.append('\n<style>body { direction: rtl; } pre, code { direction: ltr; unicode-bidi: embed; }</style>\n')

    final_text = "\n".join(out_lines) + "\n"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(final_text, encoding='utf-8')
    print(f"Wrote embedded output to {out_path}")

# Convert image to base64 and embed
def image_to_base64(img_path, base_dir):
    """Convert image path to base64 data URI."""
    try:
        candidate_path = img_path.strip()
        full_path = (base_dir / candidate_path).resolve()
        while not full_path.exists() and candidate_path.startswith('../'):
            candidate_path = candidate_path[3:]
            full_path = (base_dir / candidate_path).resolve()
        if not full_path.exists():
            print(f"path [{img_path}] does not exist in [{base_dir}]")
            return None
        with open(full_path, 'rb') as f:
            img_data = f.read()
        mime_type, _ = mimetypes.guess_type(str(full_path))
        if not mime_type:
            mime_type = 'image/png'  # default
        b64_data = base64.b64encode(img_data).decode('utf-8')
        return f'data:{mime_type};base64,{b64_data}'
    except Exception as e:
        print(f"Warning: Could not encode image {img_path}: {e}")
        return None

def embed_images_as_base64(text, base_dir):
    """Convert local images to base64.

    Markdown images are replaced with the user-provided wrapper:
    <div style="position: relative; display: flex; justify-content: center; align-items: center; margin: 20px auto;">
        <img src="..." alt="..." style="display: block; width: 50vw;  max-width: 100%;">
    </div>
    """
    markdown_pattern = re.compile(r'!\[([^\]]*?)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
    html_pattern = re.compile(r'<img\b([^>]*?)\bsrc=["\']([^"\']+)["\']([^>]*)>', re.IGNORECASE)

    def should_inline_gif(img_path):
        return Path(img_path).suffix.lower() == '.gif'

    def replace_markdown_img(match):
        alt_text = match.group(1)
        img_path = match.group(2).strip()
        data_uri = img_path
        if not img_path.startswith(('http://', 'https://', 'data:')) and should_inline_gif(img_path):
            b64_uri = image_to_base64(img_path, base_dir)
            if b64_uri:
                data_uri = b64_uri
        return ("<div style=\"position: relative; display: flex; justify-content: center; align-items: center; margin: 20px auto;\">"
                f"<img src=\"{data_uri}\" alt=\"{alt_text}\" style=\"display: block; width: 50vw;  max-width: 100%;\">"
                "</div>")

    def replace_html_img(match):
        before_src = match.group(1)
        img_path = match.group(2).strip()
        after_src = match.group(3)
        if img_path.startswith(('http://', 'https://', 'data:')) or not should_inline_gif(img_path):
            return match.group(0)
        b64_uri = image_to_base64(img_path, base_dir)
        if not b64_uri:
            return match.group(0)
        return f'<img{before_src}src="{b64_uri}"{after_src}>'

    text = markdown_pattern.sub(replace_markdown_img, text)
    return html_pattern.sub(replace_html_img, text)

# Note: HTML box conversion moved to Markdown files themselves per user request.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python embed_sections.py path/to/main.md")
        sys.exit(1)
    main_md = Path(sys.argv[1]).resolve()
    if not main_md.exists():
        print("File not found:", main_md)
        sys.exit(1)
    # Output to phase1/final/main.md by default
    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2])
    else:
        out_path = main_md.parent / "final" / main_md.name
    process_main(main_md, out_path)