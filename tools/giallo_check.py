import os
import sys
import re

# CHTHON-ONEIROS: The Giallo Linter
# Goal: Enforce evocative color vocabulary for high-intensity Argento-axis scenes.

COLOR_MAP = {
    r"\bred\b": "CRIMSON",
    r"\bblue\b": "INDIGO",
    r"\bgreen\b": "EMERALD",
    r"\byellow\b": "SODIUM",
    r"\bpurple\b": "VIOLET",
    r"\bwhite\b": "BLINDING",
    r"\bblack\b": "INK",
    r"\borange\b": "VERMILION"
}

def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    findings = []
    for pattern, replacement in COLOR_MAP.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            findings.append(f"Found {len(matches)} occurrences of '{matches[0]}'. Suggest replacement: '{replacement}'.")
    
    return findings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python giallo_check.py <file_path>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    if os.path.isfile(target_file):
        results = check_file(target_file)
        if results:
            print(f"--- GIALLO AXIS VIOLATION in {target_file} ---")
            for r in results:
                print(f"[!] {r}")
        else:
            print(f"--- {target_file} adheres to the Giallo Law ---")
