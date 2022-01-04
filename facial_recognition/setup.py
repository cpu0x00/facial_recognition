# a setup script for automating setting up and trouble shooting the required stuff for using the facial recognition script

import os
from subprocess import run
import sys


if os.getuid() != 0:
	sys.exit('[-] try to run with root permissions (sudo python3 setup.py) ')

system_dependencies = [ # neccessary system dependencies for the face_recognition library
	'cmake',
	'build-essential',
	'pkg-config',
	'libx11-dev',
	'libatlas-base-dev',
	'libgtk-3-dev',
	'libboost-python-dev',
	'users', # required just for the setup script to install the python libraries for the current user avoiding package corruptions
]


requirements = [
	'opencv-python', # for taking photos
	'face_recognition',	# for the actual face recognition  
	'pywhatkit', # for shutting down the system 
]


def install_dependencies():

	print('[*] installing the required system packages')
	print('--------------------------------------------')
	for package in system_dependencies:
		print(f'[*] installing {package}')
		run(['apt', 'install', f'{package}', '-y'], capture_output=True).stdout.decode()

	print('\t')

	print('[*] installing the required python3 libraries (this will take a while)')
	print('---------------------------------------------------------------------')
	current_user = run(['users'], capture_output=True).stdout.decode()
	for lib in requirements:
		print(f'[*] installing {lib}')

		run(['sudo', f'--user={current_user}', 'python3', '-m', 'pip', 'install', f'{lib}'], capture_output=True).stdout.decode()	


def config():
	Photo_Name = 'me.jpg'
	print('\t')
	print('[*] configuring the files')
	print('--------------------------')
	print('[*] making a (.secrets) folder in /usr/share/ directory all data will be stored there')
	os.mkdir('/usr/share/.secrets')
	print('[*] moving the image file to the secrets folder')
	os.system('mv me.jpg /usr/share/.secrets/')
	print('[*] using chattr to look down the image file (even root will not be able to delete or move the image)')
	os.system('chattr +i /usr/share/.secrets/me.jpg')
	print('[*] all done ;)')
	print('\t')
	print('[+] if you want to move or delete the image navigate to /usr/share/.secrets and use this command (chattr -i me.jpg)')


def configuring_the_files():
	Photo_Name = 'me.jpg'

	if not Photo_Name in os.listdir():
		sys.exit('[-] use the (take_photo.py) script to take photo or take a photo of yourself and name it (me.jpg) in the same DIR and run the setup script\n again')
	
	if '.secrets' in os.listdir('/usr/share/'):
		q = input('[+] found a .secrets folder in your /usr/share/ directory would you like to overwrite it (not recommended)[y/n]: ')

		if q == 'y':
			config()
		if q == 'n':
			sys.exit('[-] exiting')

	if not '.secrets' in os.listdir('/usr/share/'):
		config()


install_dependencies()
configuring_the_files()