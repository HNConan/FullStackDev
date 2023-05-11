import sqlite3
from Question import Question



def insertQuestionToBDD(question):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    # Créer une instance de la classe Question avec les valeurs souhaitées
    question = Question(position=question['position'], title=question['title'], text=question['text'], image=question.get('image', ''), possibleAnswers=question['possibleAnswers'])
    # Générer la requête SQL INSERT avec les valeurs de l'objet
    requete = "INSERT INTO question (position, title, text, image, possibleAnswer1, possibleAnswer2, possibleAnswer3, possibleAnswer4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    # Exécuter la requête SQL
    cur.execute(requete, (question.getPosition(), question.getTitle(), question.gettext(), question.getImage(), question.getPossibleAnswers()[0], question.getPossibleAnswers()[1], question.getPossibleAnswers()[2], question.getPossibleAnswers()[3]))
    # Valider la transaction
    conn.commit()
    # Récupérer l'ID de la question insérée
    question.setId(cur.lastrowid)
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    return question.getId()


def getColumnsFromTableById(table_name, columns, id):
    conn = sqlite3.connect('bdd.db')
    cur = conn.cursor()
    columns_str = ", ".join(columns)
    query = f"SELECT {columns_str} FROM {table_name} WHERE id=?"
    cur.execute(query, (id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result is None:
        return None  # Aucune ligne ne correspond à cet ID
    return dict(zip(columns, result))  # Retourne un dictionnaire avec les colonnes demandées







