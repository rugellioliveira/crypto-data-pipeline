"""
load.py

Salva dados no banco sem duplicação.
Pipeline incremental (engenharia de dados real).
"""
from sqlalchemy import create_engine, text

# Conexão com o banco dentro do Docker
DB_URL = "postgresql://user:password@db:5432/crypto"

engine = create_engine(DB_URL)

def load_data(data):

    with engine.connect() as conn:

        # Cria tabela apenas se não existir
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS prices (
                id SERIAL PRIMARY KEY,
                coin TEXT,
                price_usd FLOAT,
                price_brl FLOAT,
                exchange_rate FLOAT,
                timestamp TIMESTAMP
            )
        """))

        # Insere dados (acumulando histórico)
        for row in data:
            conn.execute(text("""
                INSERT INTO prices
                (coin, price_usd, price_brl, exchange_rate, timestamp)
                VALUES
                (:coin, :price_usd, :price_brl, :exchange_rate, :timestamp)
            """), row)

        conn.commit()
