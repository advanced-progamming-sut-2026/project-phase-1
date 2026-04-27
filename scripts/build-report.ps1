param(
    [string]$InputFile = "docs/report/main.md",
    [string]$OutputFile = "docs/report/output/report.pdf"
)

$ErrorActionPreference = "Stop"

$outputDir = Split-Path -Path $OutputFile -Parent
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$sectionsDir = "docs/report/sections"
$combinedFile = Join-Path $outputDir ".report-combined.md"

Write-Host "Preparing combined markdown from $InputFile + sections ..."

$mainContent = Get-Content -Path $InputFile -Raw
Set-Content -Path $combinedFile -Value $mainContent -Encoding utf8

if (Test-Path $sectionsDir) {
    $sectionFiles = Get-ChildItem -Path $sectionsDir -Filter *.md | Sort-Object Name
    foreach ($section in $sectionFiles) {
        Add-Content -Path $combinedFile -Value "`r`n<div class=`"page-break`" aria-hidden=`"true`"></div>`r`n"
        Add-Content -Path $combinedFile -Value (Get-Content -Path $section.FullName -Raw)
        Add-Content -Path $combinedFile -Value "`r`n"
    }
}

Write-Host "Building PDF from combined markdown ..."

pandoc `
  "$combinedFile" `
  --from markdown `
  --pdf-engine=weasyprint `
  --css "styles/report.css" `
  --standalone `
  --toc `
  --output "$OutputFile"

if (Test-Path $combinedFile) {
    Remove-Item -Path $combinedFile -Force
}

Write-Host "Done: $OutputFile"
