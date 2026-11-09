from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_tutte_biblioteche()


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()




    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        #traduzione dei valori UI: se l'utente ha scelto 'NONE' o stringa vuota, passiamo None
        id_biblioteca= int(biblioteca) if biblioteca and biblioteca!="NONE" else None
        genere_filtrato= genere if genere and genere!="NONE" else None

        #chiamata al metodo del DAO che esegue la query SQL con COALESCE()
        return self._libro_dao.get_libri_filtrati(id_biblioteca, genere_filtrato)





