import threading
import speech_recognition as sr
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import openai

class SpeechApp(App):
    def build(self):
        self.recognizer = sr.Recognizer()
        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.label = Label(
            text="Pronto para reconhecer voz",
            size_hint=(1, None),
            height=100,  # Altura do Label
            color=(1, 1, 1, 1),  # Cor do texto: branco
            halign="center",  # Alinhamento horizontal do texto
            valign="middle"  # Alinhamento vertical do texto
        )
        self.label.bind(size=self.label.setter('text_size'))  # Atualizar o tamanho do texto
        self.update_label_background(self.label)
        
        self.transcription_label = Label(text="")

        self.start_button = Button(text="Iniciar reconhecimento por voz", on_press=self.start_speech_recognition)
        self.analyze_button = Button(text="Iniciar análise do projeto", on_press=self.analyze_project, disabled=True)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.transcription_label)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.analyze_button)

        return self.layout

    def update_label_background(self, label):
        with label.canvas.before:
            Color(0, 0, 0, 1)  # Cor do fundo: preto para a borda
            self.rect_border = Rectangle(size=(label.width + 4, label.height + 4), pos=(label.x - 2, label.y - 2))
            Color(0,0, 0, 1)  # Cor do fundo: verde
            self.rect = Rectangle(size=label.size, pos=label.pos)
        label.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
        self.rect_border.size = (instance.width + 4, instance.height + 4)
        self.rect_border.pos = (instance.x - 2, instance.y - 2)

    def start_speech_recognition(self, instance):
        self.start_button.disabled = True
        self.analyze_button.disabled = True
        self.transcription_label.text = "Falando..."
        threading.Thread(target=self.recognize_speech).start()

    def recognize_speech(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio, language="pt-BR")
                self.transcription_label.text = "Você disse: " + text
                self.voice_prompt = text
                self.analyze_button.disabled = False
            except sr.UnknownValueError:
                self.transcription_label.text = "Não entendi o áudio"
            except sr.RequestError as e:
                self.transcription_label.text = "Erro de serviço: {0}".format(e)
            finally:
                # Reabilitar o botão de reconhecimento de voz
                self.start_button.disabled = False

    def analyze_project(self, instance):
        if hasattr(self, 'voice_prompt'):
            prompt = (
                "Considerando que um projeto do terceiro setor custe 1, 3 ou 5 de recursos onde 1 é pouco, 3 é médio e 5 é muito,onde os recursos são dinheiro, pessoas e infraestrutura, me diga quanto de cada recurso será necessário para o seguinte projeto, De uma resposta direta nesse template: 'Dinheiro: X; Infraestrutura: Y; Pessoas: Z; pontuando apenas os 3 tipos de recursos e a numeração para cada um deles: : "
                f"{self.voice_prompt}"
            )
            response = self.ask_openai_chat(prompt)
            self.label.text = "O necessário para o projeto de acordo com a IA: " + response
            self.voice_prompt = ""  # Limpar o prompt de voz para a próxima entrada
        else:
            self.label.text = "Nenhum prompt de voz detectado."

    def ask_openai_chat(self, prompt):
        try:
            openai.api_key = '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'
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    SpeechApp().run()
