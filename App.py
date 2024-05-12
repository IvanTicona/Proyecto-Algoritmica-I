import flet as ft
from flet import Page as page
#Importamos las paginas
from LandingPage import LandingPage
from pagina4 import pagina4
from LoginPage import LoginPage

data_user = {
    "name": "",
    "email": "",
    "password": "",
    "age": "",
    "gender": ""
}

def button_clicked(e):
        data_user["name"] = nombre.value
        data_user["email"] = email.value
        data_user['password'] = password.value
        data_user['age'] = age.value
        data_user['gender'] = gender.value
        if not checkTerms.value:
            print("You have accepted the terms and conditions")
            return
        
        print(data_user)
        # Resetear los campos
        nombre.value = ""
        email.value = ""
        password.value = ""
        age.value = ""
        gender.value = ""
        page.update()


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
                            LandingPage(),
                            ft.ElevatedButton("Genres", on_click=lambda _: page.go("/store")),
                            ft.ElevatedButton("Login", on_click=lambda _: page.go("/login")),
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
                      ft.Stack(
                        [
                            pagina4(),
                            ft.ElevatedButton("Menu", on_click=lambda _: page.go("/"), icon=ft.icons.ARROW_BACK),
                        ]
                      )
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                )
            )
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        LoginPage(data_user,page, button_clicked),
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