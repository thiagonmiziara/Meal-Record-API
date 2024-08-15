# Meal Record App

Este é um aplicativo simples desenvolvido em Flask para registrar e gerenciar refeições. Ele permite criar, ler, atualizar e excluir informações sobre refeições.

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PyMySQL

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/meal-record.git
   cd meal-record
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do Banco de Dados:**

   - Certifique-se de ter um banco de dados MySQL criado. Atualize a URI do banco de dados no arquivo principal (app.py) conforme necessário:

   ```bash
   app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://usuario:senha@127.0.0.1:3306/nome_do_banco"
   ```

5. **Inicialize o Banco de Dados:**
   - Execute o Flask Shell para criar as tabelas:
   ```bash
   flask shell
   ```
   - Dentro do shell:
   ```bash
      db.create_all()
      exit()
   ```

## Endpoints

1. **Listar todas as refeições:**

   - Método: GET
   - URL: /meals
   - Resposta:
     ```bash
       {
         "meals": [
                     {
                       "id": 1,
                       "name": "Salada",
                       "description": "Salada de frutas",
                       "datetime": "2024-08-15T12:00:00",
                       "dieting": false
                     }
                   ]
       }
     ```

2. **Obter uma refeição por ID**

   - Método: GET
   - URL: /meal/meal_id
   - Resposta:
     ```bash
           {
             "id": 1,
             "name": "Salada",
             "description": "Salada de frutas",
             "datetime": "2024-08-15T12:00:00",
             "dieting": false
           }
     ```

3. **Criar uma nova refeição**

   - Método: POST
   - URL: /meal
   - Corpo da Requisição:
     ```bash
           {
             "name": "Salada",
             "description": "Salada de frutas",
             "dieting": false
           }
     ```

4. **Atualizar uma refeição**

   - Método: PUT
   - URL: /meal/meal_id
   - Corpo da Requisição:
     ```bash
           {
               "name": "Salada",
               "description": "Salada de folhas",
               "dieting": true
            }
     ```

5. **Deletar uma refeição**
   - Método: DELETE
   - URL: /meal/meal_id
   - Resposta:
     ```bash
           {
             "message": "Meal deleted successfully"
           }
     ```
