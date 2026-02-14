#!/bin/sh
# Espera até o Postgres estar pronto
until nc -z db 5432; do
  echo "Aguardando Postgres..."
  sleep 2
done

# Roda o comando passado para o container (normalmente python main.py)
exec "$@"
