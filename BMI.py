height = float(input("please input height:"))
weight = float(input("please input weight:"))
BMI = weight/(height**2)
print('BMI = %f' % BMI)
if BMI < 18.5:
    print('过轻')
elif BMI <25 and BMI >18.5:
    print('正常')
	#break
elif BMI < 28:
    print('过重')
	#break
elif BMI < 32:
    print('肥胖')
	#break
else:
    print('严重肥胖')