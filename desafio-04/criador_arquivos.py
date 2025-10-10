from os import path, makedirs
from cores import Cores

def criar_arquivos_teste(caminho_pasta):
    if not path.exists(caminho_pasta):
        makedirs(caminho_pasta)
    
    arquivos_teste = [
        'logo_empresa.svg', 'foto_ferias.jpeg', 'planta_baixa.png',
        'icone_app.ico', 'imagem_animada.gif', 'animacao.webp',
        'apresentacao_reuniao.pptx', 'notas_importantes.txt', 'dados_vendas.xlsx',
        'manual_produto.odt', 'curriculo_joao.pdf', 'documento.docx',
        'curriculo_joao.rtf', 'video_familia.mov', 'filme_hd.mkv',
        'tutorial_rapido.webm', 'tutorial.mp4', 'filme.avi',
        'entrevista_podcast.flac', 'efeito_sonoro.ogg', 'musica.mp3',
        'gravacao_reuniao.m4a', 'som_ambiente.wav', 'projeto_codigos.zip',
        'backup_site.tar.gz', 'projeto_completo.7z', 'documentos.rar',
        'configuracoes.json', 'script_animacao.js', 'estilos.css',
        'modulo_principal.java', 'consulta.sql', 'index.html',
        'instalador.msi', 'programa.exe', 'pacote.deb',
        'biblioteca_grafica.dll', 'fonte_elegante.ttf', 'mapa_da_cidade.kml',
        'modelo_3d.obj', 'sistema_completo.iso', 'arquivo_sem_extensao'
    ]

    print(f"{Cores.CIANO}🔧 Criando {len(arquivos_teste)} arquivos de teste...{Cores.RESET}\n")
    
    for arquivo in arquivos_teste:
        caminho_arquivo = path.join(caminho_pasta, arquivo)
        try:
            with open(caminho_arquivo, 'w') as f:
                pass
        except OSError as e:
            print(f"Não foi possível criar {arquivo}: {e}")
    
    print(f"{Cores.VERDE}✅ Arquivos de teste criados em: {Cores.NEGRITO}{caminho_pasta}{Cores.RESET}\n")