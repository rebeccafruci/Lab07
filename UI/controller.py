import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = "NONE"
        self.genere_selezionato = "NONE"

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        #popola i menu a tendina (Dropdown) delle biblioteche e dei generi
        #leggendo i dati dal Model all'avvio dell'applicazione
        try:
            #recupero la lista delle biblioteche dal Modello
            biblioteche= self._model.get_biblioteche()

            #pulisco e imposto l'opzione di default "nessun filtro" (chiave= NONE)
            self._view.dd_biblioteche.options.clear()
            self._view.dd_biblioteche.options.append(
                ft.dropdown.Option(key="NONE", text="Nessun filtro")
            )

            for b in biblioteche:
                self._view.dd_biblioteche.options.append(
                    ft.dropdown.Option(key=str(b.id), text=b.nome)
                )

        #recupero la lista dei generi dal Modello
            generi=self._model.get_generi()
            self._view.dd_generi.options.clear()
            self._view.dd_generi.options.append(
                ft.dropdown.Option(key="NONE", text="Nessun filtro")
            )

            for g in generi:
                self._view.dd_generi.options.append(
                    ft.dropdown.Option(key=g, text=g)
                )

            # Imposto "NONE" come valore iniziale sia nei Dropdown che nelle variabili del Controller
            self._view.dd_biblioteche.value = "NONE"
            self._view.dd_generi.value = "NONE"

            self.biblioteca_selezionata = "NONE"
            self.genere_selezionato = "NONE"

        # Aggiorno l'interfaccia grafica
            self._view.update()

        except Exception as ex:
            self._view.show_alert(f"Errore durante il popolamento dei filtri: {ex}")

        # --- CALLBACKS DROPDOWN ---


    def read_biblioteca(self, e):
        """
        Callback associata alla selezione di una biblioteca dal Dropdown.
        Salva la selezione corrente nella variabile d'istanza.
        """
        self.biblioteca_selezionata = self._view.dd_biblioteche.value


    def read_genere(self, e):
        """
        Callback associata alla selezione di un genere dal Dropdown.
        Salva la selezione corrente nella variabile d'istanza.
        """
        self.genere_selezionato = self._view.dd_generi.value

        # --- AZIONE: MOSTRA LIBRI ---


    def handle_mostra_libri(self, e):
        """
        Handler associato al click del pulsante 'Mostra Libri'.
        Recupera i libri filtrati dal Model e li mostra nella ListView.
        """
        try:
            # Assicuriamo che le variabili abbiano i valori correnti dai Dropdown
            valore_biblio = self._view.dd_biblioteche.value if self._view.dd_biblioteche.value else self.biblioteca_selezionata
            valore_genere = self._view.dd_generi.value if self._view.dd_generi.value else self.genere_selezionato

            # Recupero i libri filtrati invocando il metodo del Model (con COALESCE SQL)
            libri = self._model.get_libri_filtrati(valore_biblio, valore_genere)

            # Pulisco i risultati precedenti dalla ListView
            self._view.lv_libri.controls.clear()

            if not libri:
                # Se nessun libro corrisponde ai filtri prescelti, mostro un Alert
                self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio selezionati!")
            else:
                # Popolo la ListView aggiungendo oggetti ft.Text
                for l in libri:
                    self._view.lv_libri.controls.append(ft.Text(f"• {l}"))

            # Aggiorno il rendering grafico della View
            self._view.update()

        except Exception as ex:
            self._view.show_alert(f"Errore durante il recupero dei libri: {ex}")