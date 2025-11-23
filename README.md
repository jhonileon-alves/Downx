# DownX

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-None-lightgrey)]()
[![GitHub Repo](https://img.shields.io/badge/GitHub-DownX-blue?logo=github)](https://github.com/jhonileon-alves)

**DownX** é um downloader de vídeos do YouTube desenvolvido em **Python** utilizando **CustomTkinter**.  
Interface moderna em **dark mode**, download em **MP4** na melhor qualidade disponível, seleção de pasta de destino e acompanhamento do status do download em tempo real.

Este projeto foi criado com foco em **usabilidade, simplicidade e aprendizado**, ideal para uso pessoal e educacional.

---

## 🎯 Funcionalidades

- 📁 **Seleção de pasta de destino**: escolha onde salvar os vídeos  
- 🎬 **Download de vídeos do YouTube**: melhor qualidade em MP4  
- 🌑 **Interface moderna**: dark mode com CustomTkinter  
- ⚡ **Status de download**: mensagens em tempo real indicando progresso ou erros  
- ❌ **Validação de entrada**: alerta se URL ou pasta não forem informadas  

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior  
- Instalar as dependências:

```bash
pip install -r requirements.txt
🛠️ Instalação
Clone o repositório:

bash
Copy code
git clone https://github.com/jhonileon-alves/DownX.git
cd DownX
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute o aplicativo:

bash
Copy code
python main.py
🚀 Uso
Clique em Escolher pasta e selecione a pasta de destino

Insira a URL do vídeo do YouTube

Clique em Download

Acompanhe o status do download na barra inferior

Mensagens de erro serão exibidas caso a URL esteja incorreta ou nenhuma pasta tenha sido selecionada.

📂 Estrutura do projeto
bash
Copy code
DownX/
│
├─ main.py             # Código principal
├─ downx.ico           # Ícone do aplicativo
├─ requirements.txt    # Dependências do projeto
├─ README.md           # Documentação
└─ assets/             # Screenshots e GIFs de demonstração
    ├─ screenshot.png
    └─ demo.gif
💡 Dicas Extras
Criar executável Windows (.exe):

bash
Copy code
pip install pyinstaller
pyinstaller --onefile --windowed --icon=downx.ico main.py
Personalizar interface:

python
Copy code
set_appearance_mode("dark")        # dark / light / system
set_default_color_theme("blue")    # blue, green, dark-blue, etc.
🤝 Contribuição
Contribuições são bem-vindas!

Fork o repositório

Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade)

Commit suas alterações (git commit -m "Descrição da alteração")

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request no repositório original

📜 Licença
Uso pessoal e educacional. Respeite direitos autorais ao baixar conteúdos da internet.

👨‍💻 Autor
Jhoni Leon

GitHub: https://github.com/jhonileon-alves

Email: jhoni.leon.alves@gmail.com

DownX foi desenvolvido com foco em experiência do usuário, simplicidade e aprendizado em Python.
Qualquer uso comercial deve seguir as regras de direitos autorais do YouTube e demais conteúdos online.
