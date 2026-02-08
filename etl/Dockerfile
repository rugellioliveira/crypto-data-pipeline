# Imagem Python
FROM python:3.11

# Pasta de trabalho dentro do container
WORKDIR /etl

# Copia tudo da pasta etl do seu PC para /etl no container
COPY . /etl

# Instala bibliotecas
RUN pip install requests psycopg2-binary sqlalchemy

# Executa o script principal
CMD ["python", "main.py"]
