import flet as ft
from flet import Page as page
from LandingPage import landingPage
from pagina4 import pagina4

def main(page: ft.Page):
    page.title = "Routes Example"

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
                            landingPage,
                            ft.ElevatedButton("<-", on_click=lambda _: page.go("/store")),
                        ]
                    )
                ],
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
                            ft.ElevatedButton("<-", on_click=lambda _: page.go("/")),
                        ]
                      )
                    ],
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