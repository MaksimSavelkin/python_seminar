## 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a = float(input("Введиите сторону А: "))
b = float(input("Введиите сторону B: "))
c = float(input("Введиите сторону C: "))
if (a + b) > c:
    if (b + c) > a:
        if (c + a) > b:
            if a == b and b == c and a == c:
                print("Равносторонний треугольник")
            elif a == b or b == c or c == a:
                print("Равнобедренный треугольник")
            else:
                print("Разносторонний треугольник")
else:
    print("Такого треугольника не существует")