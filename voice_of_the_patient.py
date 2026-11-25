# Convert audio to text
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Define a function that converts the recorded patient audio into text.
def transcribe_patient_voice(audio_filepath):
    groq_api_key = os.environ.get("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY environment variable.")

    if not audio_filepath:
        raise ValueError("Please upload or record your voice first.")

    client = Groq(api_key=groq_api_key)

# This section of code opens the recorded audio file and sends it to the Groq API for transcription. The transcription result is then returned as text.
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.environ.get("WHISPER_MODEL", "whisper-large-v3"),
        )

    return transcription.text





# # Step1: Record audio from microphone

# # dependencies: ffmpeg, portaudio, pyaudio
# import logging                       # THis is to display useful messages while the program runs.
# import speech_recognition as sr      # This is for recording audio from the microphone
# from pydub import AudioSegment       # This is for converting recorded audio into MP3 format.
# from io import BytesIO               # This is for handling audio data in memory without creating a temporary WAV file.

# # Set the format for messages displayed in the terminal. Shows the date, time, message type (INFO/ERROR), and message.
# logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# # Define a function that records the patient's voice and saves it to a file.
# def record_audio(file_path, timeout=20, phrase_time_limit=None):
#     """
#     Simplified function to record audio from the microphone and save it as an MP3 file.

#     Args:
#     file_path (str): Path to save the recorded audio file.
#     timeout (int): Maximum time to wait for a phrase to start (in seconds).
#     phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
#     """
#     recognizer = sr.Recognizer()            # Create a recognizer object to manage audio recording.

#     # Open the default microphone so the program can capture the patient's voice.
#     with sr.Microphone() as source:
#         logging.info("Adjusting for ambient noise...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)             # Listen to the surroundings for one second to improve speech detection.
#         logging.info("Start speaking now...")
        
#         # Record the audio
#         # Record speech from the microphone. Wait up to 'timeout' seconds for speech to begin.
#         # Stop recording after 'phrase_time_limit' seconds once speech starts.
#         audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
#         logging.info("Recording complete.")
        
#         # Convert the recorded audio to an MP3 file
#         wav_data = audio_data.get_wav_data()
#         audio_segment = AudioSegment.from_wav(BytesIO(wav_data))              # Read the WAV audio bytes into an AudioSegment object.
#         audio_segment.export(file_path, format="mp3", bitrate="128k")         # Export the recorded audio as an MP3 file with a 128 kbps bitrate.
        
#         logging.info(f"Audio saved to {file_path}")         # This will display the location where the audio file is saved.

# audio_filepath="patient_voice_test.mp3"
# record_audio(audio_filepath, timeout=20, phrase_time_limit=10)      # Call the recording function. Wait up to 20 seconds for speech to begin and record for at most 10 seconds.


