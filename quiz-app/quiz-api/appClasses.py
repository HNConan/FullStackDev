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
            "possibleAnswers": [{'text':ans.getText(), 'isCorrect':ans.getIsCorrect()} for ans in self._possibleAnswers]
        }, ensure_ascii=False)
    
    def printQuestion(self):
        print(str(self))

class PossibleAnswer:
    def __init__(self, id_question, text, isCorrect):
        self._id_question = id_question
        self._text = text
        self._isCorrect = isCorrect
    
    # Getters
    def getId(self):
        return self._id
    
    def getIdQuestion(self):
        return self._id_question

    def getText(self):
        return self._text

    def getIsCorrect(self):
        return self._isCorrect

    # Setters
    def setId(self, id):
        self._id = id
    
    def setIdQuestion(self, id_question):
        self._id_question = id_question

    def setText(self, text):
        self._text = text

    def setIsCorrect(self, isCorrect):
        self._isCorrect = isCorrect

    # Autres méthodes
    def __str__(self):
        return str({
            "id": self._id,
            "text": self._text,
            "isCorrect": self._isCorrect
        })

    def printPossibleAnswer(self):
        print(str(self))

def createPossAnswers(answers):
    posAns = []
    for ans in answers:
        objAns = PossibleAnswer(int(ans['id_quest']), ans['text'], ConvertBoolIntIsCorrect(ans['isCorrect']))
        objAns.setId(int(ans['id']))
        posAns.append(objAns)
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
    