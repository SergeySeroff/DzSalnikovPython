"""Напишите программу, удаляющую из текста все слова, 
содержащие ""абв""."""

word_list = ['ау', 'бур', 'лор', 'мор', 'вор', 'тур']
new_list = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, word_list))
print(new_list)