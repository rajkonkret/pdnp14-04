import chardet

# pip install chardet


# rb - biblioteka wymaga odczytu bajtowego
with open('test.log', "rb") as f:
    raw_data = f.read()

print(raw_data)
# b'nowe\r\nnowe\r\nnowe\r\nPowitanie\r\nKolejne\r\nJeszcze jedno\r\ndo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)  # {'encoding': 'MacRoman', 'confidence': 0.63, 'language': ''}
# 3 po zwiekszeniu liczby polskich znaków w pliku
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(encoding)  # utf-8

print(raw_data.decode(encoding=encoding))
