# Usa imagem oficial Python
FROM python:3.11

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala bibliotecas Python
RUN pip install -r requirements.txt

# Copia código da API
COPY api/ .

# Comando para iniciar servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
