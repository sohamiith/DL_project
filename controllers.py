from pytube import YouTube

def download(url, outpath="./videos"):
	# Write code to download video from youtube
	"""
	yt = YouTube(url)
	path = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
	return path
	"""
	return "path"

def convertAudio(path):
	# Write code here to convert into audio file
	return "audio"

def generateText(audio):
	# Generate text
	return "text"

def generateSummary(text):
	# Write code to generate summary here
	return "summary"

"""
def sum1(a,b):
	return a+b
"""