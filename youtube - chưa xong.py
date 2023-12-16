import flet as ft
import moviepy as mv
from pytube import YouTube

# https://www.youtube.com/watch?v=hPYdzegfkyw
# chưa xong vì chưa bị lỗi


def main(page: ft.Page):
    page.appbar= ft.AppBar(
        title= ft.Text('Trình tải Video từ youtube'),
        center_title= True
    )
    
    def textChanged(e):
        try:
            video_details = YouTube(e.control.value)
            button.text= 'Download - ' + video_details.title
            image.src = video_details.thumbnail_url
            image.update()
            button.update()
            print(video_details.title)

        except:
            button.text = 'Tải nhanh cmm lên!!'
            image.src = r'https://img.freepik.com/premium-vector/free-vector-youtube-icon-logo-social-media-logo_901408-454.jpg?w=2000'
            image.update()
            button.update()
            print('Cái này không phải link')

    txt = ft.TextField(hint_text="Link, svp!", on_change=textChanged)
    image = ft.Image(src= r'https://img.freepik.com/premium-vector/free-vector-youtube-icon-logo-social-media-logo_901408-454.jpg?w=2000',
                     width=140, fit = ft.ImageFit.COVER)
    button = ft.ElevatedButton('Tải nhanh cmm lên!!')
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        image,
        ft.Container(height=7),
        txt,
        button
        )


ft.app(target=main)
