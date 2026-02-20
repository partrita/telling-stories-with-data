
import os
import re

def fix_citations_in_qmd(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".qmd"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Regex to find @Key followed by Korean chars
                    # We want to capture @Key and replace @KeyKorean with @Key
                    # But we should be careful not to merge with following text without space
                    # If we have "@Key이 text", replacing "@Key이" with "@Key" gives "@Key text" (good)
                    # If we have "@Key이.", replacing "@Key이" with "@Key" gives "@Key." (good)
                    
                    new_content = re.sub(r'(@[a-zA-Z0-9_-]+)([\uac00-\ud7a3]+)', r'\1', content)
                    
                    if content != new_content:
                        print(f"Fixing citations in {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    fix_citations_in_qmd('mybook')
