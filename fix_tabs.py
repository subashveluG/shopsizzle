import os
import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove bg-white text-dark from the women-tab and tech-tab if present
    content = content.replace('bg-white text-dark shadow-sm border border-transparent', 'shadow-sm border border-transparent collection-tab-btn')
    
    # Give men-tab the same base class
    content = content.replace('active px-4 py-2 rounded-pill fw-bold shadow-sm border border-transparent', 'active px-4 py-2 rounded-pill fw-bold shadow-sm collection-tab-btn border border-transparent')
    
    # Some buttons might be 'nav-link active px-4 py-2 rounded-pill fw-bold shadow-sm' without 'border border-transparent'
    content = content.replace('active px-4 py-2 rounded-pill fw-bold shadow-sm" id="men-tab"', 'active px-4 py-2 rounded-pill fw-bold shadow-sm collection-tab-btn border border-transparent" id="men-tab"')
    
    # Strip the inline style block for #collectionTabs
    content = re.sub(r'<style>[\s\n]*#collectionTabs .*?</style>', '', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Collection Tabs replaced.")
