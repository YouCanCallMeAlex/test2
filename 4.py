
import json
#



def register():
    log = input('Введите логин:')
    pswd = input('Введите пароль:')
    with open('reg.json','r') as f:
        base = json.load(f)
    if log in base.keys():
        print('Пользователь с таким именем уже существует!')
    else:
        base[log] = pswd
        with open('reg.json','w') as f:
            json.dump(base,f)
    
def enter_sys():
    log = input('Введите логин:')
    pswd = input('Введите пароль:')
    with open('reg.json','r') as f:
        base = json.load(f)
    if log in base:
        if base[log] == pswd:
            print('Добро пожаловать!!')
        else:
            print('Неверный пароль!!')
    else:
        print('Неверный логин!!')
      
a = None
while True:
    a = input('Вход или регистрация?')
    if a == 'вход':
        enter_sys()
        break
    elif a == 'регистрация':
        register()
        break
    else:
        print('???')
        continue