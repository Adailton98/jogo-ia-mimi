import traceback
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock

class JogoWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = 200
        self.pos_y = 400
        self.vel_x = 5
        self.vel_y = 5
        
        self.label = Label(
            text="Jogo IA Mimi",
            pos=(100, 100),
            font_size='20sp'
        )
        self.add_widget(self.label)
        
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def atualizar(self, dt):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        if self.pos_x <= 0 or self.pos_x >= max(self.width - 80, 100):
            self.vel_x *= -1
        if self.pos_y <= 0 or self.pos_y >= max(self.height - 80, 100):
            self.vel_y *= -1

        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos=(self.pos_x, self.pos_y), size=(80, 80))

class JogoApp(App):
    def build(self):
        try:
            return JogoWidget()
        except Exception as e:
            # Se der erro, mostra o erro na tela em vez de fechar
            erro_str = traceback.format_exc()
            lbl = Label(text=f"Erro ao iniciar:\n{erro_str}", font_size='12sp')
            return lbl

if __name__ == '__main__':
    JogoApp().run()
