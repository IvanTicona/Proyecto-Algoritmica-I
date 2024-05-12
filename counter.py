import flet as ft
from flet import theme

def main(page: ft.Page):
    page.title = "Flet Proyect"

    page.theme = theme.Theme(color_scheme_seed="green", font_family="Gotham")
    page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()

    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()

    # ft.Container(
    #   image_src='./Landing.jpg',
    #   image_fit= ft.ImageFit.COVER,
    #   expand=True,
    #   padding= ft.padding.all(0),
    #   margin= ft.margin.all(0),
    #   #content=ft.Control()
    # ),

    page.add(
        ft.Stack(
            [
                ft.Image(
                    src=f"./Landing.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Row(
                    [
                        ft.Text("FaveFusion",
                            size=40, 
                            weight=ft.FontWeight.BOLD, 
                            text_align=ft.TextAlign.START, 
                            width=page.window_width * 0.3,
                            color=ft.colors.GREEN_500
                        ),
                        ft.Row(
                            [
                                ft.FilledButton("Login", on_click=print("Login")),
                                ft.FilledButton("Playlist", on_click=print("Playlist")),
                                ft.FilledButton("Settings", on_click=print("Settings")),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            # width=page.window_width * 0.7
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    # padding=ft.padding.all(20),
                ),
                # ft.Container(
                #   image_src='./Landing.jpg',
                #   image_fit= ft.ImageFit.COVER,
                #   expand=True,
                #   padding= ft.padding.all(0),
                #   margin= ft.margin.all(0),
                #   #content=ft.Control()
                # ),
            ],
            
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