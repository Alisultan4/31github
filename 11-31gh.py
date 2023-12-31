# В берляндском зоопарке есть вольер с верблюдами. Как известно, верблюды любят плевать. Вася целый день наблюдал за этими интересными животными и записывал в блокнот, какой верблюд куда плевал. Теперь он хочет выяснить, есть ли в зоопарке два верблюда, которые плюнули друг в друга. Помогите ему справиться с этой задачей.

# Верблюды плюют по дуге, т. е. если верблюд в точке x плюнул на d метров вправо, то он может попасть только в верблюда, стоящего в точке x + d, если такой есть.

# Входные данные
# В первой строке содержится целое число n (1 ≤ n ≤ 100) — число верблюдов в зоопарке. Далее следует n строк по два целых числа xi и di ( - 104 ≤ xi ≤ 104, 1 ≤ |di| ≤ 2·104) — записи в блокноте Васи. xi — координата точки, в которой стоит i-ый верблюд, в метрах. di — на сколько метров плюнул i-ый верблюд. Положительные значения di означают, что i-ый верблюд плевал вправо, отрицательные — что i-ый верблюд плевал влево. В одной точке не может стоять больше одного верблюда.

# Выходные данные
# Если в зоопарке есть два верблюда, которые плюнули друг в друга, выведите YES. Иначе выведите NO.

#я бы решил эту задачку, но ноута рядом нет

n = int(input())
coordinates_set = set()

for _ in range(n):
    x, d = map(int, input().split())
    if x + d in coordinates_set or x - d in coordinates_set:
        print("YES")
        break
    coordinates_set.add(x)
    coordinates_set.add(x + d)

else:
    print("NO")

#final day yayyyy