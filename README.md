# Flask Rest

## Pycharm

Projeto criado com o Pycharm no Ubuntu, Isso instala a versão Community (gratuita)

    sudo snap install pycharm-community --classic
    
    pycharm-community

Se quiser a versão Professional

    sudo snap install pycharm-professional --classic

    pycharm-professional

### Ambiente Virtual (venv)

Pycharm cria o ambiente virtual automaticamente em novos projetos

    python -m venv .venv

Lembre-se de ativar para usar

    source .venv/bin/activate

Para sair

    deactivate

### Requiriments

Export

    source .venv/bin/activate

    pip freeze > requirements.txt

Import
    
    source .venv/bin/activate

    pip install -r requirements.txt

## Run

Projeto simples, http://127.0.0.1:5000

    python app.py

Jeito Flask CLI

    source .venv/bin/activate
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run

Forma moderna (recomendada)

    flask --app app run --debug

Ou

    flask --app app run

## Docker

    docker build -t flask-rest .

    docker run --rm -it -p 5000:5000 --name flask-rest flask-rest