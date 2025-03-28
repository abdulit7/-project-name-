class AssetPagee(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column([
            ft.Text("Asset Management", size=30, weight="bold"),
            # Add more controls and layout for asset management here
        ])