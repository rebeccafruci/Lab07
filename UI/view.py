import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        #menu a tendina per la selezione della biblioteca
        self.dd_biblioteche = ft.Dropdown(
            label="Seleziona Biblioteca",
            width=350
        )

        self.dd_generi = ft.Dropdown(
            label="Seleziona Genere",
            width=350
        )

        # Sezione 3: Libri
        #pulsante per attivare il recupero dei libri filtrati
        pulsante_mostra_libri=ft.Button(
            "Mostra libri",
            on_click=self.controller.handle_mostra_libri if self.controller else None
        )

        #contenitore ListView per mostrare i libri trovati dal database
        self.lv_libri=ft.ListView(
            expand=False,
            height=250,
            spacing=5,
            padding=10,
            auto_scroll=True
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)


        #popolamento iniziale dei Dropdown tramite il Controller
        if self.controller:
            self.controller.popola_dropdown()

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Text("Seleziona filtri di ricerca", size=20, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[self.dd_biblioteche, self.dd_generi],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),

            # Sezione 3: Libri
            pulsante_mostra_libri,
            self.lv_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
