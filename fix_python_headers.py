#!/usr/bin/env python3
"""Script to fix Python file headers to match .h format."""

import os
import re
from pathlib import Path

def fix_header(content):
    """Fix the header comment in a Python file."""
    # Match the triple-quote header block
    pattern = r'^("""\n)((?:.*\n)*?)(""")'
    match = re.match(pattern, content, re.MULTILINE)

    if not match:
        return content

    opening = match.group(1)
    header_content = match.group(2)
    closing = match.group(3)
    rest = content[match.end():]

    # Process each line in the header
    lines = header_content.split('\n')
    fixed_lines = []

    for line in lines:
        if line.strip():  # Non-empty line
            # Replace # with // in the line
            line = line.replace('#', '//')
            # Add " * " prefix if not already there
            if not line.startswith(' * '):
                fixed_lines.append(' * ' + line)
            else:
                fixed_lines.append(line)
        else:  # Empty line
            fixed_lines.append(line)

    # Reconstruct the file
    new_header = opening + '\n'.join(fixed_lines) + '\n' + closing
    return new_header + rest

def process_file(filepath):
    """Process a single Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = fix_header(content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all Python files in the python/content directory."""
    base_dir = Path('python/content')

    if not base_dir.exists():
        print(f"Directory {base_dir} does not exist")
        return

    py_files = list(base_dir.rglob('*.py'))

    print(f"Found {len(py_files)} Python files")

    fixed_count = 0
    for py_file in py_files:
        if process_file(py_file):
            fixed_count += 1

    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()
