import pandas as pd
import sys
from pathlib import Path

class Cores:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

def mostrar_banner():
    print(f"\n{Cores.MAGENTA}{'=' * 50}{Cores.RESET}")
    print(f"{Cores.MAGENTA}=={Cores.RESET}  📊  {Cores.NEGRITO}ANÁLISE DE DADOS DE USUÁRIOS{Cores.RESET}  📊  {Cores.MAGENTA}=={Cores.RESET}")
    print(f"{Cores.MAGENTA}{'=' * 50}{Cores.RESET}\n")

def carregar_csv(caminho_arquivo):
    try:
        if not Path(caminho_arquivo).exists():
            print(f"{Cores.VERMELHO}❌ Erro: Arquivo '{caminho_arquivo}' não encontrado!{Cores.RESET}\n")
            return None
        
        df = pd.read_csv(caminho_arquivo)
        print(f"{Cores.VERDE}✅ Arquivo carregado com sucesso!{Cores.RESET}\n")
        return df
        
    except pd.errors.EmptyDataError:
        print(f"{Cores.VERMELHO}❌ Erro: O arquivo está vazio!{Cores.RESET}\n")
        return None
    except pd.errors.ParserError:
        print(f"{Cores.VERMELHO}❌ Erro: Não foi possível processar o arquivo CSV!{Cores.RESET}\n")
        return None
    except Exception as e:
        print(f"{Cores.VERMELHO}❌ Erro ao carregar arquivo: {e}{Cores.RESET}\n")
        return None

def mostrar_informacoes_basicas(df):
    print(f"{Cores.CIANO}{Cores.NEGRITO}📋 INFORMAÇÕES BÁSICAS{Cores.RESET}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}")
    print(f"{Cores.NEGRITO}Total de registros:{Cores.RESET} {len(df)}")
    print(f"{Cores.NEGRITO}Total de colunas:{Cores.RESET} {len(df.columns)}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}\n")
    
    print(f"{Cores.CIANO}{Cores.NEGRITO}📄 PRIMEIRAS 5 LINHAS{Cores.RESET}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}")
    print(df.head())
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}\n")

def calcular_estatisticas(df):
    print(f"{Cores.CIANO}{Cores.NEGRITO}📊 ESTATÍSTICAS{Cores.RESET}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}")
    
    # Média de idade
    media_idade = df['idade'].mean()
    print(f"{Cores.VERDE}👤 Média de idade:{Cores.RESET} {Cores.NEGRITO}{media_idade:.2f} anos{Cores.RESET}")
    
    # Valor total de compras
    valor_total = df['valor_compras'].sum()
    print(f"{Cores.VERDE}💰 Valor total de compras:{Cores.RESET} {Cores.NEGRITO}R$ {valor_total:,.2f}{Cores.RESET}")
    
    # Valor médio de compras
    valor_medio = df['valor_compras'].mean()
    print(f"{Cores.VERDE}💵 Valor médio de compras:{Cores.RESET} {Cores.NEGRITO}R$ {valor_medio:,.2f}{Cores.RESET}")
    
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}\n")
    
    # Usuários por cidade
    print(f"{Cores.CIANO}{Cores.NEGRITO}🌆 USUÁRIOS POR CIDADE{Cores.RESET}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}")
    usuarios_por_cidade = df['cidade'].value_counts()
    
    for cidade, quantidade in usuarios_por_cidade.items():
        print(f"{Cores.AMARELO}{cidade}:{Cores.RESET} {Cores.NEGRITO}{quantidade} usuário(s){Cores.RESET}")
    
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}\n")
    
    return valor_medio

def filtrar_top_usuarios(df, valor_medio):
    df_top = df[df['valor_compras'] > valor_medio].copy()
    
    print(f"{Cores.CIANO}{Cores.NEGRITO}⭐ USUÁRIOS TOP (Compras acima da média){Cores.RESET}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}")
    print(f"{Cores.NEGRITO}Total de usuários top:{Cores.RESET} {len(df_top)}")
    print(f"{Cores.NEGRITO}Valor mínimo de compras (média):{Cores.RESET} R$ {valor_medio:,.2f}")
    print(f"{Cores.AZUL}{'─' * 50}{Cores.RESET}\n")
    
    if len(df_top) > 0:
        print(f"{Cores.AMARELO}Usuários filtrados:{Cores.RESET}")
        print(df_top.to_string(index=False))
        print()
    
    return df_top

def salvar_top_usuarios(df_top, arquivo_saida='usuarios_top.csv'):
    """
    Salva os usuários top em um novo arquivo CSV
    
    Args:
        df_top (DataFrame): DataFrame com usuários filtrados
        arquivo_saida (str): Nome do arquivo de saída
    """
    try:
        df_top.to_csv(arquivo_saida, index=False)
        print(f"{Cores.VERDE}✅ Arquivo '{arquivo_saida}' criado com sucesso!{Cores.RESET}")
        print(f"{Cores.VERDE}📁 Localização: {Path(arquivo_saida).absolute()}{Cores.RESET}\n")
    except Exception as e:
        print(f"{Cores.VERMELHO}❌ Erro ao salvar arquivo: {e}{Cores.RESET}\n")

def main():
    """Função principal"""
    mostrar_banner()
    
    arquivo = input(f"{Cores.NEGRITO}Digite o caminho do arquivo CSV (ex: usuarios.csv): {Cores.RESET}").strip()
    print()
    
    # 1. Carrega o CSV em um DataFrame
    df = carregar_csv(arquivo)
    if df is None:
        return
    
    # 2. Mostra total de registros e as cinco primeiras linhas
    mostrar_informacoes_basicas(df)
    
    # 3. Calcula estatísticas
    valor_medio = calcular_estatisticas(df)
    
    # 4. Filtra usuários com valor de compras acima da média
    df_top = filtrar_top_usuarios(df, valor_medio)
    
    # Salva o resultado em um novo arquivo
    if len(df_top) > 0:
        salvar_top_usuarios(df_top)
    else:
        print(f"{Cores.AMARELO}⚠️  Nenhum usuário com compras acima da média.{Cores.RESET}\n")
    
    print(f"{Cores.MAGENTA}{'=' * 50}{Cores.RESET}")
    print(f"{Cores.VERDE}{Cores.NEGRITO}Análise concluída com sucesso!{Cores.RESET}")
    print(f"{Cores.MAGENTA}{'=' * 50}{Cores.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}⚠️  Programa interrompido pelo usuário.{Cores.RESET}\n")
        sys.exit(0)