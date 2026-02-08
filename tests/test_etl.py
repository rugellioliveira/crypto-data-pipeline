from etl.extract import extract_data


def test_extract():
    data = extract_data()
    assert "bitcoin" in data
