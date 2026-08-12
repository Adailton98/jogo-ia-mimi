import traceback
import sys

# Garante que qualquer erro de importação de biblioteca seja capturado
try:
    import json
    import os
    from kivy.config import Config
    Config.set('graphics', 'resizable', 'True')

    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.popup import Popup
    from kivy.graphics import Color, Rectangle, Ellipse, Triangle
    from kivy.clock import Clock
    from kivy.utils import platform

except Exception as e:
    with open("crash_log.txt", "w") as f:
        f.write(traceback.format_exc())


# Chave oficial do seu bloco de anúncios (com a barra '/')
ADMOB_REWARDED_ID = "ca-app-pub-3118010994727094/6454772833"


SAVE_FILE = "save_progresso.json"
AUTORES = "Adailton Santos e Grazzy Santos"

COLOR_BTN = (0.20, 0.30, 0.45, 0.85)
COLOR_CORRECT = (0.20, 0.65, 0.35, 1)
COLOR_WRONG = (0.80, 0.25, 0.25, 1)
COLOR_HELP = (0.85, 0.60, 0.15, 1)
COLOR_TEXT = (0.95, 0.95, 0.95, 1)

PERGUNTAS = [
    {"pergunta": "1. Próximo número: 2, 4, 8, 16, ...?", "opcoes": ["20", "24", "32", "64"], "correta": 2, "dica": "A sequência multiplica o número anterior por 2."},
    {"pergunta": "2. Se 5 gatos pegam 5 ratos em 5 min, quanto tempo 100 gatos levam p/ 100 ratos?", "opcoes": ["100 min", "5 min", "50 min", "1 min"], "correta": 1, "dica": "A proporção de gatos por rato continua sendo a mesma (1 para 1)."},
    {"pergunta": "3. Quantos meses no ano têm 28 dias?", "opcoes": ["1 mês", "2 meses", "6 meses", "Todos os 12"], "correta": 3, "dica": "Todos os meses têm pelo menos 28 dias!"},
    {"pergunta": "4. O pai de Maria tem 5 filhas: Lala, Lela, Lila, Lola. Qual o nome da 5ª?", "opcoes": ["Lula", "Maria", "Lila", "Lili"], "correta": 1, "dica": "Preste atenção no enunciado: 'O pai de...'"},
    {"pergunta": "5. Próximo termo: 1, 1, 2, 3, 5, 8, ...?", "opcoes": ["10", "11", "13", "15"], "correta": 2, "dica": "Sequência de Fibonacci: some os dois últimos números para achar o próximo."},
    {"pergunta": "6. O que fica mais úmido quanto mais seca?", "opcoes": ["Esponja", "Toalha", "Sol", "Vento"], "correta": 1, "dica": "É um objeto de banho usado para enxugar o corpo."},
    {"pergunta": "7. Se você me ultrapassar em 2º lugar numa corrida, em que lugar fica?", "opcoes": ["1º", "2º", "3º", "Último"], "correta": 1, "dica": "Você assume a posição de quem você acabou de ultrapassar."},
    {"pergunta": "8. Próximo número: 3, 6, 12, 24, ...?", "opcoes": ["30", "36", "48", "60"], "correta": 2, "dica": "Dobre o valor anterior (24 x 2)."},
    {"pergunta": "9. Tenho cidades, mas não casas; florestas, mas não árvores. O que sou?", "opcoes": ["Mapa", "Livro", "Globo", "Desenho"], "correta": 0, "dica": "Usado para navegação e geografia em papel."},
    {"pergunta": "10. Quanto é a metade de 2 mais 2?", "opcoes": ["2", "3", "4", "1"], "correta": 1, "dica": "Ordem de operações: (metade de 2) + 2 = 1 + 2."},
    {"pergunta": "11. Um tijolo pesa 1kg mais meio tijolo. Quanto pesa um tijolo?", "opcoes": ["1kg", "1.5kg", "2kg", "2.5kg"], "correta": 2, "dica": "Se 1/2 tijolo = 1kg, então 1 tijolo inteiro = 2kg."},
    {"pergunta": "12. Próximo número: 100, 95, 85, 70, ...?", "opcoes": ["60", "50", "55", "45"], "correta": 1, "dica": "A subtração aumenta a cada passo: -5, -10, -15, -20..."},
    {"pergunta": "13. O que pode passar pelo vidro sem quebrá-lo?", "opcoes": ["Som", "Luz", "Ar", "Água"], "correta": 1, "dica": "O vidro é transparente para ela."},
    {"pergunta": "14. Se A é maior que B, e B é maior que C, qual a relação entre A e C?", "opcoes": ["A < C", "A = C", "A > C", "Indeterminado"], "correta": 2, "dica": "Propriedade transitiva: Se A > B e B > C, A é o maior de todos."},
    {"pergunta": "15. Quantos números 9 existem entre 1 e 100?", "opcoes": ["10", "11", "19", "20"], "correta": 3, "dica": "Lembre de contar as dezenas (90, 91, 92...) e o 99 tem dois noves!"},
    {"pergunta": "16. Próxima letra da sequência: J, F, M, A, M, J, J, A, ...?", "opcoes": ["S", "O", "N", "D"], "correta": 0, "dica": "São as iniciais dos meses do ano (Janeiro, Fevereiro, Março... Setembro)."},
    {"pergunta": "17. Quantos lados tem um círculo?", "opcoes": ["Nenhum", "1", "2 (interno e externo)", "Infinitos"], "correta": 2, "dica": "Charada clássica: o lado de dentro e o lado de fora."},
    {"pergunta": "18. Se 3 velas queimam em 3 horas, quanto tempo queimam 6 velas juntas?", "opcoes": ["6 horas", "3 horas", "1.5 horas", "18 horas"], "correta": 1, "dica": "Todas estão queimando ao mesmo tempo."},
    {"pergunta": "19. Próximo número: 5, 10, 20, 40, ...?", "opcoes": ["50", "60", "80", "100"], "correta": 2, "dica": "Multiplique por 2."},
    {"pergunta": "20. Se ontem fosse amanhã, hoje seria sexta. Que dia é hoje?", "opcoes": ["Quarta", "Quinta", "Sábado", "Domingo"], "correta": 0, "dica": "Analise o deslocamento de dias em relação à sexta-feira."},
    {"pergunta": "21. O que pertence a você, mas os outros usam mais do que você?", "opcoes": ["Celular", "Seu nome", "Dinheiro", "Carro"], "correta": 1, "dica": "É como as pessoas chamam você."},
    {"pergunta": "22. Próximo número da sequência: 1, 4, 9, 16, 25, ...?", "opcoes": ["30", "35", "36", "49"], "correta": 2, "dica": "São os quadrados perfeitos: 1², 2², 3², 4², 5², 6²."},
    {"pergunta": "23. Quantas patas têm 3 cachorros, 2 passarinhos e 1 cobra?", "opcoes": ["16", "12", "14", "18"], "correta": 0, "dica": "(3 x 4 patas) + (2 x 2 patas) + (1 x 0 patas)."},
    {"pergunta": "24. Se um médico lhe der 3 comprimidos para tomar a cada 30 min, quanto tempo duram?", "opcoes": ["1 hora e meia", "1 hora", "30 minutos", "2 horas"], "correta": 1, "dica": "1º agora (0 min), 2º em 30 min, 3º em 60 min (1 hora total)."},
    {"pergunta": "25. Próximo número: 2, 3, 5, 7, 11, 13, ...?", "opcoes": ["15", "17", "19", "21"], "correta": 1, "dica": "Sequência de números primos."},
    {"pergunta": "26. O que é que tem chave, mas não abre nenhuma porta?", "opcoes": ["Cadeado", "Piano / Teclado", "Segredo", "Mapa"], "correta": 1, "dica": "Refere-se às teclas musicais ou de digitação."},
    {"pergunta": "27. Se dobrarmos uma folha 3 vezes ao meio, em quantas partes fica dividida?", "opcoes": ["3", "6", "8", "12"], "correta": 2, "dica": "Cada dobra dobradobra o número de partes: 2¹ = 2, 2² = 4, 2³ = 8."},
    {"pergunta": "28. Próximo número: 81, 27, 9, 3, ...?", "opcoes": ["0", "1", "2", "-3"], "correta": 1, "dica": "Divida por 3 a cada termo."},
    {"pergunta": "29. O que sobe mas nunca desce?", "opcoes": ["Fumaça", "Sua idade", "Preço", "Aviao"], "correta": 1, "dica": "Aumenta a cada ano no seu aniversário."},
    {"pergunta": "30. Se 4 máquinas fazem 4 itens em 4 min, quanto tempo 1 máquina faz 1 item?", "opcoes": ["1 min", "2 min", "4 min", "16 min"], "correta": 2, "dica": "Cada máquina leva 4 minutos para produzir o seu item individual."}
]

