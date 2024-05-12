import flet as ft
from flet import theme
import pymysql



def get_usuario_genero(id_usuario):
  mycon = pymysql.connect(
  host='localhost', 
  port=3307, 
  user='root', 
  password='', 
  database='spotify'
)
  
    cursor = mycon.cursor()
    ejecutorDeQueries=mycon.cursor()
    consulta = f"SELECT genero_musical.nombre FROM gustos \
                INNER JOIN genero_musical ON gustos.id_genero = genero_musical.id_genero \
                WHERE gustos.id_usuario = {id_usuario}"
    ejecutorDeQueries.execute(consulta)
    resultados = cursor.ferchall()
    cursor.close()
    mycon.close()

    return [resultado[0] for resultado in resultados]
    

























def main(page: ft.Page):
    page.title = "Flet Project"

    page.theme = theme.Theme(color_scheme_seed="green", font_family="Gotham")
    page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    row_image_and_text = ft.Row(
        [
            ft.Image(src='./persona2.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            ft.Text("Dasha, 23", size=40, weight=ft.FontWeight.BOLD),
            ft.Text("I love music! I'd love to find \nnew songs and people who would \nlike to listen those songs with me!", theme_style=ft.TextThemeStyle.TITLE_LARGE),
        ],
        alignment=ft.MainAxisAlignment.START   
    )


    btn_rechazar = ft.FilledButton("Rechazar", on_click=lambda e:print("Rechazar"))
    row_button1 = ft.Row(
        [
            btn_rechazar
        ],
        alignment=ft.MainAxisAlignment.START 
    )

    btn_aceptar = ft.FilledButton("Aceptar", on_click= lambda e: print("Aceptar"))
    row_button2 = ft.Row(
        [
            btn_aceptar
        ],
        alignment=ft.MainAxisAlignment.START   
    )

    row_genres = ft.Row(
        [

        ],
        alignment=ft.MainAxisAlignment.START
    )
        

    

    stack = ft.Stack(
            [
                ft.Container(height=100),
                ft.Image(
                    src=f"./fondo.jpg",
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
                                ft.FilledButton("Settings", on_click=print("Settings"))
                            ],
                            alignment=ft.MainAxisAlignment.START
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                

                ft.Column(
                    [
                        row_image_and_text,
                        row_button1,
                        row_button2
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    height= 300
                )
            ]
        )
    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False
    page.add(stack)
ft.app(main)
