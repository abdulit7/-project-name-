import flet as ft

class AssetDialog(ft.AlertDialog):
    def __init__(self, title, content, on_confirm=None, on_cancel=None):
        super().__init__(
            title=title,
            content=content,
            actions=[
                ft.TextButton("Cancel", on_click=on_cancel),
                ft.TextButton("Confirm", on_click=on_confirm),
            ],
        )