def salvar_jogo(indice, pontos):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump({"indice": indice, "pontos": pontos}, f)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def carregar_jogo():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"indice": 0, "pontos": 0}

class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_group = InstructionGroup()
        self.canvas.before.add(self.bg_group)
        self.bind(size=self.desenhar_paisagem, pos=self.desenhar_paisagem)

    def desenhar_paisagem(self, *args):
        self.bg_group.clear()
        w, h = self.size 
        self.bg_group.add(Color(0.08, 0.10, 0.18, 1))
        self.bg_group.add(Rectangle(pos=(0, 0), size=(w, h)))
        self.bg_group.add(Color(0.95, 0.95, 0.85, 0.9))
        self.bg_group.add(Ellipse(pos=(w * 0.75, h * 0.80), size=(w * 0.15, w * 0.15)))
        self.bg_group.add(Color(0.15, 0.18, 0.28, 1))
        self.bg_group.add(Triangle(points=[0, 0, w * 0.35, h * 0.35, w * 0.7, 0]))
        self.bg_group.add(Triangle(points=[w * 0.3, 0, w * 0.7, h * 0.40, w, 0]))
        self.bg_group.add(Color(0.10, 0.12, 0.20, 1))
        self.bg_group.add(Triangle(points=[0, 0, w * 0.5, h * 0.25, w, 0]))

class MenuScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        titulo = Label(text="DESAFIO DE LÓGICA & QI", font_size='22sp', bold=True, color=COLOR_TEXT, size_hint_y=0.35)
        layout.add_widget(titulo)
        
        btn_novo = Button(text="Novo Jogo", background_color=COLOR_BTN, color=COLOR_TEXT, size_hint_y=0.18, font_size='16sp')
        btn_novo.bind(on_release=self.novo_jogo)
        layout.add_widget(btn_novo)
        
        btn_continuar = Button(text="Continuar", background_color=COLOR_BTN, color=COLOR_TEXT, size_hint_y=0.18, font_size='16sp')
        btn_continuar.bind(on_release=self.continuar_jogo)
        layout.add_widget(btn_continuar)
        
        btn_sobre = Button(text="Sobre / Criadores", background_color=COLOR_BTN, color=COLOR_TEXT, size_hint_y=0.18, font_size='16sp')
        btn_sobre.bind(on_release=lambda x: setattr(self.manager, 'current', 'sobre'))
        layout.add_widget(btn_sobre)
        self.add_widget(layout)

    def novo_jogo(self, instance):
        salvar_jogo(0, 0)
        self.manager.get_screen('jogo').carregar_fase(0, 0)
        self.manager.current = 'jogo'

    def continuar_jogo(self, instance):
        dados = carregar_jogo()
        self.manager.get_screen('jogo').carregar_fase(dados["indice"], dados["pontos"])
        self.manager.current = 'jogo'

class SobreScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        lbl = Label(
            text=f"--- SOBRE O JOGO ---\n\nCriadores:\n[b]{AUTORES}[/b]\n\nAdMob Publisher:\n{ADMOB_PUBLISHER_ID}",
            markup=True, halign='center', font_size='15sp', color=COLOR_TEXT
        )
        layout.add_widget(lbl)
        btn_voltar = Button(text="Voltar ao Menu", background_color=COLOR_BTN, color=COLOR_TEXT, size_hint_y=0.2, font_size='16sp')
        btn_voltar.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_voltar)
        self.add_widget(layout)

class JogoScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.indice = 0
        self.pontos = 0
        self.bloqueado = False
        
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.10, spacing=10)
        btn_voltar = Button(text="< Voltar", size_hint_x=0.3, background_color=COLOR_BTN, color=COLOR_TEXT, font_size='13sp')
        btn_voltar.bind(on_release=self.voltar_menu)
        top_bar.add_widget(btn_voltar)
        
        self.lbl_info = Label(text="", size_hint_x=0.7, font_size='13sp', color=COLOR_TEXT, halign='right')
        top_bar.add_widget(self.lbl_info)
        self.layout.add_widget(top_bar)
        
        self.btn_ajuda = Button(text="💡 Pedir Dica (Anúncio)", size_hint_y=0.10, background_color=COLOR_HELP, color=COLOR_TEXT, font_size='14sp', bold=True)
        self.btn_ajuda.bind(on_release=self.solicitar_ajuda)
        self.layout.add_widget(self.btn_ajuda)
        
        self.lbl_feedback = Label(text="", size_hint_y=0.08, font_size='14sp', bold=True)
        self.layout.add_widget(self.lbl_feedback)
        
        self.lbl_pergunta = Label(text="", size_hint_y=0.28, font_size='15sp', text_size=(None, None), halign='center', color=COLOR_TEXT)
        self.lbl_pergunta.bind(size=self._atualizar_text_size)
        self.layout.add_widget(self.lbl_pergunta)
        
        self.botoes_opcoes = []
        for i in range(4):
            btn = Button(text="", size_hint_y=0.11, background_color=COLOR_BTN, color=COLOR_TEXT, font_size='14sp')
            btn.bind(on_release=self.verificar_resposta)
            self.botoes_opcoes.append(btn)
            self.layout.add_widget(btn)
            
        self.add_widget(self.layout)

    def _atualizar_text_size(self, instance, value):
        instance.text_size = (instance.width * 0.9, None)

    def voltar_menu(self, instance):
        self.manager.current = 'menu'

    def carregar_fase(self, indice, pontos):
        self.indice = indice
        self.pontos = pontos
        self.bloqueado = False
        self.lbl_feedback.text = ""
        self.btn_ajuda.text = "💡 Pedir Dica (Anúncio)"
        self.btn_ajuda.disabled = False
        
        if self.indice >= len(PERGUNTAS):
            self.finalizar_jogo()
            return
            
        q = PERGUNTAS[self.indice]
        self.lbl_info.text = f"Fase {self.indice + 1}/{len(PERGUNTAS)} | Pts: {self.pontos}"
        self.lbl_pergunta.text = q["pergunta"]
        
        for i, opt in enumerate(q["opcoes"]):
            self.botoes_opcoes[i].text = opt
            self.botoes_opcoes[i].opcao_id = i
            self.botoes_opcoes[i].background_color = COLOR_BTN

    def solicitar_ajuda(self, instance):
        if self.bloqueado:
            return
            
        # Exibição de anúncio simulado ou nativo
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        lbl_ad = Label(text=f"📺 Exibindo Anúncio AdMob...\nID: {ADMOB_PUBLISHER_ID}\nAguarde a recompensa...", halign='center', font_size='14sp')
        content.add_widget(lbl_ad)
        
        popup = Popup(title='AdMob Rewards', content=content, size_hint=(0.85, 0.4), auto_dismiss=False)
        popup.open()
        
        Clock.schedule_once(lambda dt: self.concluir_anuncio(popup), 3.0)

    def concluir_anuncio(self, popup):
        popup.dismiss()
        dica_texto = PERGUNTAS[self.indice]["dica"]
        
        content = BoxLayout(orientation='vertical', padding=15, spacing=10)
        lbl_dica = Label(text=f"DICA LIBERADA:\n\n{dica_texto}", halign='center', font_size='14sp', size_hint_y=0.7)
        btn_fechar = Button(text="OK", size_hint_y=0.3, background_color=COLOR_BTN)
        content.add_widget(lbl_dica)
        content.add_widget(btn_fechar)
        
        popup_dica = Popup(title='Sucesso', content=content, size_hint=(0.85, 0.45))
        btn_fechar.bind(on_release=popup_dica.dismiss)
        popup_dica.open()
        
        self.btn_ajuda.text = "✅ Dica Utilizada"
        self.btn_ajuda.disabled = True

    def verificar_resposta(self, instance):
        if self.bloqueado:
            return
            
        self.bloqueado = True
        correta_id = PERGUNTAS[self.indice]["correta"]
        
        if instance.opcao_id == correta_id:
            self.pontos += 1
            instance.background_color = COLOR_CORRECT
            self.lbl_feedback.text = "CORRETO!"
            self.lbl_feedback.color = COLOR_CORRECT
        else:
            instance.background_color = COLOR_WRONG
            self.botoes_opcoes[correta_id].background_color = COLOR_CORRECT
            self.lbl_feedback.text = "INCORRETO!"
            self.lbl_feedback.color = COLOR_WRONG
            
        Clock.schedule_once(self.avancar_pergunta, 1.2)

    def avancar_pergunta(self, dt):
        self.indice += 1
        salvar_jogo(self.indice, self.pontos)
        self.carregar_fase(self.indice, self.pontos)

    def finalizar_jogo(self):
        resultado_screen = self.manager.get_screen('resultado')
        resultado_screen.exibir_resultado(self.pontos, len(PERGUNTAS))
        self.manager.current = 'resultado'

class ResultadoScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.lbl_resultado = Label(text="", font_size='16sp', halign='center', color=COLOR_TEXT)
        self.layout.add_widget(self.lbl_resultado)
        
        btn_menu = Button(text="Voltar ao Menu", background_color=COLOR_BTN, color=COLOR_TEXT, size_hint_y=0.2, font_size='16sp')
        btn_menu.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        self.layout.add_widget(btn_menu)
        self.add_widget(self.layout)

    def exibir_resultado(self, pontos, total):
        taxa = pontos / total
        qi = int(70 + (taxa * 70))
        classif = "Gênio 🧠" if qi >= 130 else "Acima da Média 🚀" if qi >= 115 else "Média 💡" if qi >= 100 else "Abaixo da Média 📘"
        
        texto = f"--- RESULTADO ---\n\nAcertos: {pontos} de {total}\n\nQI Estimado: {qi}\nClassificação: {classif}\n\nAdMob Publisher:\n{ADMOB_PUBLISHER_ID}\n\nCriado por:\n[b]{AUTORES}[/b]"
        self.lbl_resultado.text = texto
        self.lbl_resultado.markup = True

class JogoLogicaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SobreScreen(name='sobre'))
        sm.add_widget(JogoScreen(name='jogo'))
        sm.add_widget(ResultadoScreen(name='resultado'))
        return sm

if __name__ == "__main__":
    JogoLogicaApp().run()
