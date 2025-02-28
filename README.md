# Cell Shop

**Cell Shop** é uma aplicação web desenvolvida para gerenciar o inventário de periféricos de celulares e facilitar vendas online de forma eficiente. Utilizando o framework Flask, o projeto oferece uma interface intuitiva e responsiva, com o objetivo é simplificar a administração do estoque e otimizar o processo de vendas, proporcionando uma experiência prática e acessível tanto para administradores quanto para clientes.

## Recursos

- **Gerenciamento de Produtos**: Adicione, edite, busque e exclua do inventário.
- **Vendas e Pedidos**: Crie e gerencie pedidos de venda.
- **Usuários**: Sistema dividido entre administradores e clientes.

 ## Tecnologias

- Html5
- Css3
- JavaScript (ES6)
- Python 3.8
- Flask 3.1.0
- Git

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes pré-requisitos instalados:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/pedrobarroso-n/CellShop.git
   cd CellShop
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=sua_chave_secreta
   DATABASE_URL=sua_url_do_banco_de_dados
   ```

5. **Inicialize o banco de dados:**

   ```bash
   flask db upgrade
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   flask run
   ```

   Acesse a aplicação em [http://localhost:5000](http://localhost:5000).

## Estrutura Principal

- **api**: Pasta unificada para usabilidade do servidor de hospedagem
   - **static/**: Pasta de arquivos estáticos.
      - **css/** - Arquivos .css
      - **img/** - Arquivos de imagem
      - **js/** - Arquivos .js
   - **templates/**: Pasta de arquivos html.
      - **pasta/index.html** - Cada pasta representa um tipo de produto com seu index.html para usabilidade.
      - **index.html** - Página html principal(home page), inicial na navegação do sistema.
   - **main.py** - Controle e gerencia do banco de dados.
   - **bd.py** - Estrutura do banco de dados.

- **Db.sql** - Banco de dados do projeto.
- **vercel.json** - Controle de arquivos carregados pelo servidor de hospedagem

## Contribuições

1. [@pedrobarroso-n](https://github.com/pedrobarroso-n/)
2. [@Ranykelle21](https://github.com/Ranykelle21)
3. [@GleisonPS](https://github.com/GleisonPS)

## Acesso Simplificado

   Acesse a aplicação on-line em [https://cellshop-p2.vercel.app/](https://cellshop-p2.vercel.app/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
