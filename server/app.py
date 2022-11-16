from config import HOST, PORT,basepath,modelpath
from flask import Flask, request, jsonify

app = Flask(__name__, template_folder='template')

@app.route('/',methods=['GET', 'POST'])
def index():
    return "Running"

@app.route('/api/v0/inference',methods=['GET', 'POST'])
def perform_inference():
    if request.method =="POST":
        json_data = request.get_json()
        #model code
        return jsonify({"result":"add your result here"})
    if request.method =="GET":
        return jsonify({"status":"NOT CONFIGURED"})
    
if __name__ == '__main__':
	app.run(debug=False, host=HOST, port=PORT, use_reloader=False)