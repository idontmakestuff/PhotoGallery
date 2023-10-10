from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoGalleryApp(App):
    pass
class DisplayScreen(Screen):
    def display_image(self):
        return images[index]
    def advance(self):
        global index, image
        if index < len(images):
            index+=1
        else:
            index=0
images = ["Fiery_Blowhog.jpg","Red_Bulborb.jpg"]
index=0

PhotoGalleryApp().run()