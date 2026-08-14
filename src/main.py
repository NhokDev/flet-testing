import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Flet Testing"

    page.add(
        ft.Text(
            "Hola Flet! 👋",
            size=32,
        )
    )


ft.run(main)
