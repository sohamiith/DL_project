"""

Developed by: Soham Bhatt (SM21MTECH14004)

"""

from pytube import YouTube
import moviepy.editor as mp
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import math
import wave
import contextlib
from pydub.utils import make_chunks
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def download(url, outpath="./videos"):
	# Write code to download video from youtube
	
	yt = YouTube(url)
	path = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
	return path

def convertAudio(path):
	# Write code here to convert into audio file
	
	clip = mp.VideoFileClip(path)
	clip.audio.write_audiofile("./audios/test.wav",codec='pcm_s16le')
	return '/var/www/DL_project/audios/test.wav'

def generateText(path,method):
	# Generate text

	r = sr.Recognizer()
	sound = AudioSegment.from_wav(path)	

	if method == 'abstractive':
		chunk_size = 20#math.ceil(ratio_percent*seconds)
		myaudio = AudioSegment.from_file(path, "wav") 
		chunk_length_ms = chunk_size*1000 # pydub calculates in millisec 
		chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
	else:
		chunks = split_on_silence(sound,min_silence_len = 500,silence_thresh = sound.dBFS-14,keep_silence=2000)

	folder_name = "./audios/chunks"
	if not os.path.isdir(folder_name):
		os.mkdir(folder_name)

	print("running...")
	whole_text = ""
	for i, audio_chunk in enumerate(chunks, start=1):
		chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
		audio_chunk.export(chunk_filename, format="wav")
		with sr.AudioFile(chunk_filename) as source:
			audio_listened = r.record(source)
			try:
				text = r.recognize_google(audio_listened)
			except sr.UnknownValueError as e:
				print("Done ",i, str(e))
			else:
				text = f"{text.capitalize()}."
				whole_text += text
	return whole_text

def generateSummary(text, x = 0.25):
	#Write code to generate summary here

	tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-wikihow")
	model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-wikihow")
	
	listTemp = []
	main_listText = []
	
	inputList = list(text.split('.'))
	l = len(inputList)
	chunk_size = math.ceil(l * x)      
	i = 0
	j = chunk_size - 1
	iterations = l / (chunk_size)

	while i < l:
		listTemp.append(inputList[i])
		if len(listTemp) >= chunk_size:
			main_listText.append('.'.join(listTemp))
			listTemp = []
		i += 1
	if len(listTemp) != 0:
		main_listText.append('.'.join(listTemp))
	
	# Create tokens - number representation of our text
	token = tokenizer(main_listText, truncation = True, padding = "longest", return_tensors = "pt")
	# Summarize
	summary = model.generate(**token)
	i = 0
	summaryText = ""
	while(i < len(summary)):
		summaryText += tokenizer.decode(summary[i])
		i += 1
	return summaryText
