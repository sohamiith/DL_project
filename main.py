"""

Developed by: Soham Bhatt (SM21MTECH14004)

"""

from flask import Flask, jsonify, request, render_template
from controllers import *
import pytube
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/video", methods=['GET', 'POST'])
def get_video_url():
	for key, value in request.form.items():
		if key == 'url': 
			url = value
		if key == 'method': 
			method = value
		if key == 'per': 
			per = value
	path = download(url)
	audio = convertAudio(path)
	text = generateText(audio,method)
	summary = generateSummary(text,int(per)//100)
	
	# Json response for testing
	# return jsonify(result = {
	#  	"video_path" : path,
	#  	"audio" : audio,
	#  	"text": text,
	#  	"summary": summary
	# })
	
	return render_template('result.html', url=url, text=text, summary=summary)

if __name__=="__main__":
	app.run(debug=True)