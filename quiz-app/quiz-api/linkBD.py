import sqlite3
from appClasses import *

#Questions Methods

def insertQuestionToBDD(question):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Créer une instance de la classe Question avec les valeurs souhaitées
    questionObject = Question(position=question['position'], title=question['title'], text=question['text'], image=question.get('image', ''))
    # Générer la requête SQL INSERT avec les valeurs de l'objet
    requete = "INSERT INTO question (position, title, text, image) VALUES (?, ?, ?, ?)"
    # Exécuter la requête SQL
    cur.execute(requete, (questionObject.getPosition(), questionObject.getTitle(), questionObject.gettext(), questionObject.getImage()))
    # Valider la transaction
    conn.commit()
    # Récupérer l'ID de la question insérée
    questionObject.setId(cur.lastrowid)
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    return questionObject


def insertOneAnswerToBDD(objPosAnswer):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL INSERT avec les valeurs de l'objet
    requete = "INSERT INTO poss_answers (id_quest, text, isCorrect, position) VALUES (?, ?, ?, ?)"
    # Exécuter la requête SQL
    cur.execute(requete, (objPosAnswer.getIdQuestion(), objPosAnswer.getText(), ConvertBoolIntIsCorrect(objPosAnswer.getIsCorrect()), objPosAnswer.getPosition()))
    # Valider la transaction
    conn.commit()
    # Récupérer l'ID de la question insérée
    objPosAnswer.setId(cur.lastrowid)
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()

def insertPossibleAnswersToBDD(id_quest,answers):
    possAnswers = []
    index = 0
    for oneAns in answers:
        objectAnswer = PossibleAnswer(id_quest, oneAns['text'], oneAns['isCorrect'], index)
        insertOneAnswerToBDD(objectAnswer)
        possAnswers.append(objectAnswer)
        index += 1
    return possAnswers
    

def getColumnsFromTableByColumn(table_name, columns, nameOfColumn, valOfColumn):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    columns_str = ", ".join(columns)
    query = f"SELECT {columns_str} FROM {table_name} WHERE {nameOfColumn}=?"
    cur.execute(query, (valOfColumn,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    if results is None:
        return None  # Aucune ligne ne correspond à cet ID
    return [dict(zip(columns, row)) for row in results]  # Retourne une liste de dictionnaires avec les colonnes demandées


def updateQuestion(objQuestion, possAnswersJson):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "UPDATE question SET position = ?, title = ?, text = ?, image = ? WHERE id = ?"
    # Exécuter la requête SQL
    cur.execute(requete, (objQuestion.getPosition(), objQuestion.getTitle(), objQuestion.gettext(), objQuestion.getImage(), objQuestion.getId()))
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    updatePossiblesAnswers(objQuestion.getId(),possAnswersJson)


def updatePossiblesAnswers(id_quest ,objPosAnswer):
    deleteAllAnswersOfQuest(id_quest)
    insertPossibleAnswersToBDD(id_quest, objPosAnswer)

def deleteQuestion(idQuestion):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM question WHERE id = ?"
    # Exécuter la requête SQL
    cur.execute(requete, (idQuestion , ))
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    deleteAllAnswersOfQuest(idQuestion)

def deleteAllQuestion():
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM question"
    # Exécuter la requête SQL
    cur.execute(requete)
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    deleteAllAnswers()


def deleteAllParticipants():
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM participants"
    # Exécuter la requête SQL
    cur.execute(requete)
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()

def deleteAllAnswers():
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM poss_answers"
    # Exécuter la requête SQL
    cur.execute(requete)
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()

def deleteAllAnswersOfQuest(id_quest):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM poss_answers WHERE id_quest = ?"
    # Exécuter la requête SQL
    cur.execute(requete, ( id_quest,))
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()

def deleteAnswer(id_quest, position):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Générer la requête SQL UPDATE avec les nouvelles valeurs de l'objet
    requete = "DELETE FROM poss_answers WHERE (id_quest = ?) AND (position = ?))"
    # Exécuter la requête SQL
    cur.execute(requete, (id_quest, position))
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()



