import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

#print(caminho)

lista_arquivos = os.listdir(caminho)
#print(lista_arquivos)
locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Planilhas": [".xlsx", ".csv"],
    "Pdfs": [".pdf"],
    "Torrents": [".torrent"],
    "Compactados": [".rar", ".zip"],
    "Documentos": [".doc", ".docx"],   
}

for arquivo in lista_arquivos:
    # . arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")