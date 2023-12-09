# Театральная площадь в столице Берляндии представляет собой прямоугольник n × m метров. По случаю очередного юбилея города, было принято решение о замощении площади квадратными гранитными плитами. Каждая плита имеет размер a × a.

# Какое наименьшее количество плит понадобится для замощения площади? Разрешено покрыть плитами большую поверхность, чем театральная площадь, но она должна быть покрыта обязательно. Гранитные плиты нельзя ломать или дробить, а разрешено использовать только целиком. Границы плит должны быть параллельны границам площади.

# Входные данные
# В первой строке записано три целых натуральных числа n, m и a (1 ≤ n, m, a ≤ 109).

# Выходные данные
# Выведите искомое количество плит.

def solve(n, m, a):
  """
  Решает задачу o замощении театральной площади в столице Берляндии.

  Args:
    n: Длина площади в метрах.
    m: Ширина площади в метрах.
    a: Размер гранитной плиты в метрах.

  Returns:
    Количество плит, необходимое для замощения площади.
  """

  # Находим количество плит, умещающихся по длине площади.

  x = n // a

  # Находим количество плит, умещающихся по ширине площади.

  y = m // a

  # Возвращаем минимальное из двух значений.

  return min(x, y)


def main():
  # Вводим данные.

  n, m, a = map(int, input().split())

  # Решаем задачу.

  result = solve(n, m, a)

  # Выводим результат.

  print(result)


if __name__ == "__main__":
  main()
