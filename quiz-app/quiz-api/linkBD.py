import sqlite3
from Question import Question



def insertQuestionToBDD():
    conn = sqlite3.connect('bdd.db')
    # Créer un curseur pour exécuter des requêtes
    cur = conn.cursor()
    # Créer une instance de la classe avec les valeurs souhaitées
    object = Question(0 ,"First"," LOLILOL")
    # Générer la requête SQL INSERT avec les valeurs de l'objet
    requete = "INSERT INTO question (position,title,questionText) VALUES ('{}', '{}','{}')".format(object.position, object.title,object.questionText)
    # Exécuter la requête SQL
    cur.execute(requete)
    # Valider la transaction
    conn.commit()
    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()
    return 200






