param([string]$Template = "cv-picture")

$out = "build/cv-bundle.txt"
New-Item -ItemType Directory -Force build | Out-Null

$files = @("AGENTS.md") +
  (Get-ChildItem data -Filter *.yaml | ForEach-Object { "data/$($_.Name)" }) +
  @("templates/$Template/$Template-template.tex",
    "templates/$Template/style-$Template-template.sty")

Set-Content $out "" -Encoding utf8
foreach ($f in $files) {
    Add-Content $out "`n===== $f =====" -Encoding utf8
    Get-Content $f -Raw -Encoding utf8 | Add-Content $out -Encoding utf8
}
Write-Host "Bundle ready: $out"