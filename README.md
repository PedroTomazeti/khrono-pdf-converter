# Khrono - Conversor de Laudos (PDF → JPG)
> Automação de conversão em `.JPG` do PDF de laudos técnico usando Python, com interface gráfica e análise de arquivo.

## 💡 Objetivo

Este projeto converte automaticamente arquivos PDF de laudos técnicos em imagens `.JPG`, ignorando a primeira página de cada documento. A interface foi desenvolvida com **CustomTkinter**.

## 🚀 Como usar

1. Coloque os arquivos `.pdf` na pasta: `C:\PDF LAUDOS`.
2. Execute o programa (`Khrono.exe` ou `python app/app.py`).
3. As imagens serão salvas em: `C:\PDF LAUDOS\imagens\NOMEDOARQUIVO`.
4. O PDF original será **excluído** após conversão.

> **Importante:** PDFs já convertidos (com pasta de destino criada) serão ignorados. Para reconverter, delete a pasta correspondente.

---

## 🧰 Requisitos

- Python 3.10+
- `pdf2image`
- `Pillow`
- `customtkinter`

## 📁 Estrutura de Pastas
📁 khrono-pdf-converter/
│
├── app/
│   └── app.py                # Interface principal
│
├── functions/
│   └── main.py               # Funções de conversão
│   └── poppler/
│
├── img/
│   └── Análise do Motor Dimensional.png  # Imagem de fundo
├── README.md
├── requirements.txt
└── .gitignore



### Instalar dependências

```bash
pip install -r requirements.txt
```

## Execute o script principal:
> python -m app.app

## Para criar o .exe:
> pyinstaller --onefile -w --name="Khrono" app/app.py

## ⚠️ Avisos
- Este projeto é uma versão genérica, sem qualquer vínculo com dados sensíveis ou proprietários. Adaptado exclusivamente para fins educacionais e de portfólio.
