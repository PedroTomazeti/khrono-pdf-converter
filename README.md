# 🕒 Khrono - Conversor de Laudos Técnicos (PDF → JPG)

> Conversão automatizada de laudos técnicos em `.PDF` para imagens `.JPG`, com interface gráfica interativa e tratamento inteligente de arquivos.

---

## 💡 Objetivo

O **Khrono** é uma aplicação desenvolvida em **Python** com **CustomTkinter**, voltada para a automação da conversão de laudos técnicos em PDF para imagens `.JPG`.

✔️ Ignora automaticamente a primeira página do PDF.  
✔️ Detecta e evita conversões duplicadas.  
✔️ Interface gráfica amigável e responsiva.

---

## 📂 Como Usar

1. Coloque os arquivos `.pdf` na pasta:  
   `C:\PDF LAUDOS`

2. Execute o programa:  
   - Via terminal: `python app/app.py`  
   - Ou através do executável: `Khrono.exe`

3. As imagens `.jpg` serão salvas em:  
   `C:\PDF LAUDOS\imagens\NOMEDOARQUIVO`

4. O PDF original será **excluído automaticamente** após a conversão.

> ⚠️ PDFs que já possuem pastas de imagens geradas serão ignorados. Para reconverter, exclua a pasta correspondente em `imagens/`.

---

## 🧰 Requisitos

- Python 3.10+
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases) instalado e configurado no PATH
- Bibliotecas Python:
  - `pdf2image`
  - `Pillow`
  - `customtkinter`

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

## 🧪 Execução Local

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   # Ative:
   # Linux/macOS:
   source env/bin/activate
   # Windows:
   .\env\Scripts\activate
