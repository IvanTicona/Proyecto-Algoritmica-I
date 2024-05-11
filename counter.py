import flet as ft
from flet import theme

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.START  # Cambiado a START para mover al inicio de la página
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.theme = theme.Theme(color_scheme_seed="green", font_family="Gotham")
    page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Text("Spotify Tinder", 
            size=50, 
            weight=ft.FontWeight.BOLD, 
            text_align=ft.TextAlign.CENTER, 
            width=1500,
            color=ft.colors.GREEN_500
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)