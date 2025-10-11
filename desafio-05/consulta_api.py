import requests
import sys

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
    print(f"\n{Cores.CIANO}{'=' * 42}{Cores.RESET}")
    print(f"{Cores.CIANO}=={Cores.RESET}  📍  {Cores.NEGRITO}CONSULTA DE CEP - ViaCEP{Cores.RESET}  📍  {Cores.CIANO}=={Cores.RESET}")
    print(f"{Cores.CIANO}{'=' * 42}{Cores.RESET}\n")

def limpar_cep(cep):
    return ''.join(filter(str.isdigit, cep))

def validar_cep(cep):
    return len(cep) == 8 and cep.isdigit()

def formatar_cep(cep):
    return f"{cep[:5]}-{cep[5:]}"

def consultar_cep(cep):
    cep_limpo = limpar_cep(cep)
    
    if not validar_cep(cep_limpo):
        print(f"{Cores.VERMELHO}❌ CEP inválido! O CEP deve conter 8 dígitos.{Cores.RESET}")
        return None
    
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    print(f"{Cores.AMARELO}🔍 Consultando CEP {formatar_cep(cep_limpo)}...{Cores.RESET}\n")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        dados = response.json()
        
        if 'erro' in dados and dados['erro']:
            print(f"{Cores.VERMELHO}❌ CEP não encontrado na base de dados.{Cores.RESET}")
            return None
        
        return dados
        
    except requests.exceptions.Timeout:
        print(f"{Cores.VERMELHO}❌ Erro: Tempo de resposta excedido.{Cores.RESET}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{Cores.VERMELHO}❌ Erro: Falha na conexão com a API.{Cores.RESET}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"{Cores.VERMELHO}❌ Erro na requisição: {e}{Cores.RESET}")
        return None
    except ValueError:
        print(f"{Cores.VERMELHO}❌ Erro ao processar resposta da API.{Cores.RESET}")
        return None

def exibir_endereco(dados):
    if not dados:
        return
    
    print(f"{Cores.VERDE}{Cores.NEGRITO}✅ CEP ENCONTRADO!{Cores.RESET}\n")
    print(f"{Cores.MAGENTA}{'─' * 50}{Cores.RESET}")
    
    campos = [
        ("📮 CEP", dados.get('cep', 'N/A')),
        ("📍 Logradouro", dados.get('logradouro', 'N/A')),
        ("🏘️  Complemento", dados.get('complemento', 'N/A')),
        ("🏙️  Bairro", dados.get('bairro', 'N/A')),
        ("🌆 Cidade", dados.get('localidade', 'N/A')),
        ("🗺️  Estado", f"{dados.get('estado', 'N/A')} ({dados.get('uf', 'N/A')})"),
        ("🌎 Região", dados.get('regiao', 'N/A')),
        ("📊 IBGE", dados.get('ibge', 'N/A')),
        ("📞 DDD", dados.get('ddd', 'N/A')),
    ]
    
    for label, valor in campos:
        if valor and valor != 'N/A' and valor.strip():
            print(f"{Cores.AZUL}{label}:{Cores.RESET} {Cores.NEGRITO}{valor}{Cores.RESET}")
        else:
            print(f"{Cores.AZUL}{label}:{Cores.RESET} {Cores.AMARELO}(não informado){Cores.RESET}")
    
    print(f"{Cores.MAGENTA}{'─' * 50}{Cores.RESET}\n")

def menu_principal():
    mostrar_banner()
    
    while True:
        print(f"{Cores.NEGRITO}Escolha uma opção:{Cores.RESET}")
        print(f"  {Cores.CIANO}1{Cores.RESET} - Consultar um CEP")
        print(f"  {Cores.CIANO}2{Cores.RESET} - Sair")
        print()
        
        opcao = input(f"{Cores.NEGRITO}Digite sua escolha: {Cores.RESET}").strip()
        print()
        
        if opcao == '1':
            cep = input(f"{Cores.NEGRITO}Digite o CEP (ex: 41343-265 ou 41343265): {Cores.RESET}").strip()
            print()
            dados = consultar_cep(cep)
            exibir_endereco(dados)
                
        elif opcao == '2':
            print(f"{Cores.VERDE}👋 Até logo!{Cores.RESET}\n")
            sys.exit(0)
            
        else:
            print(f"{Cores.VERMELHO}❌ Opção inválida!{Cores.RESET}\n")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}⚠️  Programa interrompido pelo usuário.{Cores.RESET}")
        sys.exit(0)