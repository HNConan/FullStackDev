
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

@app.route('/rebuild-db', methods=['POST'])
def rebuildDB():
	return 'Ok', 200


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
		print("Unauthorized")
		return "",401
	
	question = request.get_json()
	
	responseInsertQuestion = insertQuestionToBDD(question)
	responseInsertAnswer = insertPossibleAnswersToBDD(responseInsertQuestion.getId(), question['possibleAnswers'])
	responseInsertQuestion.setPossibleAnswers(responseInsertAnswer)
	if isinstance(responseInsertQuestion,Question):
		my_dict = {"id":responseInsertQuestion.getId()}
		jsondata = to_json(my_dict) 
	return jsondata, 200


@app.route('/questions/<int:question_id>', methods=['DELETE'])
def DeleteQuestion(question_id):
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	deleteQuestion(question_id)
	return "",204

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestion():
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	deleteAllQuestion()
	return "",204

@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipants():
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	deleteAllParticipants()
	return "",204
		

@app.route('/questions/<int:question_id>', methods=['GET'])
def GetQuestionsInfoById(question_id):
	responseSelectQuestion = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "position", question_id)
	responseSelectAnswers = getColumnsFromTableByColumn("poss_answers", ['id','id_quest', 'text', 'isCorrect', 'position'], "id_quest", responseSelectQuestion[0]['id'])
	question = Question(responseSelectQuestion[0]['position'],responseSelectQuestion[0]['title'],responseSelectQuestion[0]['text'],responseSelectQuestion[0]['image'])
	question.setId(responseSelectQuestion[0]['id']) 
	posAns = createPossAnswers(responseSelectAnswers, id_quest=responseSelectQuestion[0]['id'])
	question.setPossibleAnswers(posAns)
	return str(question), 200



@app.route('/questions', methods=['GET'])
def GetQuestionsInfo():
	position = request.args.get('position')
	responseSelectQuestion = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "position", position)
	responseSelectAnswers = getColumnsFromTableByColumn("poss_answers", ['id','id_quest', 'text', 'isCorrect', 'position'], "id_quest", responseSelectQuestion[0]['id'])
	question = Question(responseSelectQuestion[0]['position'],responseSelectQuestion[0]['title'],responseSelectQuestion[0]['text'],responseSelectQuestion[0]['image'])
	question.setId(responseSelectQuestion[0]['id']) 
	posAns = createPossAnswers(responseSelectAnswers,id_quest=responseSelectQuestion[0]['id'])
	question.setPossibleAnswers(posAns)
	return str(question), 200

@app.route('/questions/<int:question_id>', methods=['PUT'])
def UpdateQuestion(question_id):
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	#Get and create new Question (the one that will Replace)
	newQuestionJSON = request.get_json()
	updatedQuestion = Question(newQuestionJSON['position'],newQuestionJSON['title'],newQuestionJSON['text'],newQuestionJSON['image'])
	newPossibleAnswers = createPossAnswers(newQuestionJSON['possibleAnswers'], question_id)
	updatedQuestion.setPossibleAnswers(newPossibleAnswers)
	updatedQuestion.setId(question_id)
	
	#Update the question
	updateQuestion(updatedQuestion)
	return "",204


if __name__ == "__main__":
    app.run()
