#!/bin/bash
TOTAL_WORDS=$(find . -name "*.md" -type f -not -path '*/.*' -print0 | xargs -0 wc -w | tail -n 1 | awk '{print $1}')
TOTAL_FILES=$(find . -name "*.md" -type f -not -path '*/.*' | wc -l)
echo "Current Stats: $TOTAL_FILES files, $TOTAL_WORDS words."
# Update CATALOG.md (Requires specific header format)
sed -i '' "s/Total documents | .*/Total documents | $TOTAL_FILES files |/" docs/CATALOG.md
sed -i '' "s/Estimated total word count | .*/Estimated total word count | **$TOTAL_WORDS** |/" docs/CATALOG.md
