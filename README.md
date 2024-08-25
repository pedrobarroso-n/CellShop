# Cell_Shop

**Cell_Shop** é uma aplicação web para gerenciar um inventário de celulares e realizar vendas online. Desenvolvido com o framework Flask, este projeto visa fornecer uma interface amigável para a administração de produtos e pedidos.

## Recursos

- **Gerenciamento de Produtos**: Adicione, edite e exclua celulares no inventário.
- **Vendas e Pedidos**: Crie e gerencie pedidos de venda.
- **Usuários**: Sistema de autenticação e autorização para administradores e clientes.
- **Relatórios**: Visualize relatórios de vendas e estoque.

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes pré-requisitos instalados:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/Cell_Shop.git
   cd Cell_Shop
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

## Estrutura do Projeto

- **app/**: Contém o código da aplicação Flask.
  - **static/**: Arquivos estáticos (CSS, JavaScript, imagens).
  - **templates/**: Arquivos de template HTML.
  - **routes/**: Módulos de rota.
  - **models/**: Definições de modelos de dados.
  - **forms/**: Formulários da aplicação.
- **migrations/**: Scripts de migração do banco de dados.
- **tests/**: Testes da aplicação.
- **config.py**: Configurações da aplicação.
- **requirements.txt**: Lista de dependências do projeto.

## Contribuintes

FrontEnd: [@pedrobarroso-n](https://github.com/pedrobarroso-n)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para perguntas ou suporte, entre em contato pelo Discord: toupeira21.

