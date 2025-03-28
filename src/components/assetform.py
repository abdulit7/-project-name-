import flet as ft

class AssetFormPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.asset_name = ft.TextField(label="Asset Name")
        self.asset_description = ft.TextField(label="Asset Description")
        self.asset_value = ft.TextField(label="Asset Value", keyboard_type=ft.KeyboardType.NUMBER)
        self.submit_button = ft.ElevatedButton(text="Submit", on_click=self.submit)

    def build(self):
        return ft.Column(
            controls=[
                self.asset_name,
                self.asset_description,
                self.asset_value,
                self.submit_button
            ]
        )

    def submit(self, e):
        # Logic to handle asset submission
        asset_data = {
            "name": self.asset_name.value,
            "description": self.asset_description.value,
            "value": self.asset_value.value
        }
        print("Asset submitted:", asset_data)
        # Clear the fields after submission
        self.asset_name.value = ""
        self.asset_description.value = ""
        self.asset_value.value = ""
        self.page.update()