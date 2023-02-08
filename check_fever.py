# Sometimes can write tests b/4 writing functions

def test_check_fever():
    from blood_calculator import check_fever
    input_temp = [97, 98.6, 100.1, 103]
    answer = check_fever(input_temp)
    expected = True
    assert answer == expected


def check_fever(input_list):
    for temperature in input_list:
        if temperature > 100.5:
            return True
    return False
