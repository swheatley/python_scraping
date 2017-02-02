#!/usr/bin/python

import webbrowser, sys


if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	#Get address from clipboard
	address = pyperclip.paste()
	
webbrowser.open('https://www.google.com/maps/place/' + address)
	
#Todo: get address from the clipboard
