# https://www.youtube.com/watch?v=ZNuHDvt3Oxc
# Adding Navigation To Your Python App (Flet Tutorial)
# # flet run --android Navigation.py
# flet publish Navigation.py
# pip freeze > requirements.txt

import flet
from flet import View, Page, AppBar, ElevatedButton, Text, AppView
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: Page) -> None:
    page.title = "My store"

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route= '/',
                controls= [
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Go to store', on_click=lambda _: page.go('/store'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        # Store
        if page.route == '/store':
            page.views.append(
                View(
                    route='/store',
                    controls=[
                        AppBar(title=Text('Store'), bgcolor='purple'),
                        Text(value='Store', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change # Phải có dòng này thì mới lên hình
    page.on_view_pop = view_pop # Dòng này là để bấm vào mũi tên back
    page.go(page.route)

if __name__ == "__main__":
    # flet.app(target=main)
    flet.app(target=main, view= flet.AppView.WEB_BROWSER) # Với dòng này thì khi bấm Run, máy tự nhảy sang web luôn