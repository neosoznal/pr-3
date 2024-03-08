def power(x):
  return x**2 if x >= 0 else x**4

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

# Використання функції power
a = power(a)
b = power(b)
c = power(c)

print("Перше число:", a)
print("Друге число:", b)
print("Третє число:", c)