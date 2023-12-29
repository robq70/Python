import os

print("path to script __file__:", __file__)  # absolutna ścieżka do skryptu
script_dir = os.path.dirname(__file__)  # absolutna ścieżka do katalogu skryptu
print("script located in folder, script_dir: ", script_dir)
# ścieżka absolutna na którym katalog skryptu jest wykonywany
print("current working directory: os.getcwd(): ", os.getcwd())

# program Python/07 files/relative_path.py
fh = open("file1.txt", "w")
fh.write("content")
fh.close()
