def test_check_fever():
    from blood_calculator import check_fever
    input_temps = [97, 98.6, 100.1, 103, 98.4]
    answer = check_fever(input_temps)
    expected = True
    assert answer == expected



