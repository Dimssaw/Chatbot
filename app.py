from flask import Flask, render_template, request, jsonify

app = Flask(__name__,template_folder='templates')



@app.route('/')
def tanya():
	return render_template('tanya.html')

@app.post("/predict")
def response():
	text = request.get_json().get('message')
	
	message = {"answer": response}
	return jsonify(message)

if __name__ == '__main__':
	app.run(debug = True)