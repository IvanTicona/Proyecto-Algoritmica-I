import flet as ft
from flet import theme

def main(page: ft.Page):
    page.title = "Flet Project"

    page.theme = theme.Theme(color_scheme_seed="green", font_family="Gotham")
    page.update()

    # Crear las imágenes y el texto "MATCH"
    image1 = ft.Image(src='./persona.png', width=200, height=200, fit=ft.ImageFit.CONTAIN)
    image2 = ft.Image(src='./persona.png', width=200, height=200, fit=ft.ImageFit.CONTAIN)
    match_text = ft.Text("MATCH", size=40, weight=ft.FontWeight.BOLD)

    # Crear una fila con las imágenes y el texto centrados
    images_and_text = ft.Row([
        #ft.Container(content=image1),
        #ft.Container(content=match_text),
        #ft.Container(content=image2),
        image1, image2
    ], alignment=ft.MainAxisAlignment.CENTER)

    # Crear un Stack para centrar las imágenes y el texto verticalmente
    stack = ft.Stack([
        images_and_text,
    ], alignment=ft.MainAxisAlignment.CENTER)

    # Agregar el Stack a la página
    page.add(stack)

ft.app(main)