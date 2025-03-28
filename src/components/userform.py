import flet as ft

class UserForm(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.username = ft.TextField(label="Username")
        self.email = ft.TextField(label="Email")
        self.password = ft.TextField(label="Password", password=True)
        self.submit_button = ft.ElevatedButton(text="Submit", on_click=self.submit)

    def build(self):
        return ft.Column(controls=[
            self.username,
            self.email,
            self.password,
            self.submit_button
        ])

    def submit(self, e):
        # Handle form submission logic here
        username = self.username.value
        email = self.email.value
        password = self.password.value
        print(f"Submitted: {username}, {email}, {password}")
        # You can add further processing like validation or sending data to a server