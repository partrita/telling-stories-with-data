
import re

def remove_duplicate_bib_entries(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by entries. Assuming entries start with @ and are at the beginning of a line
    # We use a lookahead to split but keep the delimiter
    # Actually, splitting by likely @[a-zA-Z]+{ is better
    
    entries = re.split(r'(^@\w+\{)', content, flags=re.MULTILINE)
    
    # The first element might be empty or preamble
    # The subsequent elements are pairs of (delimiter, content)
    
    if not entries:
        return

    unique_entries = []
    seen_keys = set()
    
    # Process the preamble (anything before the first entry)
    preamble = entries[0]
    
    # Process entries
    # entries[1] is '@article{', entries[2] is the body, etc.
    
    final_content = preamble
    
    for i in range(1, len(entries), 2):
        delimiter = entries[i]
        body = entries[i+1]
        
        # Extract key
        # body starts with key,
        match = re.match(r'([^,]+),', body)
        if match:
            key = match.group(1).strip()
            if key in seen_keys:
                print(f"Skipping duplicate key: {key}")
                continue
            seen_keys.add(key)
            final_content += delimiter + body
        else:
            # Could not find key, maybe string or comment, just append
            final_content += delimiter + body
            
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    remove_duplicate_bib_entries('mybook/references.bib', 'mybook/references_dedup.bib')
