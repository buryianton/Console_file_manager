from math import pi, pow, sqrt, hypot

print(5*pi)

help(pow)

help(sqrt)

help(hypot)

print(pow(2, 2))
print(pow(2, 3))
print(pow(2, 4))
print('sqrt')
print(sqrt(9))
print(sqrt(16))
print(sqrt(81))
print('hypot')
print(hypot(2, 4))
print(hypot(4,8))
print(hypot(100, 200))

def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert sqrt(81) == 9
    assert sqrt(100) == 10
    assert sqrt(10000) == 100
    assert sqrt(144) == 12

def test_pi():
    assert round(pi, 2) == 3.14
    assert round(pi, 6) == 3.141593
    assert round(pi, 15) == 3.141592653589793

def test_pow():
    assert pow(2, 2) == 4
    assert pow(2, 3) == 8
    assert pow(2, 4) == 16
    assert pow(2, 5) == 32
    assert pow(2, 6) == 64
    assert pow(2, 7) == 128
    assert pow(2, 8) == 256
    assert pow(2, 9) == 512
    assert pow(2, 10) == 1024
    assert pow(3, 2) == 9
    assert pow(3, 3) == 27
    assert pow(3, 4) == 81

def test_hypot():
    assert hypot(1, 2) == sqrt(5)
    assert hypot(2, 2) == sqrt(8)
    assert round(hypot(2, 3),5) == round(sqrt(13),5)
    assert round(hypot(20, 5934), 5) == round(sqrt(20**2 + 5934**2), 5)

def test_map():
    numbers = [4, 9, 16, 25, 100, 10000, 400]
    assert list(map(sqrt, numbers)) == [2, 3, 4, 5, 10, 100, 20]

def for_test(i):
    return i*2

def test_map_2():
    numbers = [1, 2, 3, 5, 10, 20, 333]
    assert list(map(for_test, numbers)) == [2, 4, 6, 10, 20, 40, 666]

def test_filter():
    data = [1, 2, 0.5, 4, 5, 6, 9.2]
    assert list(filter(lambda x: x > 4, data)) == [5, 6, 9.2]
    assert list(filter(lambda x: type(x) == float, data)) == [0.5, 9.2]
    assert list(filter(lambda x: type(x) == int, data)) == [1, 2, 4, 5, 6]
    assert list(filter(lambda x: x%2 == 0, data)) == [2, 4, 6]

def test_sorted():
    figures = (99, 23, 0.1, 2, 3, 4, 64, 4)
    assert sorted(figures) == [0.1, 2, 3, 4, 4, 23, 64, 99]
    words = "Привет всем!"
    assert sorted(words) == [' ', '!', 'П', 'в', 'в', 'е', 'е', 'и', 'м', 'р', 'с', 'т']