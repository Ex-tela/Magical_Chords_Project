import os

def scan_chopro_files():
    root_dir = os.path.join(os.path.dirname(__file__), "songs_chord_pro")
    for folder, _, files in os.walk(root_dir):  
        for filename in files:
            full_path = os.path.join(folder, filename)
            if full_path.endswith(".chopro"):
                last_sub_folder = os.path.basename(folder) 
                with open(full_path, encoding='iso-8859-1') as f:
                    file_contents = f.read() 
                yield last_sub_folder, filename[:-7], file_contents
 

chopro_gen = scan_chopro_files()
# for artist, title, contents in chopro_gen:
#     print(f"{artist.replace('.', ' ')}")