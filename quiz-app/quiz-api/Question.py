class Question:
    def __init__(self, id, position, title, questionText):
        self._id = id
        self._position = position
        self._title = title
        self._questionText = questionText
    def __init__(self, position, title, questionText):
        self._position = position
        self._title = title
        self._questionText = questionText
    
    # Getters
    def getId(self):
        return self._id
    
    def getPosition(self):
        return self._position
    
    def getTitle(self):
        return self._title
    
    def getQuestionText(self):
        return self._questionText
    
    # Setters
    def setId(self, id):
        self._id = id
        
    def setPosition(self, position):
        self._position = position
        
    def setTitle(self, title):
        self._title = title
        
    def setQuestionText(self, questionText):
        self._questionText = questionText
    
    # Autres méthodes
    def __str__(self):
        return f"Question {self._id}: {self._title}"
    
    def printQuestion(self):
        print(f"Question {self._id}: {self._title}")
