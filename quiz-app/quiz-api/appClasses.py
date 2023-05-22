import json
class Question:
    def __init__(self, position, title, text, image):
        self._position = position
        self._title = title
        self._text = text
        self._image = image

    # Getters
    def getId(self):
        return self._id
    
    def getPosition(self):
        return self._position
    
    def getTitle(self):
        return self._title
    
    def gettext(self):
        return self._text
    
    def getImage(self):
        return self._image
    
    def getPossibleAnswers(self):
        return self._possibleAnswers
    
    # Setters
    def setId(self, id):
        self._id = id
        
    def setPosition(self, position):
        self._position = position
        
    def setTitle(self, title):
        self._title = title
        
    def settext(self, text):
        self._text = text
        
    def setImage(self, image):
        self._image = image
        
    def setPossibleAnswers(self, possibleAnswers):
        self._possibleAnswers = possibleAnswers
    
    # Autres méthodes
    # Autres méthodes
    def __str__(self):
        return json.dumps({
            "id": self._id,
            "position": self._position,
            "title": self._title,
            "text": self._text,
            "image": self._image,
            "possibleAnswers": [{'idQuest': ans.getIdQuestion(),'text':ans.getText(), 'isCorrect':ans.getIsCorrect(), 'position': ans.getPosition()} for ans in self._possibleAnswers]
        }, ensure_ascii=False)
    
    def printQuestion(self):
        print(str(self))

class PossibleAnswer:
    def __init__(self, id_question, text, isCorrect, position):
        self._id_question = id_question
        self._text = text
        self._isCorrect = isCorrect
        self._position = position
    
    # Getters
    def getId(self):
        return self._id
    
    def getIdQuestion(self):
        return self._id_question

    def getText(self):
        return self._text

    def getIsCorrect(self):
        return self._isCorrect
    
    def getPosition(self):
        return self._position

    # Setters
    def setId(self, id):
        self._id = id
    
    def setIdQuestion(self, id_question):
        self._id_question = id_question

    def setText(self, text):
        self._text = text

    def setIsCorrect(self, isCorrect):
        self._isCorrect = isCorrect

    def setPosition(self, position):
        self._position = position


    # Autres méthodes
    def __str__(self):
        return str({
            "id": self._id,
            'idQuest': self._id_question,
            "text": self._text,
            "isCorrect": self._isCorrect,
            "position": self._position
        })

    def printPossibleAnswer(self):
        print(str(self))


class Participation:
    def __init__(self, pseudo, answers=None, score=0):
        self._pseudo = pseudo
        self._answers = answers or []
        self._score = score

    # Getters
    def get_id(self):
        return self._id

    def get_pseudo(self):
        return self._pseudo

    def get_answers(self):
        return self._answers

    def get_score(self):
        return self._score

    # Setters
    def set_id(self, id):
        self._id = id

    def set_pseudo(self, pseudo):
        self._pseudo = pseudo

    def set_answers(self, answers):
        self._answers = answers

    def set_score(self, score):
        self._score = score

    # Autres méthodes utiles
    def add_answer(self, answer):
        self._answers.append(answer)

    def calculate_score(self, tabOfGoodAns):
        count = 0
        for i in range(len(tabOfGoodAns)):
            if self._answers[i] == tabOfGoodAns[i]:
                count += 1
        self._score = count
        

    def to_dict(self):
        return {
            "id": self._id,
            "playerName": self._pseudo,
            "answers": [answer for answer in self._answers],
            "score": self._score
        }

    # Autres méthodes
    def __str__(self):
        return json.dumps({
            "id": self._id,
            "playerName": self._pseudo,
            "answers": [answer for answer in self._answers],
            "score": self._score
        }, ensure_ascii=False)


def createPossAnswers(answers, id_quest=""):
    posAns = []
    if isinstance(id_quest, int):
        id_question = id_quest
    else:
        id_question =  int(ans['id'])
    index = 0
    for ans in answers:
        objAns = PossibleAnswer(id_question, ans['text'], ConvertBoolIntIsCorrect(ans['isCorrect']), index)
        posAns.append(objAns)
        index += 1
    return posAns

def ConvertBoolIntIsCorrect(val):
    if(val == True and isinstance(val,bool)):
        return 1
    if(val == False and isinstance(val,bool)):
        return 0
    if(int(val) == 1):
        return True
    if(int(val) == 0):
        return False

