import flet as ft
from flet import Page as page
#Importamos las paginas
from LandingPage import LandingPage
from GenresPage import GenresPage
from PersonPage import PersonPage
from MatchPage import MatchPage
from LoginPage import LoginPage


class DataUserProvider():
    def __init__(self, initial_data=None):
        self.value = initial_data

    def get_data_user(self):
        return self.value

    def set_data_user(self, data):
        self.value = data

data_user_provider = DataUserProvider(initial_data={
    "ID": "",
    "username": "",
    "email": "",
    "password": "",
    "age": ""
})


def main(page: ft.Page):

    page.title = "Nombre de la aplicacion"

    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False

    name = ft.Text(data_user_provider.get_data_user()["username"])

    def changeName(data):
        data_user_provider.set_data_user(data)
        name.value = data_user_provider.get_data_user()["username"]
        print(data_user_provider.get_data_user())
        page.update()
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    LoginPage(page, changeName),
                ]
            )
        )
        if page.route == "/home":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Stack(
                            [
                                LandingPage(page, data_user_provider.get_data_user()),
                            ]
                        )
                    ]
                )
            )
        if page.route == "/genres":
            page.views.append(
                ft.View(
                    "/genres",
                    [
                      ft.Stack(
                        [
                            GenresPage(page, 7),
                        ]
                      )
                    ]
                )
            )
        if page.route == "/person":
            page.views.append(
                ft.View(
                    "/person",
                    [
                        PersonPage(page),
                    ],
                    scroll= ft.ScrollMode.ALWAYS
                )
            )
        if page.route == "/match":
            page.views.append(
                ft.View(
                    "/match",
                    [
                        MatchPage(page),
                    ]
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