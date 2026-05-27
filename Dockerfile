# Imagem base
FROM python:3.12-slim

# Diretório dentro do container
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Flask
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]