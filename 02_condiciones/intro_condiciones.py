a = 4
b = 6
c = 4
print("¿b >= a? ", (b >= a))  # true
print("¿a >= c? ", (a >= c))  # true
print("¿a >= 5? ", (a >= 5))  # false
print("---------------------------")
print("¿a <= c? ", (a <= c))  # true
print("¿b <= 10? ", (b <= 10))  # true
print("¿b <= a? ", (b <= a))  # false
#   <= ✅   =< ❌    < = ❌
#   >= ✅   => ❌    > = ❌
print("---------------------------")
print("¿a == 4? ", (a == 4))  # true
print("¿a == 2? ", (a == 2))  # false
#  == ✅    = = ❌   = ❌
print("---------------------------")
print("¿a != b? ", (a != b))  # true
print("¿b != c? ", (b != c))  # true
print("¿a != c? ", (a != c))  # false
#  != ✅    = ! ❌   ! ❌
