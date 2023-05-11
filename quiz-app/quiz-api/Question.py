class Question:
    def __init__(self, id, position, title, text, image, possibleAnswers):
        self._id = id
        self._position = position
        self._title = title
        self._text = text
        self._image = image
        self._possibleAnswers = possibleAnswers

    def __init__(self, position, title, text, image, possibleAnswers):
        self._position = position
        self._title = title
        self._text = text
        self._image = image
        self._possibleAnswers = possibleAnswers
    
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
    def __str__(self):
        return f"Question {self._id}: {self._title}"
    
    def printQuestion(self):
        print(f"Question {self._id}: {self._title}")
