#webbrowser module is imported to enable opening and searching in browser
#pyperclip module is imported to enable successful and accurate copying of clipboard item
import webbrowser, sys, pyperclip

#the copied item from the clipboard is made a string type and put into variable address if it is longer than length 1
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#a window is opened in the browser and the copied item is displayed on Google Maps!
webbrowser.open('https://www.google.com/maps/place/' + address)
