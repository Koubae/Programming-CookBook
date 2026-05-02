#!/bin/bash
FILE=$(jq -r '.tool_input.file_path')
[[ ! -f "$FILE" ]] && echo "⚠️ No file found to format: $FILE" && exit 0
goimports -w "$FILE" 2>/dev/null
gofmt -w "$FILE" 2>/dev/null
echo "✅ Formatted: $FILE ✨"
