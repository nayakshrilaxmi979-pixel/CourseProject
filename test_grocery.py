from grocery import calculate_total

def test_calculate_total():
    assert calculate_total(2, 60, 3, 45) == 255

def test_calculate_total_zero():
    assert calculate_total(0, 50, 2, 30) == 60

def test_calculate_total_decimal():
    assert calculate_total(2, 10.5, 3, 20) == 81