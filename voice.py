# Python program to show 
# how to convert text to speech 


import pyttsx3 

# Initialize the converter 
converter = pyttsx3.init() 

voices = converter.getProperty('voices') 

for voice in voices: 
	# to get the info. about various voices in our PC 
	print("Voice:") 
	print("ID: %s" %voice.id) 
	print("Name: %s" %voice.name) 
	print("Age: %s" %voice.age) 
	print("Gender: %s" %voice.gender) 
	print("Languages Known: %s" %voice.languages) 

