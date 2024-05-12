import flet as ft
from flet import theme
from flet import Page as page 

def pagina4():

    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False


    #creamos los container de botones
    nom_generos = ["POP","TRAP","ALTERNATIVA","REGGATON","RAP", "CUMBIA","ROCK","REGGAE","SALSA"]
    page.scroll = ft.ScrollMode.ALWAYS

    botones = []
    for nombre in nom_generos:
        botones.append(ft.FilledButton(text=nombre,style = ft.ButtonStyle(
                                color={                                    
                                    ft.MaterialState.HOVERED: ft.colors.BLACK,
                                    ft.MaterialState.FOCUSED: ft.colors.YELLOW,
                                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                },
                                bgcolor= ft.colors.with_opacity(0.9, ft.colors.LIME_ACCENT_700)
                            ),width=230,height=70),
                       )
        

    contain_botones = []
    for boton in botones:
        contain_botones.append(
            ft.Container(
                content=boton,                
                margin=10,
                padding=0,
                alignment=ft.alignment.center,
                width=250,
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

    # print(filas)
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
                    src=f"./imagenes/Bad-Bunny.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.7,   
                )
    
    imagen_verde = ft.Image(
                    src=f"./imagenes/azul.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.5,   
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

    return st