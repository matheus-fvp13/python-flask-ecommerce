from src import create_app, db
from flask import current_app
from src.models.user_model import User

app = create_app()

@app.cli.command("create-db")
def create_db():
    """Comando para criar o banco de dados"""
    with current_app.app_context():
        db.create_all()
    print("Banco de dados criado com sucesso!")

if __name__ == '__main__':
    app.run(debug=True)