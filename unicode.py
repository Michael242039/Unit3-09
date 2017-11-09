#Created by: Michael Taylor
#Created on:October 23, 2017
#Created for ICS3U
#This program prints the the letters of the alphabet using unichr()

BEGINNING_NUMBER_UPPER = 64
BEGINNING_NUMBER_LOWER = 96
ALPHABET_SIZE = 26

def print_letters():
	print ('##### START #####')
	for increment in range(1, ALPHABET_SIZE + 1):
		letter_number1 = BEGINNING_NUMBER_UPPER + increment
		for increment in range(1, ALPHABET_SIZE + 1):
			letter_number2 = BEGINNING_NUMBER_LOWER + increment
			print unichr(letter_number1),
			print(unichr(letter_number2))
	print ('##### FINISH #####')

print_letters()
