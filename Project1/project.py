
"""
    The code is a Python script that uses the gTTS library to convert user input text into speech and
    plays it using the pygame library.
    
    Args:
      text: The text parameter is the input text that you want to convert to speech.
"""

from gtts import gTTS
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to play speech
def play_speech(text):
    # Generate speech
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save("texttospeech.mp3")

    # Load the speech file
    pygame.mixer.music.load("texttospeech.mp3")

    # Play the speech
    pygame.mixer.music.play()

    # Wait until the speech finishes playing
    while pygame.mixer.music.get_busy():
        continue

# Run indefinitely
while True:
    # Wait for user input
    user_input = input("Enter text to convert to speech (type 'exit' to quit): ")

    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting...")
        break

    # Play speech for the input text
    play_speech(user_input)
