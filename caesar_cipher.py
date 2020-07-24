SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
max_key = len(SYMBOLS)

def getMode():
	while True:
		print("Do you want to encrypt or decrypt: ")
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd']:
			return mode
		else:
			print('Enter either "encrypt" or "e", "decrypt" or "d"')
			
def getMessage():
	print('Enter the message: ')
	return input()
	
def getKey():
	key = 0
	while True:
		key = int(input('Enter the key number (1-%s): ' % (max_key)))
		if (key >= 1 and key <= max_key):
			return key
			
def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	
	for symbol in message:
		symbolIndex = SYMBOLS.find(symbol)
		if symbolIndex == -1:
			translated += symbol
		else:
			symbolIndex += key
			
			if symbolIndex >= len(SYMBOLS):
				symbolIndex -= len(SYMBOLS)
			elif symbolIndex < 0:
				symbolIndex += len(SYMBOLS)
			
			translated += SYMBOLS[symbolIndex]
	return translated
	
mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))