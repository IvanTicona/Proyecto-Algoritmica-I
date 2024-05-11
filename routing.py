import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    pagetow = ft.Stack(
            [
                # ft.Image(
                #     src=f"./Landing.jpg",
                #     width=page.window_width,
                #     height=page.window_height,
                #     fit=ft.ImageFit.COVER,
                #     opacity=0.7,   
                # ),
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text("| FaveFusion",
                                        size=40, 
                                        weight=ft.FontWeight.BOLD, 
                                        text_align=ft.TextAlign.START,
                                        color=ft.colors.GREEN_400,
                                    ),
                                    margin=ft.margin.only(top=0, left=30, right=0, bottom=0),
                                ),
                                ft.Container(
                                    content = ft.Row(
                                        [
                                            ft.FilledButton("Login", height=40, width=120),
                                            ft.FilledButton("Playlist", height=40, width=120),
                                            ft.FilledButton("Settings", height=40, width=120),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        width=400,
                                    ),
                                    margin=ft.margin.only(top=10, left=0, right=30, bottom=0)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            width=page.window_width,
                        ),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Container(
                                            content = ft.Row(
                                                [
                                                    ft.FilledButton("Buscar por Genero", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                    ft.FilledButton("Buscar por artista", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                width=page.window_width*0.7,
                                            ),
                                            margin=ft.margin.only(top=0, left=0, right=30, bottom=0),
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    height=50
                                ),
                                ft.Row(
                                    [
                                        ft.Container(
                                            content = ft.Row(
                                                [
                                                    ft.FilledButton("Agregar genero a mi perfil", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                    ft.FilledButton("Eliminar genero de mi perfil", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                width=page.window_width*0.7,
                                            ),
                                            margin=ft.margin.only(top=0, left=0, right=30, bottom=0)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    height=50
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            height=500,
                            spacing=60
                        )
                    ]
                ),
            ],
            height=page.window_height
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        pagetow,
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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