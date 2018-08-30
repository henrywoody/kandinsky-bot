import os


def get_location_input(message, show_warning=False):
	location = ''
	while not location:
		location = input("Where would you like to save images? (default: ./images): ") or './images'

		if location == './images' and 'images' not in os.listdir():
			os.system('mkdir images')

		try:
			if os.listdir(location) and show_warning:
				print('Warning: the directory you have given contains files that may be overwritten!')
				is_sure = input('Are you sure? (y/n, default: y): ') not in ['no', 'n']
				if not is_sure:
					print('Bye!')
					return
			return location
		except FileNotFoundError:
			print('The given directory does not exist!')
			location = ''