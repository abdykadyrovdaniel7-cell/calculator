
def calculate_average(grades):
    """
    Вычисляет средний балл студента.

    grades — список оценок от 0 до 100.
    """

    # Проверка пустого списка
    if not grades:
        raise ValueError("Список оценок не должен быть пустым")

    # Проверка корректности каждой оценки
    for grade in grades:
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            raise ValueError("Оценки должны быть числами")

        if grade < 0:
            raise ValueError("Оценка не может быть меньше 0")

        if grade > 100:
            raise ValueError("Оценка не может быть больше 100")

    # Вычисление среднего балла
    average = sum(grades) / len(grades)

    return average


# Проверка работы программы
if __name__ == "__main__":
    student_grades = [80, 90, 100]

    result = calculate_average(student_grades)

    print("Оценки студента:", student_grades)
    print("Средний балл студента:", result)
