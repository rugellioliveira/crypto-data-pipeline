"""
transform.py

Transforma dados com USD e BRL.
"""

from datetime import datetime


def transform_data(raw_data):
    """
    Converte dados para estrutura pronta para o banco.

    Args:
        raw_data (dict)

    Returns:
        list
    """

    transformed = []
    timestamp = datetime.utcnow()

    for coin, data in raw_data.items():

        usd_price = data["usd"]
        brl_price = data["brl"]

        # taxa implícita USD -> BRL (extra interessante)
        exchange_rate = brl_price / usd_price if usd_price else None

        transformed.append({
            "coin": coin,
            "price_usd": usd_price,
            "price_brl": brl_price,
            "exchange_rate": exchange_rate,
            "timestamp": timestamp
        })

    return transformed