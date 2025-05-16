# Khrono - Conversor de Laudos (PDF → JPG)

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

### Instalar dependências

```bash
pip install -r requirements.txt
