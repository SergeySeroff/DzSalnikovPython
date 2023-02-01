"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""

def rle_encode(data):
    encoding = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + data[i]
        i += 1
    return encoding

def rle_decode(data):
    decode = ""
    count = ""
    for i in data:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ""
    return decode

s = 'AAAAAAAFDDCCCCCCAEEEEEEEE'
print(rle_encode(s))
b = rle_encode(s)
print(rle_decode(b))
