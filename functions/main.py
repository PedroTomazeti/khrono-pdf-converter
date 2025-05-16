import os
from pathlib import Path
from pdf2image import convert_from_path
import sys

def obter_caminho_poppler():
    pasta_base = Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else Path(__file__).parent
    return str(pasta_base / "poppler" / "bin")

def criar_readme(pasta_pdf):
    readme_path = pasta_pdf / "README.txt"
    if readme_path.exists():
        return  # Não sobrescreve se já existir

    conteudo = """
================= CONVERSOR DE LAUDOS PDF → JPG =================

1️⃣  COMO USAR:
--------------------------------------------------------------
1. Coloque todos os arquivos .PDF que deseja converter dentro da pasta:
   C:\\PDF LAUDOS

2. Execute o programa (Khrono.exe).

3. As imagens serão geradas dentro da subpasta:
   C:\\PDF LAUDOS\\imagens\\NOMEDOPDF

   A primeira página do PDF será ignorada.

4. Após a conversão, o arquivo PDF original será excluído automaticamente.

--------------------------------------------------------------

2️⃣  IMPORTANTE:
--------------------------------------------------------------
- Para converter novamente um arquivo, apague a pasta correspondente
  dentro de C:\\PDF LAUDOS\\imagens e coloque o PDF novamente em
  C:\\PDF LAUDOS.

- PDFs já processados não serão convertidos novamente a menos que
  suas pastas sejam apagadas.

--------------------------------------------------------------

3️⃣  ATALHO:
--------------------------------------------------------------
Você pode criar um atalho do executável na área de trabalho:
→ Clique com o botão direito sobre ele
→ "Enviar para" → "Área de trabalho (criar atalho)"

==============================================================
"""
    readme_path.write_text(conteudo.strip(), encoding="utf-8")

def converter_pdfs_em_pasta(log_queue, messagebox, pasta_pdf, caminho_poppler=None):
    pasta_pdf = Path(pasta_pdf).resolve()

    if not pasta_pdf.exists():
        print(f"Pasta '{pasta_pdf}' não encontrada. Criando agora...")
        log_queue.put(f"Pasta '{pasta_pdf}' não encontrada. Criando agora...")
        messagebox.showerror("Erro", f"Pasta '{pasta_pdf}' não encontrada. Criando agora...")
        pasta_pdf.mkdir(parents=True, exist_ok=True)
        criar_readme(pasta_pdf)
        print("\nA pasta 'PDF LAUDOS' foi criada com sucesso.")
        log_queue.put("\nA pasta 'PDF LAUDOS' foi criada com sucesso.")
        print("👉 Coloque seus arquivos PDF dentro dessa pasta e execute o programa novamente.")
        log_queue.put("👉 Coloque seus arquivos PDF dentro dessa pasta e execute o programa novamente.")
        return

    criar_readme(pasta_pdf)

    pasta_imagem = pasta_pdf / "imagens"
    pasta_imagem.mkdir(exist_ok=True)

    arquivos_pdf = list(pasta_pdf.glob("*.pdf"))
    if not arquivos_pdf:
        print("Nenhum arquivo PDF encontrado em C:/PDF LAUDOS.")
        log_queue.put("\nNenhum arquivo PDF encontrado em C:/PDF LAUDOS.")
        messagebox.showinfo("Informação", "Nenhum arquivo PDF encontrado em C:/PDF LAUDOS.")
        return

    for pdf in arquivos_pdf:
        nome_base = pdf.stem
        pasta_destino = pasta_imagem / nome_base

        if pasta_destino.exists():
            print(f"Pasta '{pasta_destino}' já existe. Pulando {pdf.name}.")
            log_queue.put(f"\nPasta '{pasta_destino}' já existe. Pulando {pdf.name}.")
            # Exclui o PDF original após sucesso
            pdf.unlink()
            print(f"📁 PDF '{pdf.name}' excluído.")
            log_queue.put(f"📁 PDF '{pdf.name}' excluído.")
            continue

        os.makedirs(pasta_destino, exist_ok=True)
        print(f"\nConvertendo (ignorando a primeira página): {pdf.name}")
        log_queue.put(f"\nConvertendo (ignorando a primeira página): {pdf.name}")

        try:
            imagens = convert_from_path(str(pdf), poppler_path=caminho_poppler)
            imagens_sem_primeira = imagens[1:]

            for i, imagem in enumerate(imagens_sem_primeira, start=2):
                nome_imagem = f"LAUDO TÉCNICO FINAL_{i:02d}.jpg"
                caminho_imagem = pasta_destino / nome_imagem
                imagem.save(caminho_imagem, "JPEG")
                print(f"  Página {i} salva: {nome_imagem}")
                log_queue.put(f"  Página {i} salva: {nome_imagem}")

            # Exclui o PDF original após sucesso
            pdf.unlink()
            print(f"📁 PDF '{pdf.name}' excluído após a conversão.")
            log_queue.put(f"📁 PDF '{pdf.name}' excluído após a conversão.")

        except Exception as erro:
            print(f"❌ Erro ao converter {pdf.name}: {erro}")
            log_queue.put(f"❌ Erro ao converter {pdf.name}: {erro}")

    print("\n✅ Conversão concluída para todos os PDFs novos.")
    log_queue.put("\n✅ Conversão concluída para todos os PDFs novos.")

def iniciar_conversao(log_queue, messagebox):
    try:
        converter_pdfs_em_pasta(
            log_queue,
            messagebox,
            pasta_pdf="C:/PDF LAUDOS",
            caminho_poppler=obter_caminho_poppler()
        )
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
