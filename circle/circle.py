from kivy.app import App
from kivy.lang import Builder


class CircleApp(App):

    def build(self):
        return Builder.load_file('kvs/circle.kv')


if __name__ == '__main__':
    CircleApp().run()
