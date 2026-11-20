__version__ = "1.0.0"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class LuckyGems(App):
    def build(self):
        Window.clearcolor = (0.08, 0.02, 0.15, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="[b]LUCKY GEMS[/b]",
            markup=True,
            font_size=32
        )

        balance = Label(
            text="Demo Coins: 1000",
            font_size=22
        )

        play = Button(
            text="START PLAYING",
            font_size=22
        )

        layout.add_widget(title)
        layout.add_widget(balance)
        layout.add_widget(play)

        return layout

if __name__ == "__main__":
    LuckyGems().run()
