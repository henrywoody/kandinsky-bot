import os
from time import sleep
from kandinskybot import KandinskyBot
from get_location_input import get_location_input


def run_multiple():
	wassily = KandinskyBot()

	os.system('cls' if os.name == 'nt' else 'clear')
	print('Welcome to the KandinskyBot Super Interface!')
	sleep(1)

	location = get_location_input("Where would you like to save paintings? (default: ./images): ", show_warning=True)
	if not location: return

	number_of_paintings = get_number_input('How many paintings would you like?: ')
	starting_number = get_number_input('Starting number (paintings will be named sequentially): ')

	for i in range(starting_number, starting_number + number_of_paintings):
		wassily.paint()
		wassily.save_image(i, location=location)

def get_number_input(message):
	number = ''
	while not number:
		number = input(message)
		try:
			return abs(int(number))
		except ValueError:
			print("'{}' is not a valid number.".format(number))
			number = ''


if __name__ == '__main__':
	run_multiple()