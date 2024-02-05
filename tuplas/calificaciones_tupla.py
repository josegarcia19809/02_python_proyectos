mis_calificaciones = (87, 90, 81, 70, 100, 88)

print(mis_calificaciones[0])  # 87
print(mis_calificaciones[-1])  # 88
print(mis_calificaciones[1:])  # (90, 81, 70, 100, 88)
print(mis_calificaciones[:-2])  # (87, 90, 81, 70)

for calificacion in mis_calificaciones:
    print(calificacion)

print()
t1 = mis_calificaciones + (1000, 10000)
print(t1)  # (87, 90, 81, 70, 100, 88, 1000, 10000)

t2 = mis_calificaciones * 3
print(len(t2))  # 18
print(t2)  # (87, 90, 81, 70, 100, 88, 87, 90, 81, 70, 100, 88, 87, 90, 81, 70, 100, 88)
print(10 in mis_calificaciones)  # False
print(-10 not in mis_calificaciones)  # True
