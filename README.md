# DownX

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-None-lightgrey)]()
[![GitHub Repo](https://img.shields.io/badge/GitHub-DownX-blue?logo=github)](https://github.com/jhonileon-alves)

**DownX** é um downloader de vídeos do YouTube desenvolvido em **Python** com **CustomTkinter**.  
Oferece interface moderna em **dark mode**, download em **MP4** na melhor qualidade, seleção de pasta de destino e acompanhamento do status de download em tempo real.

Este projeto foi criado com foco em **usabilidade, simplicidade e aprendizado**, ideal para uso pessoal e educacional.

---

## Funcionalidades

- 📁 **Seleção de pasta de destino**: escolha onde salvar os vídeos  
- 🎬 **Download de vídeos do YouTube**: melhor qualidade em MP4  
- 🌑 **Interface moderna**: dark mode com CustomTkinter  
- ⚡ **Status de download**: mensagens em tempo real indicando progresso ou erros  
- ❌ **Validação de entrada**: alerta se URL ou pasta não forem informadas  

---

## Demonstração

**Tela principal do aplicativo:**

<img width="805" height="561" alt="Image" src="https://github.com/user-attachments/assets/ad49c1d3-0fe4-4114-9bb3-f285fc3a9af4" />
> Exemplo da interface principal mostrando seleção de pasta, entrada de URL e botões de download.

---

## Pré-requisitos

- Python 3.10 ou superior  
- Bibliotecas necessárias, listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
````

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/jhonileon-alves/DownX.git
cd DownX
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o aplicativo:

```bash
python main.py
```

---

## Uso

1. Clique em **Escolher pasta** e selecione o destino dos vídeos
2. Insira a URL do vídeo do YouTube
3. Clique em **Download**
4. Acompanhe o status do download na barra inferior

Mensagens de erro serão exibidas caso a URL esteja incorreta ou nenhuma pasta tenha sido selecionada.

---

## Estrutura do projeto

```
DownX/
│
├─ main.py             # Código principal
├─ downx.ico           # Ícone do aplicativo
├─ requirements.txt    # Dependências do projeto
├─ README.md           # Documentação
└─ assets/             # Screenshots do app
    └─ screenshot.png
```

---

## Dicas Extras

* Criar **executável Windows (.exe)**:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=downx.ico main.py
```

* Personalizar interface:

```python
set_appearance_mode("dark")        # dark / light / system
set_default_color_theme("blue")    # blue, green, dark-blue, etc.
```

* Barra de status exibe mensagens em tempo real, permitindo acompanhar o progresso do download.

---

## Contribuição

Contribuições são bem-vindas!

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m "Descrição da alteração"`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request no repositório original

---

## Licença

Uso pessoal e educacional. Respeite direitos autorais ao baixar conteúdos da internet.

---

## Autor

**Jhoni Leon**

* GitHub: [https://github.com/jhonileon-alves](https://github.com/jhonileon-alves)
* Email: [jhoni.leon.alves@gmail.com](mailto:jhoni.leon.alves@gmail.com)

> DownX foi desenvolvido com foco em **experiência do usuário, simplicidade e aprendizado em Python**.
> Qualquer uso comercial deve seguir as regras de direitos autorais do YouTube e demais conteúdos online.

```
