"""
API FastAPI para consultar preços.
"""

from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Conexão com banco
engine = create_engine(
    "postgresql://user:password@db:5432/crypto"
)


@app.get("/prices")
def get_prices():
    """
    Lista todos registros.
    """

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM prices"))
        rows = [dict(r._mapping) for r in result]

    return rows


@app.get("/compare/{coin}")
def compare_coin(coin: str):
    """
    Compara USD x BRL.
    """

    query = text("""
        SELECT coin, price_usd,
               price_brl, exchange_rate
        FROM prices
        WHERE coin = :coin
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"coin": coin})
        row = result.fetchone()

    return dict(row._mapping) if row else {"error": "not found"}
