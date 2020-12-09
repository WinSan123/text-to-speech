"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/credentials.json"

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants.")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Wavenet-C",
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding="LINEAR16",
    pitch= 2.4,
    speaking_rate=0.9
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input_=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("./output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')