import flet as ft
from flet import Page as page

AppBar = ft.Row(
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
)

def LandingPage(page: ft.Page):
    landingPage = ft.Stack(
                [
                    ft.Image(
                        src=f"./imagenes/Landing.jpg",
                        width=page.window_width,
                        height=page.window_height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7,   
                    ),
                    ft.Column(
                        [
                            AppBar,
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Container(
                                                content = ft.Row(
                                                    [
                                                        ft.FilledButton("Buscar por Genero", on_click= lambda e: page.go("/person"), height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                        ft.FilledButton("Buscar por artista", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    width=700,
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
                                                        ft.FilledButton("Agregar genero a mi perfil", on_click= lambda e: page.go("/genres") , height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                        ft.FilledButton("Eliminar genero de mi perfil", height=60, width=150, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                        
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    width=700,
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
    return landingPage
