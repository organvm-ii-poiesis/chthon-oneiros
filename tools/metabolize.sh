#!/bin/bash
# CHTHON-ONEIROS: The Digestion Script
# Goal: Add digital decay (Zalgo/Unicode noise) to older files to simulate "metabolism."

TARGET_DIR="production/beta"
GLITCH_CHARACTERS=("ᛟ" "ᚦ" "ᚱ" "ᚲ" "ᚷ" "ᚹ" "ᚺ" "ᚻ" "ᚼ" "ᚽ")

# Ensure target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Target directory $TARGET_DIR not found. Skipping digestion."
    exit 0
fi

echo "Starting metabolism of the substrate..."

for file in "$TARGET_DIR"/*.md; do
    if [ -f "$file" ]; then
        # 10% chance to "infect" a file on each run
        if [ $((RANDOM % 10)) -eq 0 ]; then
            echo "Infecting $file..."
            
            # Select a random glitch character
            GLITCH=${GLITCH_CHARACTERS[$((RANDOM % ${#GLITCH_CHARACTERS[@]}))]}
            
            # Append glitch text to the end of the file
            echo -e "

---" >> "$file"
            echo "## // DIGESTION_LOG" >> "$file"
            echo "Status: Metabolizing... $GLITCH" >> "$file"
            echo "Timestamp: $(date +%Y-%m-%d_%H:%M:%S)" >> "$file"
            
            # Add some scattered Unicode noise to random lines
            sed -i '' "s/ / $GLITCH /g" "$file" 2>/dev/null | head -n 5
        fi
    fi
done

echo "Metabolism complete."
