def decoder(message, offset):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	punctuation = ".,?'! "
	translated_message = " "
	for letter in message:
		if not letter in punctuation:
			letter_value = alphabet.find(letter)
			translated_message += alphabet[(letter_value + offset) % 26]
		else:
			translated_message += letter
	print(translated_message)
decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud", 10)
decoder("Hey guys how are you doing?", 10)
decoder("joi qeic ryg kbo iye nysxq",16)