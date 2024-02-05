Aplicativo de Análise de Voz para SDGame 2 - O Aplicativo de Análise de Voz para SDGame 2 é uma aplicação desenvolvida em Python que utiliza reconhecimento de voz e integração com a API da OpenAI para avaliar projetos dentro do jogo. Este aplicativo, construído com a biblioteca Kivy para interface gráfica, permite aos jogadores interagir e avaliar projetos do jogo usando apenas comandos de voz, proporcionando uma experiência única e interativa.

Funcionalidades
Reconhecimento de Voz: Capta e transcreve a fala do usuário em tempo real.
Interface Gráfica Amigável: Desenvolvido com Kivy, oferece uma experiência de usuário suave e intuitiva.
Integração com OpenAI: Analisa o discurso transcrito utilizando modelos GPT da OpenAI para gerar uma avaliação detalhada do projeto mencionado pelo usuário.
Avaliação de Projetos do SDGame 2: Avalia projetos numa escala onde 1 indica baixa demanda por recursos, 3 média e 5 alta, ajudando na tomada de decisões estratégicas dentro do jogo.
Instalação
Para utilizar o Aplicativo de Análise de Voz para SDGame 2, certifique-se de ter instalado:

Python 3.6 ou superior
Kivy
Biblioteca SpeechRecognition
Uma chave de API válida da OpenAI
Siga os passos abaixo para instalar e executar o aplicativo:
Instalar Kivy:
pip install kivy
Instalar SpeechRecognition:
pip install SpeechRecognition
Executar o Aplicativo:

Salve o script como app.py e execute-o com o comando:
python app.py

Iniciar o Aplicativo: Ao abrir, a interface gráfica será exibida com botões para interação.  
Iniciar o Reconhecimento de Voz: Clique em "Iniciar reconhecimento por voz" e fale no microfone. O aplicativo exibirá o texto transcrito.
Analisar o Discurso: Após a transcrição, clique em "Iniciar análise do projeto" para que o aplicativo analise o conteúdo usando a API da OpenAI e forneça uma avaliação baseada nos critérios do SDGame 2.

Contribuições
Contribuições para o Aplicativo de Análise de Voz para SDGame 2 são bem-vindas. Seja através de solicitações de funcionalidades, relatórios de bugs ou contribuições de código, sinta-se à vontade para ajudar a melhorar o aplicativo.
