
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import build_token, decode_token
import json
from linkBD import *
from appClasses import Question

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
	responseInsertQuestion = insertQuestionToBDD(question)
	responseInsertAnswer = insertPossibleAnswersToBDD(responseInsertQuestion.getId(), question['possibleAnswers'])
	responseInsertQuestion.setPossibleAnswers(responseInsertAnswer)
	if isinstance(responseInsertQuestion,Question):
		my_dict = {"id":responseInsertQuestion.getId()}
		jsondata = to_json(my_dict) 
	return jsondata, 200



@app.route('/questions', methods=['GET'])
def GetQuestionsInfo():
	position = request.args.get('position')
	responseSelectQuestion = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "position", position)
	responseSelectAnswers = getColumnsFromTableByColumn("poss_answers", ['id','id_quest', 'text', 'isCorrect'], "id_quest", responseSelectQuestion[0]['id'])
	question = Question(responseSelectQuestion[0]['position'],responseSelectQuestion[0]['title'],responseSelectQuestion[0]['text'],responseSelectQuestion[0]['image'])
	question.setId(responseSelectQuestion[0]['id']) 
	posAns = createPossAnswers(responseSelectAnswers)
	question.setPossibleAnswers(posAns)
	for i in posAns:
		print(i)
	return str(question), 200


if __name__ == "__main__":
    app.run()
