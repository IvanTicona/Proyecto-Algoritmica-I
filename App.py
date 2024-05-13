import flet as ft
from flet import Page as page
#Importamos las paginas
from LandingPage import LandingPage
from pagina4 import pagina4
# from LoginPage import LoginPage

class DataUserProvider():
    def __init__(self, initial_data=None):
        self.value = initial_data

    def get_data_user(self):
        return self.value

    def set_data_user(self, data):
        self.value = data

data_user_provider = DataUserProvider(initial_data={
    "username": "Dorian",
})

#Funcion principal
def main(page: ft.Page):


    page.title = "Nombre de la aplicacion"

    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Stack(
                        [
                            # ft.Text("Bienvenido a la aplicacion", size= 30),
                            # # mostrar el nombre del usuario
                            # ft.Text(data_user_provider.get_data_user()["username"]),
                            LandingPage(),
                            ft.ElevatedButton("Genres", on_click=lambda _: page.go("/store")),
                            # ft.ElevatedButton("Login", on_click=lambda _: page.go("/login")),
                        ]
                    )
                ]
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                    #   ft.Stack(
                        # [
                            # ft.Text("Genres", size=30),
                            # ft.Text(data_user_provider.get_data_user()["username"]),
                            ft.ElevatedButton("Menu", on_click=lambda _: page.go("/"), icon=ft.icons.ARROW_BACK),
                            pagina4(),
                        # ]
                    #   )
                    ],
                    # scroll=ft.ScrollMode.ALWAYS,
                )
            )
        page.update()



    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)