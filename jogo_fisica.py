from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
import random

class JogoComFisica(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pontos = 0
        
        # Posição Inicial do Alvo
        self.alvo_x = 200
        self.alvo_y = 300
        
        # Vetor de Velocidade (Pixels por frame)
        self.vel_x = 5
        self.vel_y = 7
        
        # Tamanho do Alvo
        self.tamanho = 60
        
        # Loop do Jogo - Roda 60 vezes por segundo
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def atualizar(self, dt):
        # 1. Atualiza a Posição baseada na Velocidade
        self.alvo_x += self.vel_x
        self.alvo_y += self.vel_y

        # 2. Física de Colisão com as Bordas (Rebate)
        largura_tela = Window.width or 800
        altura_tela = Window.height or 600

        if self.alvo_x <= 0 or (self.alvo_x + self.tamanho) >= largura_tela:
            self.vel_x *= -1  # Inverte a direção horizontal

        if self.alvo_y <= 0 or (self.alvo_y + self.tamanho) >= altura_tela:
            self.vel_y *= -1  # Inverte a direção vertical

        # 3. Renderiza a Tela
        self.canvas.clear()
        with self.canvas:
            # Esfera Vermelha em Movimento
            Color(1, 0.2, 0.2, 1)
            Ellipse(pos=(self.alvo_x, self.alvo_y), size=(self.tamanho, self.tamanho))

    def on_touch_down(self, touch):
        # Detecção de Clique/Toque na Esfera em Movimento
        if (self.alvo_x <= touch.x <= self.alvo_x + self.tamanho) and \
           (self.alvo_y <= touch.y <= self.alvo_y + self.tamanho):
            self.pontos += 1
            # Aumenta a velocidade a cada acerto para aumentar a dificuldade!
            self.vel_x *= 1.2
            self.vel_y *= 1.2
            print(f"🎯 ACERTOU EM MOVIMENTO! Pontuação: {self.pontos} | Nova Vel: ({self.vel_x:.1f}, {self.vel_y:.1f})")

class AppJogoFisica(App):
    def build(self):
        return JogoComFisica()

if __name__ == '__main__':
    AppJogoFisica().run()
