from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

class JogoComReset(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tamanho = 80
        self.recorde = 0
        self.reset_jogo()

        # Placar na Tela
        self.placar = Label(
            text="",
            font_size='18sp',
            pos=(Window.width / 2 - 100, Window.height - 80) if Window.width else (200, 500)
        )
        self.add_widget(self.placar)
        self.atualizar_texto_placar()

        # Game Loop
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def reset_jogo(self):
        """Reinicia os parâmetros do jogo para o estado inicial"""
        self.pontos = 0
        self.vidas = 5
        self.alvo_x = 200
        self.alvo_y = 300
        self.vel_x = 5
        self.vel_y = 7
        self.cor_r = 0.2
        self.cor_g = 0.8
        self.cor_b = 0.2
        self.game_over = False

    def atualizar_texto_placar(self):
        self.placar.text = f"Pontos: {self.pontos} | Vidas: {self.vidas} | Recorde: {self.recorde}"

    def atualizar(self, dt):
        if self.game_over:
            return

        # Movimentação
        self.alvo_x += self.vel_x
        self.alvo_y += self.vel_y

        largura_tela = Window.width or 800
        altura_tela = Window.height or 600

        # Colisão com as bordas
        if self.alvo_x <= 0 or (self.alvo_x + self.tamanho) >= largura_tela:
            self.vel_x *= -1

        if self.alvo_y <= 0 or (self.alvo_y + self.tamanho) >= altura_tela:
            self.vel_y *= -1

        # Renderização
        self.canvas.clear()
        with self.canvas:
            Color(self.cor_r, self.cor_g, self.cor_b, 1)
            Ellipse(pos=(self.alvo_x, self.alvo_y), size=(self.tamanho, self.tamanho))

    def on_touch_down(self, touch):
        # Se estiver em Game Over, qualquer toque reinicia a partida!
        if self.game_over:
            self.reset_jogo()
            self.atualizar_texto_placar()
            return

        # Checa colisão do toque com a esfera
        if (self.alvo_x <= touch.x <= self.alvo_x + self.tamanho) and \
           (self.alvo_y <= touch.y <= self.alvo_y + self.tamanho):
            
            self.pontos += 10
            if self.pontos > self.recorde:
                self.recorde = self.pontos

            # Aumenta a velocidade
            self.vel_x *= 1.1
            self.vel_y *= 1.1
            
            # Gera cor aleatória
            self.cor_r = random.random()
            self.cor_g = random.random()
            self.cor_b = random.random()
        else:
            self.vidas -= 1
            if self.vidas <= 0:
                self.game_over = True
                self.placar.text = f"❌ GAME OVER! Final: {self.pontos} pts.\n[ Toque na tela para Recomeçar ]"
                return

        self.atualizar_texto_placar()

class AppJogoV3(App):
    def build(self):
        return JogoComReset()

if __name__ == '__main__':
    AppJogoV3().run()

