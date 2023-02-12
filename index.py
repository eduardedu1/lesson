lang='EN'
lang_opt=input('Enter 1 to change language or other key to continue->>')
prodolzhit ='y'
while lang_opt=='1':
    if lang =='RU':
        lang='EN'
        lang_opt=input('Enter 1 to change language or other key to continue->>')
    else:
        lang='RU'
        lang_opt=input('Введите 1, чтобы сменить язык, или любую клавишу, чтобы продолжить->>')
if lang=='EN':
    f='Enter first number->>'
    o='Enter operation (+, -, /, *)->>'
    s='Enter second number->>'
    r='Result->>'
    e='Error'
    p="Enter 'y' to continue and other key to finish->>"
if lang =='RU':
    f='Введите первое число->>'
    o='Введите оперцию (+, -, *, /)->>'
    s='Введите второе число->>'
    r='Результат->>'
    e='Ошибка'
    p="Введите 'y' или любую клавишу, чтобы закончить->>"
while prodolzhit =='y':
    f_num=float(input(f))
    oper=input(o)
    s_num=float(input(s))
    if oper=='+':
        print(r, f_num+s_num)
    elif oper=='-':
        print(r, f_num-s_num)
    elif oper=='*':
        print(r, f_num*s_num)
    elif oper=='/':
        print(r, f_num/s_num)
    else:
        print(e)
    prodolzhit=input(p)