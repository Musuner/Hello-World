while (1) :
    str=input()
    if ' ' in str:
        str_list=str.split( )
    a=str_list[0]
    b=str_list[1]
    print(a)
    print(b)
    c=int(a)
    d=int(b)
    if c%d ==0:
        print('YES')
    else:
        print('NO')
    continue
