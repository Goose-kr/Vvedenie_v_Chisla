import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    return x ** 3 - 3.9 * x ** 2 + 4.4 * x - 1.4
def f1(x):
    return 3*x**2 - 7.7*x +4.4;

def halfDivision(a, b, epsilon, delta):
    c = (a + b) / 2
    n = 0
    rooot_ = 0
    while (b-a) >= 2 * epsilon:
        n += 1
        #if (b - a) < 2 * epsilon:
         #   rooot_ = c
          #  break
        if f(c) == 0:
            return c
        if abs(f(c)) < delta:
            rooot_ = c
            break
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    print("Корень:", c)
    print("Невязка:", "{:e}".format(-f(c)))
    print("Число итераций:", n)
    return c


def secantMethod():
    m = 0
    print("Начальное приближение:  x0: ")
    x0 = float(input())
    x1 = x0 - f(x0)/f1(x0)
    #print("Начальное приближение:  x1: ")
    #x1 = float(input())
    while math.fabs(x1 - x0) > epsilon:
        xk = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = xk
        m += 1
    print("Корень:", x1)
    print("Невязка:", "{:e}".format(-f(x1)))
    print("Число итераций:", m)



x = np.linspace(0, 2.5, 50)
fig, ax = plt.subplots()
ax.plot(x, f(x), color="blue", label="y(x)")

ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()

fig.set_figwidth(8)
fig.set_figheight(6)
plt.grid()
plt.show()

print("Введите epsilon = ")
epsilon = float(input())
print("Введите delta = ")
delta = float(input())

flag = True
while flag:
    n = 0
    a = float(input("Введите левую границу интервала: "))
    b = float(input("Введите правую границу интервала: "))
    print("Результат метода половинного деления")
    halfDivision(a, b, epsilon, delta)
    print("Результат метода секущих")
    secantMethod()
    ans_flag = True
    while ans_flag:
        ans = input("Хотите найти ещё один корень? (да/нет): ")
        if ans == 'нет' or ans == 'да':
            ans_flag = False
            if ans == 'нет':
                flag = False
        else:
            print("Введите только да или нет.")
