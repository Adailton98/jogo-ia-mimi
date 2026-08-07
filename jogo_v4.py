from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random
import sqlite3

class JogoComBanco(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tamanho = 80
        self.inicializar_banco()
        self.recorde = self.carregar_recorde()
        self.reset_jogo()

        # Placar na Tela
        self.placar = Label(
            text="",
            font_size='18sp',
            pos=(Window.width / 2 - 100, Window.height - 80) if Window.width else (200, 500)
        )
        self.add_widget(self.placar)
        self.atualizar_texto_placar()

        # Game Loop (60 FPS)
        Clock.schedule_interval(self.atualizar, 1.0 / 60.0)

    def inicializar_banco(self):
        """Cria o banco de dados e a tabela se não existirem"""
        conn = sqlite3.connect("recorde.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS placar (id INTEGER PRIMARY KEY, pontuacao INTEGER)")
        cursor.execute("SELECT COUNT(*) FROM placar")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO placar (id, pontuacao) VALUES (1, 0)")
        conn.commit()
        conn.close()

    def carregar_recorde(self):
        """Busca o recorde salvo no SQLite"""
        conn = sqlite3.connect("recorde.db")
        cursor = conn.cursor()
        cursor.execute("SELECT pontuacao FROM placar WHERE id = 1")
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else 0

    def salvar_recorde(self, novo_recorde):
        """Atualiza o banco com a nova pontuação máxima"""
        conn = sqlite3.connect("recorde.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE placar SET pontuacao = ? WHERE id = 1", (novo_recorde,))
        conn.commit()
        conn.close()

    def reset_jogo(self):
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

        self.alvo_x += self.vel_x
        self.alvo_y += self.vel_y

        largura_tela = Window.width or 800
        altura_tela = Window.height or 600

        if self.alvo_x <= 0 or (self.alvo_x + self.tamanho) >= largura_tela:
            self.vel_x *= -1

        if self.alvo_y <= 0 or (self.alvo_y + self.tamanho) >= altura_tela:
            self.vel_y *= -1

        self.canvas.clear()
        with self.canvas:
            Color(self.cor_r, self.cor_g, self.cor_b, 1)
            Ellipse(pos=(self.alvo_x, self.alvo_y), size=(self.tamanho, self.tamanho))

    def on_touch_down(self, touch):
        if self.game_over:
            self.reset_jogo()
            self.atualizar_texto_placar()
            return

        if (self.alvo_x <= touch.x <= self.alvo_x + self.tamanho) and \
           (self.alvo_y <= touch.y <= self.alvo_y + self.tamanho):
            
            self.pontos += 10
            if self.pontos > self.recorde:
                self.recorde = self.pontos
                self.salvar_recorde(self.recorde)

            self.vel_x *= 1.1
            self.vel_y *= 1.1
            self.cor_r = random.random()
            self.cor_g = random.random()
            self.cor_b = random.random()
        else:
            self.vidas -= 1
            if self.vidas <= 0:
                self.game_over = True
                self.placar.text = f"❌ GAME OVER! Final: {self.pontos} pts.\nRecorde Salvo: {self.recorde}\n[ Toque para Recomeçar ]"
                return

        self.atualizar_texto_placar()

class AppJogoV4(App):
    def build(self):
        return JogoComBanco()

if __name__ == '__main__':
    AppJogoV4().run()
