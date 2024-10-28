# utils/fileUtil.py

import os

def create_translate_file(key: int, plain_text: str):
    current_file_path = os.path.abspath(__file__) 
    current_dir = os.path.dirname(current_file_path)
    output_dir = os.path.join(current_dir, '..', 'plain_texts')
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True) 
    file_path = os.path.join(output_dir, f'plain_text_key-{key}.txt')
    
    with open(file_path, "w") as f:
        f.write(plain_text)
