import numpy as np
import matplotlib.pyplot as plt
import math


def f1(x, y):
    return math.sin(x) + 2 * y - 2


def f2(x, y):
    return 2 * x + math.cos(y - 1) - 0.7


def f1dx(x):
    return math.cos(x)


def f2dy(y):
    return -math.sin(y - 1)


def X(y):
    return (0.7 - math.cos(y - 1)) / 2


def Y(x):
    return 1 - math.sin(x) / 2


def J(x, y):
    j = np.eye(2)
    j[0][0] = f1dx(x)
    j[0][1] = 2
    j[1][0] = 2
    j[1][1] = f2dy(y)
    return j


def J_reverse(x, y):
    J1 = J(x, y)
    det_J1 = J1[0][0] * J1[1][1] - J1[0][1] * J1[1][0]
    if det_J1 == 0:
        print("Определитель Якобиана равен 0")
    J_reverse = np.eye(2)
    J_reverse[0][0] = (1 / det_J1) * f2dy(y)
    J_reverse[0][1] = -2 / det_J1
    J_reverse[1][0] = -2 / det_J1
    J_reverse[1][1] = (1 / det_J1) * f1dx(x)
    return J_reverse


def NewtonMethod(x, y):
    A = J_reverse(x, y)
    x_k = x - A[0][0] * f1(x, y) - A[0][1] * f2(x, y)
    y_k = y - A[1][0] * f1(x, y) - A[1][1] * f2(x, y)
    n = 1

    x0 = x
    y0 = y
    x1 = x_k
    y1 = y_k
    while max(math.fabs(x_k - x), math.fabs(y_k - y)) > epsilon:
        x = x_k
        y = y_k
        A = J_reverse(x, y)
        x_k = x - A[0][0] * f1(x, y) - A[0][1] * f2(x, y)
        y_k = y - A[1][0] * f1(x, y) - A[1][1] * f2(x, y)
        n += 1
        x2 = x_k
        y2 = y_k
        if max(abs(x0 - x1), abs(y0 - y1)) < max(abs(x1 - x2), abs(y1 - y2)):
            print("Метод расходится")
            return 0

        if max(abs(f1(x0, y0)), abs(f2(x0, y0))) < max(abs(f1(x1, y1)), abs(f2(x1, y1))):
            print("Метод расходится")
            return 0
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
    print("Корень:")
    print("x = ", round(x_k, 5))
    print("y = ", round(y_k, 5))
    print("Невязка: ", "{:e}".format(max(math.fabs(0 - f1(x_k, y_k)), math.fabs(0 - f2(x_k, y_k)))))
    print("Количество итераций = ", n)


def NewtonModifiedMethod(x, y):
    A = J_reverse(x, y)
    x_k = x - A[0][0] * f1(x, y) - A[0][1] * f2(x, y)
    y_k = y - A[1][0] * f1(x, y) - A[1][1] * f2(x, y)
    n = 1
    x0 = x
    y0 = y
    x1 = x_k
    y1 = y_k
    while max(math.fabs(x_k - x), math.fabs(y_k - y)) > epsilon:
        x = x_k
        y = y_k
        x_k = x - A[0][0] * f1(x, y) - A[0][1] * f2(x, y)
        y_k = y - A[1][0] * f1(x, y) - A[1][1] * f2(x, y)
        n += 1
        x2 = x_k
        y2 = y_k
        if max(abs(x0 - x1), abs(y0 - y1)) < max(abs(x1 - x2), abs(y1 - y2)):
            print("Метод расходится")
            return 0

        if max(abs(f1(x0, y0)), abs(f2(x0, y0))) < max(abs(f1(x1, y1)), abs(f2(x1, y1))):
            print("Метод расходится")
            return 0
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
    print("Корень:")
    print("x = ", round(x_k, 5))
    print("y = ", round(y_k, 5))
    print("Невязка: ", "{:e}".format(max(math.fabs(0 - f1(x_k, y_k)), math.fabs(0 - f2(x_k, y_k)))))
    print("Количество итераций = ", n)

print("Введите epsilon: ")
epsilon = float(input())
fig, ax = plt.subplots()

y1 = np.linspace(0, 2, 500)
x1 = list()
for i in range(len(y1)):
    x1.append(X(y1[i]))
ax.plot(x1, y1, color="blue", label="f1")

x2 = np.linspace(-1, 1, 500)
y2 = list()
for i in range(len(x2)):
    y2.append(Y(x2[i]))
ax.plot(x2, y2, color="red", label="f2")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
fig.set_figwidth(8)
fig.set_figheight(6)
plt.grid()
plt.show()

print("Введите начальное приближение")
x = float(input("Введите x: "))
y = float(input("Введите y: "))
print("Результаты метода Ньютона")
NewtonMethod(x, y)
print("Результаты модифицированного метода Ньютона")
NewtonModifiedMethod(x, y)