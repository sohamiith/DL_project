from flask import Flask, jsonify, request, render_template
from controllers import *
#import pytube
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
	return jsonify(result = {
	 	"video_path" : path,
	 	"audio" : audio,
	 	"text": text,
	 	"summary": summary
	})
	return render_template('result.html', url=url, text=text, summary=summary)
	#return jsonify(result)

"""
@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
	ans = str(sum1(a,b))
	result = {
		"a" : a,
		"b" : b,
		"operation": "+",
		"ans": ans
	}
	return jsonify(result)
"""

if __name__=="__main__":
	app.run(debug=True)