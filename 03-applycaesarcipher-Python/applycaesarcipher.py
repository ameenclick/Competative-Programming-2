# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	result=""
	for e in msg:
		shifted=ord(e)+shift
		if(e == " "):
			result+=" "
			continue
		if(e.islower()):
			if(shifted >= 97 and (shifted <= 122)):
				result+=chr(shifted)
			elif(shifted<97):
				result+=chr(122-(97-shifted)+1)
			else:
				result+=chr(97+(shifted-122)-1)
		else:
			if(shifted>=65 and shifted<=90):
				result+=chr(shifted)
			elif(shifted<65):
				result+=chr(90-(65-shifted)+1)
			else:
				result+=chr(65+(shifted-90)-1)
	return result



