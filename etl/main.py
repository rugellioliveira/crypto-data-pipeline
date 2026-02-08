"""
main.py

Orquestra o pipeline ETL.
"""

from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline():
    """Executa ETL completo"""

    raw = extract_data()
    clean = transform_data(raw)
    load_data(clean)


# executa apenas se rodar diretamente
if __name__ == "__main__":
    run_pipeline()