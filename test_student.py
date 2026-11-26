
import pytest
from student import calculate_average


# Тест 1. Проверка среднего балла нескольких оценок
def test_calculate_average():
    grades = [80, 90, 100]

    result = calculate_average(grades)

    assert result == 90


# Тест 2. Проверка пустого списка
def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])


# Тест 3. Проверка оценки меньше 0
def test_negative_grade():
    with pytest.raises(ValueError):
        calculate_average([80, -10, 90])


# Тест 4. Проверка оценки больше 100
def test_grade_above_100():
    with pytest.raises(ValueError):
        calculate_average([80, 110, 90])


# Тест 5. Проверка одной оценки
def test_single_grade():
    assert calculate_average([75]) == 75


# Тест 6. Проверка дробного среднего балла
def test_fractional_average():
    assert calculate_average([70, 80, 85]) == pytest.approx(78.3333333)


# Тест 7. Проверка некорректного типа данных
def test_invalid_data_type():
    with pytest.raises(ValueError):
        calculate_average([80, "90", 100])
