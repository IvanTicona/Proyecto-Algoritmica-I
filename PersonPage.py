import flet as ft
from flet import theme
from database import *

def generateUserGenreImages(id):
    user_genres = getGenreNames(getUserGenres(id))
    return user_genres
    

def PersonPage(page: ft.Page):
    cola = deque()
    vector = BFS(getIndex("Daniel"))
    
    for i in range(len(vector)):
        cola.append(vector[i])

    id_user=cola.popleft()+1

    descripcion = ft.Text(getUserDescription(id_user), size = 20, weight = ft.FontWeight.BOLD, theme_style=ft.TextThemeStyle.TITLE_SMALL)
    imagen = ft.Image(src=f"./losgenericos/{getUserName(id_user)}.jpg", width=200, height=200, border_radius=20, fit= ft.ImageFit.FILL)
    informacion=ft.Text(f"{getUserName(id_user)}, {getUserAge(id_user)} años", size=40, weight=ft.FontWeight.BOLD)
    image1 =ft.Image(src=f"./YALISTASBEBE/{generateUserGenreImages(id_user)[0]}.png", width=200, height=200) #for genre in generateUserGenreImages(id_user)
    image2 =ft.Image(src=f"./YALISTASBEBE/{generateUserGenreImages(id_user)[1]}.png", width=200, height=200) #for genre in generateUserGenreImages(id_user)
    image3 =ft.Image(src=f"./YALISTASBEBE/{generateUserGenreImages(id_user)[2]}.png", width=200, height=200) #for genre in generateUserGenreImages(id_user)
    image4 =ft.Image(src=f"./YALISTASBEBE/{generateUserGenreImages(id_user)[3]}.png", width=200, height=200) #for genre in generateUserGenreImages(id_user)
    image5 =ft.Image(src=f"./YALISTASBEBE/{generateUserGenreImages(id_user)[4]}.png", width=200, height=200) #for genre in generateUserGenreImages(id_user)


    def rechazar_usuario():
        if cola:
            
            id = cola.popleft()+1

            descripcion.value=getUserDescription(id)
            imagen.src=f"./losgenericos/{getUserName(id)}.jpg"
            informacion.value=f"{getUserName(id)}, {getUserAge(id)} años"
            image1.src=f"./YALISTASBEBE/{generateUserGenreImages(id)[0]}.png"
            image2.src=f"./YALISTASBEBE/{generateUserGenreImages(id)[1]}.png"
            image3.src=f"./YALISTASBEBE/{generateUserGenreImages(id)[2]}.png"
            image4.src=f"./YALISTASBEBE/{generateUserGenreImages(id)[3]}.png"
            image5.src=f"./YALISTASBEBE/{generateUserGenreImages(id)[4]}.png"

            cola.append(id)
            page.update()

    id = cola.popleft()

    content2= ft.Container(
                content= ft.Container(
                    content=descripcion,
                    margin=ft.margin.only(0,0,120,0)
                ), 
                width = 300
                )
    
    row_image= ft.Row(
        [
            imagen
        ],
        alignment=ft.MainAxisAlignment.START   
    )

    row_user_info = ft.Row(
        [
            informacion
        ]
    )

    row_user_description= ft.Row(
        [
            content2
        ]
    )

    btn_aceptar = ft.FilledButton("Aceptar", on_click= lambda e: page.go("/match"))
    row_button_aceptar= ft.Row(
        [
            btn_aceptar
        ],
        alignment=ft.MainAxisAlignment.START   
    )
    btn_rechazar = ft.FilledButton(
        "Rechazar", 
        on_click= lambda _:rechazar_usuario()
        )
    row_button_rechazar = ft.Row(
        [
            btn_rechazar
        ],
        alignment=ft.MainAxisAlignment.START 
    )

    row_info=ft.Column(
                [
                    ft.Row(
                            [
                                ft.Container(
                                content=ft.Text(
                                "| FaveFusion",size=40, weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.START,width=page.window_width * 0.3,
                                color=ft.colors.GREEN_400),
                                margin=ft.margin.only(top=0, left=30, right=0, bottom=0)
                                ),

                                ft.Row(
                                [
                                    ft.FilledButton("Home", on_click= lambda e: page.go("/home")),
                                ],
                                alignment=ft.MainAxisAlignment.START
                                )
                            ],
                            width=page.window_width,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            [
                                row_image,
                                ft.Column(
                                    [
                                        row_user_info,
                                        ft.Row(
                                            [
                                                row_button_aceptar,
                                                row_button_rechazar
                                            ]
                                        ),
                                    ]
                                ),
                                row_user_description
                            ],
                            spacing=50
                        ), 
                ], 
                width=page.window_width
            )
    
    column1=ft.Column(
                    [
                        row_info,
                        
                        ft.Row(
                            [
                                ft.Text("Top Genres",size = 30, weight = ft.FontWeight.BOLD, theme_style=ft.TextThemeStyle.TITLE_SMALL)
                            ]

                        ),
                        ft.Row(
                            [
                                image1, image2, image3, image4, image5
                            ], 
                            wrap = True 
                        ),           
                    ],
                    width = page.window_width,
                    height = page.window_height
                )

    container_page = ft.Container(
        content=column1,
        padding=ft.padding.only(50,10,50,0),
        gradient=ft.LinearGradient(["red","black"]),
        width=page.window_width,
        height=page.window_height + 200
    )

    return container_page
