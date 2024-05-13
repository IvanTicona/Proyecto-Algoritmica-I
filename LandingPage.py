import flet as ft
from flet import Page as page
from database import *


def LandingPage(page: ft.Page, data_user, changeData):

    def logoutFn(e):
        changeData({
            "ID": 0,
            "username": "",
            "email": "",
            "password": "",
            "age": 0
        })
        page.go("/login")

    


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
                                    ft.FilledButton("Ver Datos", on_click= lambda e: print(data_user)),
                                    ft.Container(
                                        content = ft.Text("Welcome to FaveFusion !", size=30, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
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
                                                        ft.FilledButton( content= ft.Text("Buscar por Genero", size=17), on_click= lambda e: page.go("/person"), height=150, width=200, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                        ft.FilledButton(content= ft.Text("Logout", size=20), height=150, on_click= logoutFn, width=200, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    height=150,
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
                                                        ft.FilledButton(content = ft.Text("Agregar genero a mi perfil", size= 17), on_click= lambda e: page.go("/genres") , height=150, width=200, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                        ft.FilledButton(content = ft.Text("Ultimo Match", size=20), on_click= lambda e: page.go("/match"), height=150, width=200, style= ft.ButtonStyle(bgcolor= ft.colors.GREY_700, color= ft.colors.WHITE)),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    height=150,
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
