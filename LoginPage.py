import flet as ft
from flet import Page as page


def LoginPage(page: ft.Page):

    title =  ft.Text("Sign Up",width=300,size=35,text_align="center",weight="w900")
    nombre = ft.TextField(width=300,height=60,hint_text="Username",border="underline",color="black",prefix_icon = ft.icons.PERSON)
    email = ft.TextField(width=300,height=60,hint_text="E-mail",border="underline",color="black",prefix_icon = ft.icons.EMAIL )
    password = ft.TextField(width=300,height=60,hint_text="Password",border="underline",color="black",prefix_icon = ft.icons.LOCK,password= True )
    age = ft.Dropdown(width=300,height=60,hint_text="Age",options=[ft.dropdown.Option("18"),ft.dropdown.Option("19"),ft.dropdown.Option("20"),ft.dropdown.Option("21"),ft.dropdown.Option("22"),ft.dropdown.Option("23"),],prefix_icon = ft.icons.CALENDAR_VIEW_DAY_ROUNDED)
    gender = ft.Dropdown(width=300,height=60,hint_text="Gender",options=[ft.dropdown.Option("Male"),ft.dropdown.Option("Female"),ft.dropdown.Option("Other"),],prefix_icon = ft.icons.PERSON_2_OUTLINED)
    checkTerms = ft.Checkbox(label="I accept the terms and conditions",check_color = "black")


    data_user = {
        "name": "",
        "email": "",
        "password": "",
        "age": "",
        "gender": ""
    }

    def button_clicked(e):
            data_user["name"] = nombre.value
            data_user["email"] = email.value
            data_user['password'] = password.value
            data_user['age'] = age.value
            data_user['gender'] = gender.value
            if not checkTerms.value:
                print("You have accepted the terms and conditions")
                return
            
            print(data_user)
            # Resetear los campos
            nombre.value = ""
            email.value = ""
            password.value = ""
            age.value = ""
            gender.value = ""
            page.update()

    page.title = "Login"
    loginPage = ft.Stack(
            [
                ft.Image(
                  src="./imagenes/Login.jpg",
                  width=page.window_width,
                  height=page.window_height,
                  fit=ft.ImageFit.COVER
                ),
                ft.Container(
                  content=ft.Column(
                    [
                      title,
                      nombre,
                      age,
                      gender,
                      email,
                      password,
                      ft.ElevatedButton(text="Submit", on_click= button_clicked),
                      checkTerms
                    ]
                  ),
                  bgcolor=ft.colors.GREEN_500,
                  width=300,
                  height=530,
                  margin=ft.margin.only(top=10, left=50, right=0, bottom=0),
                  border_radius=20,
                  padding=ft.padding.all(20),
                )
            ]
        )
    return [loginPage, button_clicked]
    # page.add(loginPage)

ft.app(LoginPage)