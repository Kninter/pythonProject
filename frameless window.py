# https://www.youtube.com/watch?v=6sql8igT090
# Flet Tutorial - Frameless Window
# Gần hoàn thiện, vướng 1 chút chỗ nút phóng to và nút ẩn

from flet import *
import flet as ft



def main(page: ft.Page):
    page.window_max_height = 520
    page.window_max_width = 400
    page.window_frameless = True
    page.spacing = 0
    page.padding = 0

    # xác định chiều rộng màn hình
    widthscr = page.window_width

    page.add(
        ResponsiveRow([
            WindowDragArea(
                Container(
                    width=widthscr,
                    bgcolor='blue',
                    padding=15,
                    content=Row([
                        Text('Your home', size=25, color='white'),
                    # Đoạn dưới này là để thêm các nút bị xóa do frameless
                        Container(
                            content=Row([
                                IconButton(icons.CHECK_BOX_OUTLINE_BLANK,
                                           icon_color='white',
                                           on_click=lambda e: page.window_maximized()),
                                IconButton(icons.CLOSE,
                                           icon_color='white',
                                           on_click=lambda  e: page.window_close())
                            ])
                                  )
                    ], alignment= "spaceBetween")
                )
            )
        ])
    )

ft.app(target=main)