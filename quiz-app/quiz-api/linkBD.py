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
    requete = "INSERT INTO poss_answers (id_quest, text, isCorrect) VALUES (?, ?, ?)"
    # Exécuter la requête SQL
    cur.execute(requete, (objPosAnswer.getIdQuestion(), objPosAnswer.getText(), ConvertBoolIntIsCorrect(objPosAnswer.getIsCorrect())))
    # Valider la transaction
    conn.commit()
    # Récupérer l'ID de la question insérée
    objPosAnswer.setId(cur.lastrowid)
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()

def insertPossibleAnswersToBDD(id_quest,answers):
    possAnswers = []
    for oneAns in answers:
        objectAnswer = PossibleAnswer(id_quest, oneAns['text'], oneAns['isCorrect'])
        insertOneAnswerToBDD(objectAnswer)
        possAnswers.append(objectAnswer)
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







