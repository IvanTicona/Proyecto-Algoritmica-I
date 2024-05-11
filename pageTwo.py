import flet as ft
from flet import theme

def main(page: ft.Page):
    page.title = "Flet Proyect"

    # page.theme = theme.Theme(color_scheme_seed=ft.colors.GREEN_500, font_family="Gotham")
    # page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False
    # page.scroll = ft.ScrollMode.ALWAYS

    page.add(
        ft.Stack(
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
        ),

        # ft.Row(
        #     [
        #         ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
        #         txt_number,
        #         ft.IconButton(ft.icons.ADD, on_click=plus_click),
        #     ],
        #     alignment=ft.MainAxisAlignment.CENTER,
        # )
    )

ft.app(main)