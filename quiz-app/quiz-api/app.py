
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import build_token, decode_token
import json
from linkBD import *
from Question import Question

def to_json(data):
    json_data = json.dumps(data)
    return json_data

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"
@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def PostLoginInfo():
	payload = request.get_json()
	triedPassword = payload['password']
	if(triedPassword == "flask2023"):
		my_dict = {"token":build_token()}
		json_data = to_json(my_dict)

		return json_data, 200
	return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def PostQuestion():
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		return 500
	question = request.get_json()
	responseInsert = insertQuestionToBDD(question)
	if(responseInsert >=0):
		my_dict = {"id":responseInsert}
		jsondata = to_json(my_dict) 
	return jsondata, 200

@app.route('/questions', methods=['GET'])
def GetQuestionsInfo():
	position = request.args.get('position')
	responseSelect = getColumnsFromTableById("question", ['id','position', 'title', 'text', 'image', 'possibleAnswer1', 'possibleAnswer2', 'possibleAnswer3', 'possibleAnswer4'], position)
	return responseSelect, 200


if __name__ == "__main__":
    app.run()
