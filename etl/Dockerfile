# Imagem Python
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /etl

# Copia tudo da pasta etl do seu PC para /etl no container
COPY . .

# Instala bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# Executa o script principal
CMD ["python", "main.py"]
