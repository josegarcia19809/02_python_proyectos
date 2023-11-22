"""
Dado el diccionario de donaciones proporcionado: 
donations = dict(sam=25.0,
lena=88.99, chuck=13.0, linus=99.5, stan=150.0, 
lisa=50.25, harrison=10.0)
Utiliza un bucle para calcular el valor total de las donaciones . Guarde el resultado
en una variable llamada total_donations
"""
donations = dict(sam=25.0,
                 lena=88.99, chuck=13.0, linus=99.5, stan=150.0,
                 lisa=50.25, harrison=10.0)

total_donations = 0
for donation in donations.values():
    total_donations += donation

print(total_donations)

total_donations = sum(donation for donation in donations.values())
print(total_donations)

total_donations = sum(donations.values())
print(total_donations)
