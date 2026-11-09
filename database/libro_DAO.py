from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
LIBRO DAO
Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_generi():
        """Recupera la lista distinta dei generi dal DB."""
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database in LibroDAO.get_generi()")
            return []

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT DISTINCT genere 
            FROM libro 
            WHERE genere IS NOT NULL AND genere != '' 
            ORDER BY genere ASC
        """

        generi = []
        try:
            cursor.execute(query)
            for row in cursor:
                generi.append(row["genere"])
        except Exception as e:
            print(f"Errore durante la query generi: {e}")
        finally:
            cursor.close()
            cnx.close()

        return generi

    @staticmethod
    def get_libri_filtrati(id_biblioteca=None, genere=None):
        """
        Recupera i libri filtrati dal database per id_biblioteca e/o genere.
        Sfrutta COALESCE in SQL per i filtri opzionali.
        """
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database in LibroDAO.get_libri_filtrati()")
            return []

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT l.id, l.titolo, l.autore, l.genere, l.anno, l.id_biblioteca
            FROM libro l
            WHERE l.id_biblioteca = COALESCE(%s, l.id_biblioteca)
              AND l.genere = COALESCE(%s, l.genere)
            ORDER BY l.titolo ASC
        """

        libri = []
        try:
            cursor.execute(query, (id_biblioteca, genere))
            for row in cursor:
                libro = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno=row["anno"],
                    id_biblioteca=row["id_biblioteca"]
                )
                libri.append(libro)
        except Exception as e:
            print(f"Errore durante la lettura dei libri filtrati: {e}")
        finally:
            cursor.close()
            cnx.close()

        return libri