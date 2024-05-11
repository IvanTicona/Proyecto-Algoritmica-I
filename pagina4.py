import flet as ft
from flet import theme


def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN,
            primary_container=ft.colors.GREEN_200
            # ...
        ),
    )
    #creamos los container de botones
    nom_generos = ["POP","TRAP","ALTERNATIVA","REGGATON","RAP", "CUMBIA","ROCK","REGGAE","SALSA"]
    page.scroll = ft.ScrollMode.ALWAYS

    botones = []
    for nombre in nom_generos:
        botones.append(ft.FilledButton(text=nombre,style = ft.ButtonStyle(
                                color={
                                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                },
                            ),width=200,height=60),
                       )
        

    contain_botones = []
    for boton in botones:
        contain_botones.append(
            ft.Container(
                content=boton,                
                margin=20,
                padding=0,
                alignment=ft.alignment.center,
                width=300,
                height=80,
                border_radius=10,
                ink=True,
            )
    )            
    
    filas = []
    contador = 1
    fila = []
    for boton in contain_botones: #este for crea las filas en flet y los guarda en la matriz
        fila.append(boton)
        if(contador % 3 == 0):
            # print(fila)
            filas.append(
                    ft.Row(controls=fila, alignment=ft.MainAxisAlignment.CENTER)                                    
            )
            # fila[int(contador/3)-1].spacing = 20
            fila = []
        contador = contador+1

    print(filas)
    col = ft.Column(filas,alignment=ft.MainAxisAlignment.CENTER)

    matriz_generos = ft.Column([
                ft.Container(
                    content=col,
                    height=page.window_height
                    # bgcolor=ft.colors.AMBER_100,
                    # height=400,
                ),
            ]
            
    )
    
    bar = ft.Row([
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
        )],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=page.window_width,
    )
    imagen_fondo = ft.Image(
                    src=f"C:/Users/pablo/Desktop/project/ProyectoAlgoritmicaI/imagenes/Bad-Bunny.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.9,   
                )
    
    imagen_verde = ft.Image(
                    src=f"C:/Users/pablo/Desktop/project/ProyectoAlgoritmicaI/imagenes/verde_oscuro.png",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.8,   
                )

    st = ft.Stack([imagen_fondo,imagen_verde,bar,
                   ft.Row(
            [
                matriz_generos
            ]
            ,
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        )])

    page.add(
        st
        
    )

ft.app(main)