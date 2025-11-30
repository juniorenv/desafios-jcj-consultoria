# 🚀 Desafios JCJ Consultoria

Repositório contendo soluções para desafios técnicos propostos pela JCJ Consultoria. Cada desafio aborda diferentes aspectos do desenvolvimento de software, desde manipulação de strings até análise de dados.

## 📋 Índice

- [Desafio 01 - Processamento de Pedidos com Regex](#desafio-01---processamento-de-pedidos-com-regex)
- [Desafio 02 - Gerador de Link na Bio](#desafio-02---gerador-de-link-na-bio)
- [Desafio 03 - API REST de Tarefas](#desafio-03---api-rest-de-tarefas)
- [Desafio 04 - Organizador de Arquivos](#desafio-04---organizador-de-arquivos)
- [Desafio 05 - Consulta de CEP](#desafio-05---consulta-de-cep)
- [Desafio 06 - Análise de Dados de Usuários](#desafio-06---análise-de-dados-de-usuários)

---

## 🎯 Desafio 01 - Processamento de Pedidos com Regex

### 📝 Descrição

Sistema de processamento de pedidos de delivery utilizando expressões regulares (Regex) para extrair informações estruturadas de mensagens de texto não formatadas.

### 🛠️ Tecnologias

- JavaScript (Node.js)
- Expressões Regulares (Regex)

### ⚙️ Funcionalidades

- Extração de nome do cliente
- Identificação de itens do pedido com quantidades
- Captura de observações especiais
- Extração de endereço de entrega
- Identificação da forma de pagamento

### 🚀 Como Executar

```bash
cd desafio-01
node script.js
```

### 💡 Exemplo de Entrada

```
Olá, gostaria de fazer um pedido!
Cliente: Junior Almeida
Itens:
2x Hambúrguer (sem cebola)
1x Batata Frita Media
Endereço: Rua das Flores, 312, Bairro Centro
Pagamento: Cartão de Crédito
```

### 📤 Exemplo de Saída

```json
{
  "cliente": "Junior Almeida",
  "itens": [
    {
      "quantidade": 2,
      "produto": "Hambúrguer",
      "observacao": "sem cebola"
    },
    {
      "quantidade": 1,
      "produto": "Batata Frita Media",
      "observacao": null
    }
  ],
  "endereco": "Rua das Flores, 312, Bairro Centro",
  "formaPagamento": "Cartão de Crédito"
}
```

---

## 🔗 Desafio 02 - Gerador de Link na Bio

### 📝 Descrição

Aplicação web interativa que permite criar previews de páginas "Link na Bio" (estilo Linktree), com visualização em tempo real em um dispositivo mobile simulado.

### 🛠️ Tecnologias

- HTML5
- CSS3
- JavaScript (Vanilla)

### ⚙️ Funcionalidades

- Formulário para entrada de dados (nome, foto, links)
- Preview em tempo real
- Design responsivo com simulação de dispositivo móvel
- Interface moderna com animações

### 🚀 Como Executar

```bash
cd desafio-02
# Abra o arquivo index.html em um navegador
```

### 🎨 Características

- Design com fonte Poppins
- Efeitos hover nos links
- Preview instantâneo
- Layout responsivo

---

## 🔌 Desafio 03 - API REST de Tarefas

### 📝 Descrição

API RESTful completa para gerenciamento de tarefas (To-Do List) implementada com Node.js e Express, seguindo princípios de arquitetura limpa e boas práticas de desenvolvimento.

### 🛠️ Tecnologias

- Node.js
- Express.js
- JavaScript (ES Modules)

### 🏗️ Arquitetura

```
src/
├── controllers/     # Camada de controle (requisições HTTP)
├── services/        # Lógica de negócio
├── models/          # Modelos de dados
├── routes/          # Definição de rotas
└── errors/          # Classes de erro customizadas
```

### 📡 Endpoints

| Método | Endpoint         | Descrição              |
| ------ | ---------------- | ---------------------- |
| GET    | `/api/tasks`     | Lista todas as tarefas |
| GET    | `/api/tasks/:id` | Busca tarefa por ID    |
| POST   | `/api/tasks`     | Cria nova tarefa       |
| PUT    | `/api/tasks/:id` | Atualiza tarefa        |
| DELETE | `/api/tasks/:id` | Remove tarefa          |

### 🚀 Como Executar

```bash
cd desafio-03
npm install
node src/app.js
```

### 📋 Exemplo de Requisição

```bash
# Criar tarefa
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar Node.js",
    "description": "Aprender Express e APIs REST",
    "completed": false
  }'
```

### ✨ Destaques

- Validação de dados
- Tratamento de erros customizado
- Arquitetura em camadas
- Código limpo e bem documentado

---

## 📁 Desafio 04 - Organizador de Arquivos

### 📝 Descrição

Sistema automatizado em Python para organização de arquivos por categoria, com criação opcional de arquivos de teste e interface colorida no terminal.

### 🛠️ Tecnologias

- Python 3
- Biblioteca `os`, `shutil`, `pathlib`

### ⚙️ Funcionalidades

- Organização automática por tipo de arquivo
- Criação de arquivos de teste
- Categorização inteligente em pastas:
  - 🎵 Áudios
  - 💻 Códigos
  - 📦 Compactados
  - 📄 Documentos
  - ⚙️ Executáveis
  - 🖼️ Imagens
  - 🎬 Vídeos
  - 📂 Outros
- Interface colorida no terminal
- Prevenção de sobrescrita de arquivos

### 🚀 Como Executar

```bash
cd desafio-04
python organizador_arquivos.py
```

### 📊 Exemplo de Uso

```
🗂️  ORGANIZADOR DE ARQUIVOS 🗂️
Escolha uma opção:
  1 - Criar arquivos de teste e organizar
  2 - Organizar uma pasta existente
```

### 🎨 Características

- Interface colorida com emojis
- Relatório detalhado de operações
- Tratamento de conflitos de nomes
- Validação de caminhos

---

## 📮 Desafio 05 - Consulta de CEP

### 📝 Descrição

Aplicação CLI em Python para consulta de CEPs brasileiros utilizando a API ViaCEP, com interface amigável e tratamento robusto de erros.

### 🛠️ Tecnologias

- Python 3
- Biblioteca `requests`
- API ViaCEP

### ⚙️ Funcionalidades

- Consulta de CEP via API ViaCEP
- Validação de formato de CEP
- Formatação automática (aceita com ou sem hífen)
- Exibição detalhada de informações:
  - Logradouro
  - Bairro
  - Cidade/Estado
  - Região
  - Código IBGE
  - DDD
- Tratamento de erros de conexão
- Interface colorida e intuitiva

### 🚀 Como Executar

```bash
cd desafio-05
pip install -r requirements.txt
python consulta_api.py
```

### 💡 Exemplo de Uso

```
📍 CONSULTA DE CEP - ViaCEP 📍
Digite o CEP: 41343-265

✅ CEP ENCONTRADO!
📮 CEP: 41343-265
📍 Logradouro: Rua Exemplo
🏙️  Bairro: Centro
🌆 Cidade: Salvador
🗺️  Estado: Bahia (BA)
```

### 📦 Dependências

- requests==2.32.5
- urllib3==2.5.0

---

## 📊 Desafio 06 - Análise de Dados de Usuários

### 📝 Descrição

Sistema de análise de dados de usuários utilizando Pandas para processamento de arquivos CSV, cálculo de estatísticas e geração de relatórios.

### 🛠️ Tecnologias

- Python 3
- Pandas
- NumPy

### ⚙️ Funcionalidades

- Carregamento e validação de arquivos CSV
- Cálculo de estatísticas:
  - Média de idade
  - Valor total de compras
  - Valor médio de compras
- Análise por cidade
- Filtro de usuários "top" (compras acima da média)
- Exportação de dados filtrados
- Interface colorida no terminal

### 🚀 Como Executar

```bash
cd desafio-06
pip install -r requirements.txt
python analise_usuarios.py
```

### 📋 Formato do CSV

```csv
nome,idade,cidade,data_de_cadastro,valor_compras
João,28,Uberlândia,2023-06-01,350.75
Maria,34,Belo Horizonte,2023-05-10,120.50
```

### 📈 Exemplo de Saída

```
📊 ESTATÍSTICAS
👤 Média de idade: 31.88 anos
💰 Valor total de compras: R$ 3,441.95
💵 Valor médio de compras: R$ 430.24

🌆 USUÁRIOS POR CIDADE
Uberlândia: 3 usuário(s)
São Paulo: 3 usuário(s)
Belo Horizonte: 2 usuário(s)

⭐ USUÁRIOS TOP (Compras acima da média)
Total de usuários top: 4
```

### 📦 Dependências

- pandas==2.3.3
- numpy==2.0.2

---
