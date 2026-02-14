# Imagem Python
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /etl

# Copia tudo da pasta etl do seu PC para /etl no container
COPY . .

# Instala bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# Dá permissão para o script (mesmo no Windows, o Docker vai aplicar dentro do container Linux)
RUN ["chmod", "+x", "./wait-for-db.sh"]

# Executa o script de espera e depois o main.py
CMD ["./wait-for-db.sh", "python", "main.py"]
