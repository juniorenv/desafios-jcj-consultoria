import os
import shutil
from pathlib import Path
from cores import Cores
from criador_arquivos import criar_arquivos_teste

def organizar_arquivos(caminho_pasta):
    categorias = {
        'Audios': ['.ogg', '.wav', '.flac', '.aac', '.mp3', '.m4a'],
        'Codigos': ['.json', '.c', '.xml', '.py', '.php', '.cpp', '.js', '.html', '.java', '.css'],
        'Compactados': ['.7z', '.gz', '.zip', '.tar', '.rar'],
        'Documentos': ['.pptx', '.txt', '.doc', '.rtf', '.ppt', '.xls', '.pdf', '.docx', '.odt', '.xlsx'],
        'Executaveis': ['.exe', '.deb', '.msi', '.rpm', '.app'],
        'Imagens': ['.png', '.jpg', '.ico', '.webp', '.bmp', '.svg', '.gif', '.jpeg'],
        'Videos': ['.mkv', '.mov', '.webm', '.avi', '.wmv', '.flv', '.mp4']
    }
    
    if not os.path.exists(caminho_pasta):
        print(f"{Cores.VERMELHO}❌ Erro: A pasta '{caminho_pasta}' não existe!{Cores.RESET}")
        return
    
    if not os.path.isdir(caminho_pasta):
        print(f"{Cores.VERMELHO}❌ Erro: '{caminho_pasta}' não é uma pasta!{Cores.RESET}")
        return
    
    print(f"{Cores.AZUL}📁 Organizando arquivos em: {Cores.NEGRITO}{caminho_pasta}{Cores.RESET}")
    
    arquivos_movidos = 0
    arquivos_ignorados = 0
    
    for item in os.listdir(caminho_pasta):
        caminho_item = os.path.join(caminho_pasta, item)
        
        if os.path.isdir(caminho_item):
            continue
        
        extensao = Path(item).suffix.lower()
        
        if not extensao:
            print(f"  {Cores.AMARELO}⚠️  Ignorando arquivo sem extensão: {item}{Cores.RESET}")
            arquivos_ignorados += 1
            continue
        
        categoria_destino = 'Outros'
        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                categoria_destino = categoria
                break
        
        pasta_destino = os.path.join(caminho_pasta, categoria_destino)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"  {Cores.CIANO}📂 Pasta criada: {Cores.NEGRITO}{categoria_destino}{Cores.RESET}")
        
        destino_arquivo = os.path.join(pasta_destino, item)
        if os.path.exists(destino_arquivo):
            nome_base = Path(item).stem
            contador = 1
            while os.path.exists(destino_arquivo):
                novo_nome = f"{nome_base}_{contador}{extensao}"
                destino_arquivo = os.path.join(pasta_destino, novo_nome)
                contador += 1
        
        try:
            shutil.move(caminho_item, destino_arquivo)
            print(f"  {Cores.VERDE}✅ {item}{Cores.RESET} → {Cores.NEGRITO}{categoria_destino}/{Cores.RESET}")
            arquivos_movidos += 1
        except Exception as e:
            print(f"  {Cores.VERMELHO}❌ Erro ao mover {item}: {e}{Cores.RESET}")
    
    largura_sumario = 52
    print(f"{Cores.MAGENTA}{'-' * largura_sumario}{Cores.RESET}")
    titulo = "✨ Organização Concluída! ✨"
    print(f"{Cores.NEGRITO}{titulo:^{largura_sumario}}{Cores.RESET}")
    print(f"  {Cores.VERDE}📊 Arquivos movidos: {Cores.NEGRITO}{arquivos_movidos}{Cores.RESET}")
    if arquivos_ignorados > 0:
        print(f"  {Cores.AMARELO}⚠️  Arquivos ignorados: {Cores.NEGRITO}{arquivos_ignorados}{Cores.RESET}")
    print(f"{Cores.MAGENTA}{'-' * largura_sumario}{Cores.RESET}")


def mostrar_banner():
    print(f"{Cores.MAGENTA}{'=' * 46}{Cores.RESET}")
    print(f"{Cores.MAGENTA}=={Cores.RESET}   🗂️     {Cores.NEGRITO}ORGANIZADOR DE ARQUIVOS{Cores.RESET}     🗂️   {Cores.MAGENTA}=={Cores.RESET}")
    print(f"{Cores.MAGENTA}{'=' * 46}{Cores.RESET}")

if __name__ == "__main__":
    mostrar_banner()
    
    print(f"{Cores.NEGRITO}Escolha uma opção:{Cores.RESET}")
    print(f"  {Cores.CIANO}1{Cores.RESET} - Criar arquivos de teste e organizar")
    print(f"  {Cores.CIANO}2{Cores.RESET} - Organizar uma pasta existente")
    print()
    
    opcao = input(f"{Cores.NEGRITO}Digite sua escolha (1 ou 2): {Cores.RESET}").strip()
    
    print("-" * 52) 
    
    if opcao == "1":
        pasta_teste = "./arquivos_teste"
        criar_arquivos_teste(pasta_teste)
        input(f"{Cores.AMARELO}Pressione <ENTER> para iniciar a organização...{Cores.RESET}")
        organizar_arquivos(pasta_teste)
    elif opcao == "2":
        caminho = input(f"{Cores.NEGRITO}Digite o caminho da pasta que deseja organizar(Exemplo: ./arquivos_teste): {Cores.RESET}").strip()
        confirmar = input(f"{Cores.AMARELO}⚠️  Tem certeza que deseja organizar '{Cores.NEGRITO}{caminho}{Cores.RESET}'? {Cores.NEGRITO}(s/n):{Cores.RESET} ").strip().lower()
        if confirmar == 's':
            organizar_arquivos(caminho)
        else:
            print(f"{Cores.VERMELHO}❌ Operação cancelada.{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}❌ Opção inválida!{Cores.RESET}")