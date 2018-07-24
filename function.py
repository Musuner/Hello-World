'''请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。'''
import math
def quadratic(a,b,c):
    ins = b **2 - 4 * a * c
    if ins < 0:
        print('Error syx')
    else:
        x1 = (-b+math.sqrt(ins))/(2*a)
        x2 = (-b-math.sqrt(ins))/(2*a)
        return x1,x2

a = int(input('input a:'))
b = int(input('input b:'))
c = int(input('input c:'))
result = quadratic(a,b,c)
print (result)