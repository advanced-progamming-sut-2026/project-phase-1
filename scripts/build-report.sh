#!/usr/bin/env bash

set -euo pipefail

input_file="${1:-docs/report/main.md}"
output_file="${2:-docs/report/output/report.pdf}"
sections_dir="docs/report/sections"

output_dir="$(dirname "$output_file")"
mkdir -p "$output_dir"

combined_file="$output_dir/.report-combined.md"

echo "Preparing combined markdown from $input_file + sections ..."
cp "$input_file" "$combined_file"
printf "\n\n" >> "$combined_file"

if [ -d "$sections_dir" ]; then
  while IFS= read -r section; do
    printf "<div class=\"page-break\" aria-hidden=\"true\"></div>\n\n" >> "$combined_file"
    cat "$section" >> "$combined_file"
    printf "\n\n" >> "$combined_file"
  done < <(find "$sections_dir" -maxdepth 1 -type f -name "*.md" | sort)
fi

echo "Building PDF from combined markdown ..."

pandoc \
  "$combined_file" \
  --from markdown \
  --pdf-engine=weasyprint \
  --css "styles/report.css" \
  --standalone \
  --toc \
  --output "$output_file"

rm -f "$combined_file"

echo "Done: $output_file"
