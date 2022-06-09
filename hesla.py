import random, string
numb = 'a'
chars = ''
if input("include alphabet (y): "):
	chars += 'abcdefghijklmopqrstuvwxyz'
if input("include capitals (y): "):
	chars += chars.upper()
if input("include numbers (y): "):
	chars += '0123456789'
if input("include special characters (y): "):
	chars += '+-*/-\\\"\'!@#$%^&(){}[]'
while not (numb.isnumeric()):
	numb = input("zadej číslo: ")
for _ in range(10):
	print(''.join(random.choice(chars) for _ in range(int(numb))))
input()
