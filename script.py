import os
import shutil
from datetime import datetime

CATEGORIAS = {
    "Imagens": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
    "Documentos": ["pdf", "doc", "docx", "txt", "odt"],
    "Planilhas": ["xls", "xlsx", "csv"],
    "Vídeos": ["mp4", "mov", "avi", "mkv"],
    "Áudios": ["mp3", "wav", "aac", "ogg"],
    "Compactados": ["zip", "rar", "7z"],
    "Executáveis": ["exe", "msi"],
}

def registrar_log(mensagem):
    data = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    nome_arquivo = f"log_{data}.txt"

    with open(nome_arquivo, "a", encoding="utf-8") as log:
        log.write(f"[{hora}] {mensagem}\n")

def organizar_arquivos(pasta_alvo):
    for arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, arquivo)

        if os.path.isdir(caminho_completo):
            continue

        extensao = arquivo.split('.')[-1].lower()

        categoria_encontrada = None
        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                categoria_encontrada = categoria
                break

        if categoria_encontrada is None:
            categoria_encontrada = "Outros"

        pasta_destino = os.path.join(pasta_alvo, categoria_encontrada)
        os.makedirs(pasta_destino, exist_ok=True)

        try:
            destino_final = os.path.join(pasta_destino, arquivo)

            if os.path.exists(destino_final):
                nome, ext = os.path.splitext(arquivo)
                destino_final = os.path.join(pasta_destino, f"{nome}_copy{ext}")

            shutil.move(caminho_completo, destino_final)
            print(f"Movido: {arquivo} → {pasta_destino}")
            registrar_log(f"Movido: {arquivo} → {pasta_destino}")

        except PermissionError:
            print(f"⚠️ Permissão negada para mover: {arquivo}")
            registrar_log(f"Permissão negada para mover: {arquivo}")

        except FileNotFoundError:
            print(f"⚠️ Arquivo não encontrado: {arquivo}")
            registrar_log(f"Arquivo não encontrado: {arquivo}")

        except Exception as e:
            print(f"⚠️ Erro inesperado ao mover {arquivo}: {e}")
            registrar_log(f"Erro inesperado ao mover {arquivo}: {e}")

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta que deseja organizar: ")
    organizar_arquivos(pasta)
