# tup = (1,) + (1,)
# tup = tup + tup
# print(len(tup))
# # print(tup)
#
# tup=(1,2,4,8)
# tup=tup[-2:-1]
# tup=tup[-1]
# print(tup)
#
# dica={"one": "two", "three": "one",  "two": "three"}
#
# v= dica["three"]
#
# for k in range(len(dica)):
#     v=dica[v]
#
# print(v)

# foo=(1,2,3)
# foo.index(0)

# my_list=[1,2]
# for v in range(2):
#     my_list.insert(-1, my_list[v])
#
# print(my_list)

# a=1
# b=0
#
# a=a^b
# b=a^b
# a=a^b
#
# print(a, b)


# def func(a,b):
#     return b**a
#
# print(func(b=2, 2))

# print("a", "b", "c", sep="sep")

# try:
#     print(5/0)
#     break
# except:
#     print()
# except(ValueError, ZeroDivisionError):
#     print()

my_list= [x*x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))