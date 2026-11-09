from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_tutte_biblioteche():
        #recupera tutte le biblioteche presenti nella tabella "biblioteca" del database e
        #restituisce una lista di oggetti Biblioteca (DTO) o una lista vuota in caso di errore

        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database in BibliotecaDAO")
            return []
        cursor=cnx.cursor(dictionary=True)
        query= "SELECT * FROM biblioteca ORDER BY nome ASC"
        biblioteche= []
        try:
            cursor.execute(query)
            for row in cursor:
                b=Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                )
                biblioteche.append(b)
        except Exception as e:
            print(f"Errore durante l'esecuzione della query in BibliotecaDAO: {e}")

        finally:
            #chiusura di cursore e connessione
            cursor.close()
            cnx.close()

        return biblioteche
