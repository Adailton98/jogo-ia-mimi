from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

class JogoAvancado(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pontos = 0
        self.vidas = 5
        
        # Posição e Velocidade do Alvo
        self.alvo_x = 200
        self.alvo_y = 300
        self.vel_x = 6
        self.vel_y = 8
        self.tamanho = 80
        
        # Cor inicial da bola (RGB)
        self.cor_r = 1.0
        self.cor_g = 0.2
        self.cor_b = 0.2

        # Label de Placar na Tela
        self.placar = Label(
            text=f"Pontos: {self.pontos} | Vidas: {self.vidas}",
            font_size='20sp',
            pos=(Window.width / 2 - 100, Window.height - 80) if Window.width else (200, 500)
        )
        self.add_widget(self.placar)

        # Game Loop (60 FPS)
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def atualizar(self, dt):
        if self.vidas <= 0:
            return # Fim de jogo

        self.alvo_x += self.vel_x
        self.alvo_y += self.vel_y

        largura_tela = Window.width or 800
        altura_tela = Window.height or 600

        # Rebate nas paredes
        if self.alvo_x <= 0 or (self.alvo_x + self.tamanho) >= largura_tela:
            self.vel_x *= -1

        if self.alvo_y <= 0 or (self.alvo_y + self.tamanho) >= altura_tela:
            self.vel_y *= -1

        # Atualiza a renderização
        self.canvas.clear()
        with self.canvas:
            Color(self.cor_r, self.cor_g, self.cor_b, 1)
            Ellipse(pos=(self.alvo_x, self.alvo_y), size=(self.tamanho, self.tamanho))

    def on_touch_down(self, touch):
        if self.vidas <= 0:
            return

        # Checa colisão com o toque
        if (self.alvo_x <= touch.x <= self.alvo_x + self.tamanho) and \
           (self.alvo_y <= touch.y <= self.alvo_y + self.tamanho):
            
            self.pontos += 10
            # Aumenta a velocidade
            self.vel_x *= 1.1
            self.vel_y *= 1.1
            # Gera cor aleatória para a esfera a cada acerto!
            self.cor_r = random.random()
            self.cor_g = random.random()
            self.cor_b = random.random()
        else:
            # Se tocou fora da bola, perde vida!
            self.vidas -= 1
            if self.vidas <= 0:
                self.placar.text = f"❌ GAME OVER! Pontos Finais: {self.pontos}"
                return

        self.placar.text = f"Pontos: {self.pontos} | Vidas: {self.vidas}"

class AppJogoV2(App):
    def build(self):
        return JogoAvancado()

if __name__ == '__main__':
    AppJogoV2().run()
