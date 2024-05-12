import flet as ft
from flet import theme
from flet import Page as page 
import database as dt

def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

def pagina4():

    escogidos= [[] for _ in range(51)]

    #-------------------------------


    #-------------------------
    #configuracion de la pagina
    page.window_width = 1000
    page.window_height = 600
    page.window_resizable = False
    #-------------------------


    #---------------------------------
    #ponemos la imagen de fondo 
    imagen_fondo = ft.Image(
                    src=f"C:/Users/pablo/Desktop/project/ProyectoAlgoritmicaI/imagenes/Bad-Bunny.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.7,   
                )
    
    imagen_verde = ft.Image(
                    src=f"C:/Users/pablo/Desktop/project/ProyectoAlgoritmicaI/imagenes/azul.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                    opacity=0.5,   
                )
    #-----------------------------------------------------------------------------
     


    #-----------------------------------------------------------------------------
    #creamos la parte superior de la pagina donde estaran los titulos y mensajes
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
        # ft.Container(
        #     content = ft.Row(
        #         [
        #             ft.FilledButton("Login", height=40, width=120,on_click= lambda e : print(escogidos),),
        #             ft.FilledButton("Playlist", height=40, width=120),
        #             ft.FilledButton("Settings", height=40, width=120),
        #         ],
        #         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        #         width=400,
        #     ),
        #     margin=ft.margin.only(top=10, left=0, right=30, bottom=0)
        # )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=page.window_width,
    )

    bar_column = ft.Column([bar,
         ft.Container(content=ft.Text("| Selecciona al menos 5 generos",
                size=25, 
                weight=ft.FontWeight.BOLD, 
                text_align=ft.TextAlign.START,
                color=ft.colors.GREEN_800,
            ), margin=ft.margin.only(top=0, left=55, right=0, bottom=0),)])
    #--------------------------------------------------------------------



    #-------------------------------------------------------------------
    #creamos los container de botones

    nom_generos = [] #matriz donde estaran los nombres de todos los generos musicales
    
    for i in range(len(dt.generos)):
        nom_generos.append(dt.generos[i][1]) 


    # creacion de los botones
    botones = []
    iterador = 0
    def presionar(a,ind):
            r = ind    
            escogidos[ind] = a
            print(escogidos)




    for nombre in nom_generos:
        
        botones.append(
                ft.FilledButton(
                                text = nombre,
                                content=ft.Text(nombre,size = 20),
                                style = ft.ButtonStyle(
                                    color={                                    
                                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                                        ft.MaterialState.FOCUSED: ft.colors.YELLOW,
                                        ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                    },
                                    bgcolor= ft.colors.with_opacity(0.9, ft.colors.LIME_ACCENT_700),
                                    overlay_color=ft.colors.GREEN
                                ),width=230
                                ,height=80,
                                                                
                            ),
                       )
        
        # iterador = iterador + 1

    for i in range(50):
        botones[i].on_click = lambda e, i=i: presionar(botones[i].text,i)

    # print(escogidos)
    contain_botones = []
    for boton in botones:
        contain_botones.append(
            ft.Container(
                content=boton,                
                margin=10,
                padding=0,
                alignment=ft.alignment.center,
                width=250,
                height=90,
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
            filas.append(
                    ft.Row(controls=fila, alignment=ft.MainAxisAlignment.CENTER)                                    
            )
            fila = []
        contador = contador+1

    col = ft.Column(filas,alignment=ft.MainAxisAlignment.CENTER)

    matriz_generos = ft.Column([
                ft.Container(
                    content=col,
                ),
            ],alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            height=360,
            width=900,
            scroll=ft.ScrollMode.ALWAYS,        
    )
    boton_aceptar = ft.FilledButton(
                content=ft.Text("ACEPTAR",size = 20),
                on_click=lambda e : print("cmabiar pagina"),
                style = ft.ButtonStyle(
                                    color={                                    
                                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                                        ft.MaterialState.FOCUSED: ft.colors.YELLOW,
                                        ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                    },overlay_color=ft.colors.GREEN_ACCENT_400,
                                    bgcolor= ft.colors.with_opacity(0.9, ft.colors.LIGHT_GREEN_ACCENT_700)
                ),width=200,
                height=50,                
            )
    
    fila_boton_abajo = ft.Row([
        boton_aceptar  
    ],alignment=ft.MainAxisAlignment.END    
    )
    columna_boton_abajo = ft.Column([
        ft.Container(
            content=fila_boton_abajo,
            height=1000,
            margin=ft.margin.only(top=0, left=0, right=40, bottom=0),                            
        )
        ],alignment=ft.MainAxisAlignment.END

    )

    #------------------------------------------------------------------
    
    #---------------------------------
    #funcionalidad de los botones

    

    st = ft.Stack([imagen_fondo,imagen_verde,bar_column,columna_boton_abajo,
                ft.Row([
                ft.Container(content=matriz_generos,
                            margin=ft.margin.only(top=120, left=30, right=0, bottom=0),
                            )]
                            ,
                            #spacing=30,
                            ),
                            # columna_boton_abajo
                            ])

    return st