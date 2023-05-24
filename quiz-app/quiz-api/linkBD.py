import sqlite3
from appClasses import *

#Questions Methods

def createDB():
    # Connexion à la base de données
    conn = sqlite3.connect('bdd.db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS question')
    c.execute('DROP TABLE IF EXISTS participants')
    c.execute('DROP TABLE IF EXISTS poss_answers')


    # Création de la table "question"
    c.execute('''CREATE TABLE IF NOT EXISTS question
                 (id INTEGER PRIMARY KEY,
                 position INTEGER,
                 title TEXT,
                 text TEXT,
                 image NUMERIC)''')

    # Création de la table "participants"
    c.execute('''CREATE TABLE IF NOT EXISTS participants
                 (id INTEGER PRIMARY KEY,
                 pseudo TEXT,
                 score INTEGER,
                 answers TEXT)''')

    # Création de la table "poss_answers"
    c.execute('''CREATE TABLE IF NOT EXISTS poss_answers
                 (id INTEGER PRIMARY KEY,
                 id_quest INTEGER,
                 text TEXT,
                 isCorrect INTEGER,
                 position INTEGER)''')

    # Fermeture de la connexion à la base de données
    conn.close()



def get_table_count(tableName):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    
    # Exécutez la requête pour compter le nombre d'éléments dans la table
    query = f"SELECT COUNT(*) FROM {tableName}"
    cur.execute(query)
    
    # Récupérez le résultat de la requête
    count = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return count


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

def getIdsOfPostionsToUpdate(new_position, old_position):
    if(new_position == old_position):
        return
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    if(new_position < old_position):
        requete = f"SELECT id, position FROM question WHERE position BETWEEN {new_position} AND {old_position} ORDER BY position"
    elif(new_position > old_position):
        requete = f" SELECT id, position FROM question WHERE position > {old_position} AND position <= {new_position} ORDER BY position"
    cur.execute(requete)
    results = cur.fetchall()
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    return results

def updatePositionQuestions(IDs,question_id,new_position, old_position):
    if(new_position == old_position):
        return
    for row in IDs:
        if question_id == row[0]:
            continue
        conn = sqlite3.connect('bdd.db')
        cur = conn.cursor()
        if(new_position < old_position):
            requete = "UPDATE question SET position = position + 1 WHERE id = ?"
        elif(new_position > old_position):
            requete = "UPDATE question SET position = position - 1 WHERE id = ?"

        cur.execute(requete,(row[0], ))
        # Valider la transaction
        conn.commit()
        # Fermer le curseur et la connexion à la base de données
        cur.close()
        conn.close()

def updatePositionQuestionsForDeletion(old_position):
    
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    requete = f"UPDATE question SET position = position - 1 WHERE position > {old_position}"
    cur.execute(requete)
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    

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

def postParticipation(participationJSON):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Créer une instance de la classe Question avec les valeurs souhaitées
    participObject = Participation(participationJSON['playerName'], participationJSON['answers'])
    tabGoodAns = getGoodAnswers()
    participObject.calculate_score(tabGoodAns)
    # Générer la requête SQL INSERT avec les valeurs de l'objet
    requete = "INSERT INTO participants (pseudo, answers, score) VALUES (?, ?, ?)"
    # Exécuter la requête SQL
    cur.execute(requete, (participObject.get_pseudo(), str(participObject.get_answers()), participObject.get_score()))
    # Valider la transaction
    conn.commit()
    # Récupérer l'ID de la participation insérée
    participObject.set_id(cur.lastrowid)
    
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    return participObject

def getAllParticipants():
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    query = "SELECT * FROM participants"
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    if results is None:
        return None
    finalTab = []  
    for row in results:
        answers = row[3][1:-1].split(", ")
        answers = [int(element) for element in answers]
        newParticipant = Participation(row[1],answers,row[2])
        newParticipant.set_id(row[0]) 
        finalTab.append(newParticipant)
    return finalTab  # Retourne une liste de dictionnaires avec les colonnes demandées

def getGoodAnswerForQuestion(positionQuest):
    id_quest = getColumnsFromTableByColumn("question", ["id"], "position", positionQuest)
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    query = f"SELECT position FROM poss_answers WHERE id_quest=? AND isCorrect = 1"
    cur.execute(query, (id_quest[0]['id'],))
    results = cur.fetchone()
    cur.close()
    conn.close()
    if results is None:
        return None  # Aucune ligne ne correspond à cet ID
    return results[0]

def getGoodAnswers():
    numOfQuest = get_table_count("question")
    tabGoodAns = []
    for i in range(1, numOfQuest+1):
        posGoodAns = getGoodAnswerForQuestion(i)
        tabGoodAns.append(posGoodAns+1)
    return tabGoodAns

def getScores(tabOfPart):
    scores = [] 
    for particip in tabOfPart:
        scores.append(particip.to_dict())
    return sorted(scores, key=lambda x: x['score'],reverse=True)