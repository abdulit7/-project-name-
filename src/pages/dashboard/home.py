import flet as ft

def Home(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("Welcome to the Asset Management System", size=30),
            ft.Text("This is the home page of the dashboard.", size=20),
            ft.Button("Go to Users", on_click=lambda e: page.go("/user")),
            ft.Button("Go to Assets", on_click=lambda e: page.go("/asset")),
            ft.Button("Go to Categories", on_click=lambda e: page.go("/category")),
            ft.Button("Go to Departments", on_click=lambda e: page.go("/department")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )