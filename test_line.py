def test_point_on_line():
    from line import point_on_line
    point1 = (1, 1)
    point2 = (2, 2)
    x = 3
    answer = point_on_line(point1, point2, x)
    assert answer == 3