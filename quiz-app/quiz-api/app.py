
from flask import Flask, request, jsonify
from flask_cors import CORS
from jwt_utils import build_token, decode_token
import json
from linkBD import *
from appClasses import *

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
	return {"size": get_table_count("question"), "scores": getScores(getAllParticipants())}, 200

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
	print(question)
	responseInsertQuestion = insertQuestionToBDD(question)
	responseInsertAnswer = insertPossibleAnswersToBDD(responseInsertQuestion.getId(), question['possibleAnswers'])
	responseInsertQuestion.setPossibleAnswers(responseInsertAnswer)
	IDs = getIdsOfPostionsToUpdate(responseInsertQuestion.getPosition(),get_table_count("question"))
	updatePositionQuestions(IDs, responseInsertQuestion.getId(),responseInsertQuestion.getPosition(),get_table_count("question"))
	if isinstance(responseInsertQuestion,Question):
		my_dict = {"id":responseInsertQuestion.getId()}
		jsondata = to_json(my_dict) 
	return jsondata, 200


@app.route('/questions/<int:question_id>', methods=['DELETE'])
def DeleteQuestion(question_id):
	try:
		print(request.headers.get('Authorization').split(" ")[1])
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	try:
		response = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "id", question_id)
		response[0]
		deleteQuestion(question_id)
		updatePositionQuestionsForDeletion(response[0]['position'])
		return "",204
	except:
		return "Error occured", 404


@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestion():
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	deleteAllQuestion()
	return "",204


		

@app.route('/questions/<int:question_id>', methods=['GET'])
def GetQuestionsInfoById(question_id):
	try:
		responseSelectQuestion = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "id", question_id)
		responseSelectAnswers = getColumnsFromTableByColumn("poss_answers", ['id','id_quest', 'text', 'isCorrect', 'position'], "id_quest", responseSelectQuestion[0]['id'])
		question = Question(responseSelectQuestion[0]['position'],responseSelectQuestion[0]['title'],responseSelectQuestion[0]['text'],responseSelectQuestion[0]['image'])
		question.setId(responseSelectQuestion[0]['id']) 
		posAns = createPossAnswers(responseSelectAnswers, id_quest=responseSelectQuestion[0]['id'])
		question.setPossibleAnswers(posAns)
		return str(question), 200
	except:
		return "Error occured", 404


@app.route('/questions', methods=['GET'])
def GetQuestionsInfo():
	position = request.args.get('position')
	try:
		responseSelectQuestion = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "position", position)
		responseSelectAnswers = getColumnsFromTableByColumn("poss_answers", ['id','id_quest', 'text', 'isCorrect', 'position'], "id_quest", responseSelectQuestion[0]['id'])
		question = Question(responseSelectQuestion[0]['position'],responseSelectQuestion[0]['title'],responseSelectQuestion[0]['text'],responseSelectQuestion[0]['image'])
		question.setId(responseSelectQuestion[0]['id']) 
		posAns = createPossAnswers(responseSelectAnswers,id_quest=responseSelectQuestion[0]['id'])
		question.setPossibleAnswers(posAns)
		return str(question), 200
	except:
		return "Error occured", 404
@app.route('/questions/<int:question_id>', methods=['PUT'])
def UpdateQuestion(question_id):
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	#Get and create new Question (the one that will Replace)
	try:
		response = getColumnsFromTableByColumn("question", ['id','position', 'title', 'text', 'image'], "id", question_id)
		print(response[0])
		newQuestionJSON = request.get_json()
		updatedQuestion = Question(newQuestionJSON['position'],newQuestionJSON['title'],newQuestionJSON['text'],newQuestionJSON['image'])
		newPossibleAnswers = createPossAnswers(newQuestionJSON['possibleAnswers'], question_id)
		updatedQuestion.setPossibleAnswers(newPossibleAnswers)
		updatedQuestion.setId(question_id)
		IDs = getIdsOfPostionsToUpdate(newQuestionJSON['position'],response[0]['position'])
		updateQuestion(updatedQuestion,newQuestionJSON['possibleAnswers'])
		updatePositionQuestions(IDs,question_id,newQuestionJSON['position'],response[0]['position'])
		return "",204
	except:
		return "Error occured", 404


@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipants():
	try:
		decode_token(request.headers.get('Authorization').split(" ")[1])
	except:
		print("Unauthorized")
		return "",401
	deleteAllParticipants()
	return "",204


@app.route('/participations', methods=['POST'])
def PostParticipants():
	try:
		jsonInput = request.get_json()
		number_of_answer = len(jsonInput['answers'])
		if get_table_count("question") != number_of_answer:
			return "",400
		partipationObj = postParticipation(jsonInput)
		return str(partipationObj),200
	except:
		return "Error Occured", 500

if __name__ == "__main__":
    app.run()
