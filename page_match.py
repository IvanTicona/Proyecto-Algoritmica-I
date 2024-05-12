import flet as ft
from flet import theme

def main(page: ft.Page):
    page.title = "Flet Project"

    page.theme = theme.Theme(color_scheme_seed="green", font_family="Gotham")
    page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    row_image_and_text = ft.Row(
        [
            ft.Image(src='./persona.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            ft.Text("MATCH", size=40, weight=ft.FontWeight.BOLD),
            ft.Image(src='./persona.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
        ],
        alignment=ft.MainAxisAlignment.CENTER,    
    )


    hover_style = ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=10))
    btn_message=ft.FilledButton("Mensaje", on_click= lambda e: print("noseeeee"), on_hover=lambda e: (setattr(btn_message, "style", hover_style)))
    row_message = ft.Row(
        [
            btn_message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    stack = ft.Stack(
            [
                ft.Container(height=100),
                ft.Image(
                    src=f"./match.png",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                ),     
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "| FaveFusion",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.START,
                                width=page.window_width * 0.3,
                                color=ft.colors.GREEN_400
                            ),
                            margin=ft.margin.only(top=0, left=30, right=0, bottom=0)
                        ),
                        ft.Row(
                            [
                                ft.FilledButton("Login", on_click=print("Login")),
                                ft.FilledButton("Playlist", on_click=print("Playlist")),
                                ft.FilledButton("Settings", on_click=print("Settings")),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                
                ft.Column(
                    [
                        row_image_and_text,
                        row_message
                    
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    height= 500
                )
            ]
        )
    page.window_width = 1000
    page.windo_height = 600
    page.window_resizable = False
    page.add(stack)
ft.app(main)
