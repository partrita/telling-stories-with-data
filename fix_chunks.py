import os
import re

def fix_qmd_chunks(directory):
    # Regex to find chunk start followed by an empty line and then an option
    # e.g. ```{r}\n\n#|
    pattern = re.compile(r'(```{[a-z]+})(\n\s*\n\s*#\|)', re.MULTILINE)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.qmd'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace multiple newlines between chunk header and #| with a single newline
                new_content = pattern.sub(r'\1\n\2'.replace('\n\2', '\n#|'), content)
                # Wait, the above sub is a bit tricky. Let's do it simpler.
                
                def sub_func(match):
                    # match.group(1) is ```{r}
                    # match.group(2) is \n\n#|
                    return match.group(1) + '\n#|'
                
                new_content = pattern.sub(sub_func, content)
                
                if new_content != content:
                    print(f"Fixed chunks in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_qmd_chunks('mybook')
