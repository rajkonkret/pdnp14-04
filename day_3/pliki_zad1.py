# działania z plikami
# filehandler - rura do pliku
# context manager pomaga w pracy z plikami
# with - context manager w python

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', "w", encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# plik istnieje
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', "x") as f:
#     f.write("Powitanie")

# "w" kasuje plik i tworzy nowy
with open('test.log', "w", encoding='utf-8') as fh:
    fh.write("nowe\n")
    fh.write("nowe\n")
    fh.write("nowe\n")

# dodaje do istniejacego pliku
with open('test.log', "a", encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")
    fh.write("dośdane\n")
    fh.write("dośążćdane\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
# 3 nowe
# nowe
# nowe
# Powitanie
# Kolejne
# Jeszcze jedno
