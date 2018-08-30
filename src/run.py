import os
from time import sleep
from kandinskybot import KandinskyBot
from get_location_input import get_location_input


def run():
	wassily = KandinskyBot()

	os.system('cls' if os.name == 'nt' else 'clear')
	print('Welcome to the KandinskyBot Interface!')
	sleep(0.75)
	location = get_location_input("Where would you like to save paintings? (default: ./images): ")
	if not location: return

	keep_running = True
	while keep_running:
		print('Okay, chefing up a fresh painting for you...')
		sleep(0.5)

		wassily.paint()

		should_save = input("Would you like to save this painting? (y/n, default: no): ") in ['yes', 'ye', 'y', 'yeah']
		if should_save:
			file_name = get_file_name_input("What would you like to name the file? (no extension): ", location)
			wassily.save_image(file_name, location=location)
		else:
			print("Okay, I'll try harder next time.")
			wassily.close_window()
		
		keep_running = input("Would you like another? (y/n, default: yes): ") not in ['no', 'n']
		if not keep_running:
			print('Bye!')

def get_file_name_input(message, location):
	file_name = input(message)
	while not file_name or '{}.eps'.format(file_name) in os.listdir(location):
		if not file_name:
			print('A valid file name is required in order to save: ')
		if '{}.eps'.format(file_name) in os.listdir(location):
			print('A file with that name already exists!')
			if input('Overwrite? (y/n, default: n): ') in ['yes', 'ye', 'y', 'yeah']:
				break
		file_name = input(message)
	return file_name


if __name__ == "__main__":
	run()