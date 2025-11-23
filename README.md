# DownX

**DownX** é um downloader de vídeos do YouTube desenvolvido em **Python** utilizando **CustomTkinter**.  
Oferece interface moderna em **dark mode**, permite escolher a pasta de destino, baixar vídeos em **MP4** na melhor qualidade e acompanha o status do download em tempo real.  

---

## Funcionalidades

- 📁 **Escolha de pasta:** Selecione a pasta de destino para salvar os vídeos  
- 🎬 **Download de vídeos:** Baixa vídeos do YouTube na melhor qualidade disponível  
- 🌑 **Interface moderna:** Dark mode com CustomTkinter  
- ⚡ **Status de download:** Mensagens em tempo real indicando progresso ou erros  
- ❌ **Validação de entrada:** Alerta se URL ou pasta não forem informadas  

---

## Pré-requisitos

- Python 3.10 ou superior  
- Bibliotecas necessárias:

```bash
pip install customtkinter yt-dlp
````

---

## Uso

1. Clone o repositório:

```bash
git clone https://github.com/jhonileon-alves/DownX.git
cd DownX
```

2. Execute o programa:

```bash
python main.py
```

3. Operação na interface:

* Clique em **Escolher pasta** e selecione o destino
* Insira a URL do vídeo do YouTube
* Clique em **Download** e acompanhe o status

---

## Estrutura do projeto

```
DownX/
│
├─ main.py        # Código principal
├─ downx.ico      # Ícone do projeto
├─ requirements.txt
└─ README.md
```

---

## Dicas Extras

* Para criar um **executável Windows (.exe)** sem precisar do Python:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=downx.ico main.py
```

* Personalize cores e temas no `main.py`:

```python
set_appearance_mode("dark")        # dark / light / system
set_default_color_theme("blue")    # blue, green, dark-blue, etc.
```

---

## Autor

**Jhoni Leon**

* GitHub: [https://github.com/jhonileon-alves](https://github.com/jhonileon-alves)
* Email: [jhoni.leon.alves@gmail.com](mailto:jhoni.leon.alves@gmail.com)

---

> **Nota:** Este projeto é destinado para uso pessoal e educacional.
> Respeite direitos autorais ao baixar conteúdos da internet.

```

