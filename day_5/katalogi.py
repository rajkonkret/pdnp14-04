import shutil
from pathlib import Path

# poetry - inne podejscie do venv

base_path = Path('ops_example')
base_path_2 = Path("ops_example/D")

print(base_path_2)
print(base_path)
# ops_example\D
# ops_example

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()

path_b = base_path / "A" / 'B'
path_c = base_path / "A" / 'C'
path_d = base_path / "A" / 'D'

# brak katalogu A
# path_b.mkdir() # FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'

path_b.mkdir(parents=True)
path_c.mkdir()  # katalog A juz istnieje, nie musimy podawac parents

# tworzenie plików
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding="utf-8") as stream:
        stream.write(f"Jakaś tresć pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)

# zmiana nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1_renamed.log')

# kopiowanie pliku
ex1 = path_d / 'ex1_renamed.log'
docelowy = path_c
shutil.copy(ex1, docelowy)
