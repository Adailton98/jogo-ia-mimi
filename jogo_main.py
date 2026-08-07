from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
import random

class JogoCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pontos = 0
        self.alvo_x = 200
        self.alvo_y = 400
        
        # Inicia o Loop do Jogo (Roda 60 vezes por segundo)
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def on_touch_down(self, touch):
        # Verifica se o toque do jogador foi próximo ao alvo
        distancia_x = abs(touch.x - self.alvo_x)
        distancia_y = abs(touch.y - self.alvo_y)

        if distancia_x < 50 and distancia_y < 50:
            self.pontos += 1
            print(f"🔥 ACERTOU! Pontuação Atual: {self.pontos}")
            # Reposiciona o alvo em um lugar aleatório da tela
            self.alvo_x = random.randint(100, 500)
            self.alvo_y = random.randint(200, 800)

    def atualizar(self, dt):
        # Desenha/Limpa a tela a cada quadro
        self.canvas.clear()
        with self.canvas:
            # Desenha o Alvo (Círculo Vermelho)
            Color(1, 0, 0, 1) # Vermelho (R, G, B, A)
            Ellipse(pos=(self.alvo_x, self.alvo_y), size=(60, 60))

class MeuJogoApp(App):
    def build(self):
        return JogoCanvas()

if __name__ == '__main__':
    MeuJogoApp().run()
