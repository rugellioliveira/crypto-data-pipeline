"""
extract.py

Extrai dados da CoinGecko em USD e BRL.
"""

import requests

URL = "https://api.coingecko.com/api/v3/simple/price"


def extract_data():
    """
    Coleta preços em USD e BRL.

    Returns:
        dict: dados brutos da API
    """

    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd,brl"
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()