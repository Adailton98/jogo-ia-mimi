from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
import sqlite3

class JogoWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = 200
        self.pos_y = 400
        
        # Placar na tela
        self.label = Label(text="Jogo IA Mimi - Rodando Nativo!", pos=(10, 10), font_size='20sp')
        self.add_widget(self.label)
        
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def atualizar(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 1) # Círculo Verde
            Ellipse(pos=(self.pos_x, self.pos_y), size=(80, 80))

class JogoApp(App):
    def build(self):
        return JogoWidget()

if __name__ == '__main__':
    JogoApp().run()
