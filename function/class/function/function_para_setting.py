def f(x,a= 1,b =0,c =0):
    return 5*a*x+3*b+c**2

#忽略参数名，按照顺序传参数
#写上参数名，顺序可以打乱
#若有默认值，可以不传
print(f(1,2,3,4))   # 5*2*1+3*3+4**2 = 5*2+9+16 = 10+9+16 = 35
print(f(x=1,a=2,b=3,c=4))   # 5*2*1+3*3+4**2 = 5*2+9+16 = 10+9+16 = 35
print(f(a=2,x=1,c=4,b=3))   # 5*2*1+3*3+4**2 = 5*2+9+16 = 10+9+16 = 35
print(f(1))   # 5*1*1+3*0+0**2 = 5*1+0+0 = 5+0+0 = 5