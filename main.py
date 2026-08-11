import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock

class JogoWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = 300
        self.pos_y = 500
        self.alvo_x = 300
        self.alvo_y = 500
        self.pontos = 0
        self.raio = 50
        
        # Placar na tela
        self.label = Label(
            text=f"Pontos: {self.pontos}",
            pos=(100, 100),
            font_size='24sp',
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.label)
        
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def on_touch_down(self, touch):
        # Calcula a distância entre o toque e o centro da bolinha
        centro_x = self.pos_x + self.raio
        centro_y = self.pos_y + self.raio
        distancia = math.hypot(touch.x - centro_x, touch.y - centro_y)
        
        # Se tocar dentro da bolinha, ganha ponto
        if distancia <= self.raio:
            self.pontos += 1
            self.label.text = f"Pontos: {self.pontos}"
            # Move a bolinha para uma nova posição
            self.pos_x = (self.pos_x + 150) % max(int(self.width - 100), 100)
            self.pos_y = (self.pos_y + 200) % max(int(self.height - 100), 100)

    def atualizar(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos=(self.pos_x, self.pos_y), size=(self.raio * 2, self.raio * 2))

class JogoApp(App):
    def build(self):
        return JogoWidget()

if __name__ == '__main__':
    JogoApp().run()
# Forçando build AdMob
