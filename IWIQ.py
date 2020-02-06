#IWIQ BANK
import pickle

print("__________________________")
print("|                        |")
print("| IWIQ Bank 0.2.2 Client |")
print("|________________________|")

try:
    filer = open("IWIQ.files", "rb")
    users = pickle.load(filer)
    filer.close()
except:
    filew = open("IWIQ.files", "wb")
    users = {}
    pickle.dump(users, filew)
    filew.close()
user = input("Введите ваш логин: ")
if user in users:
    print("Привет,", user, "!")
    password = input("Введите ваш пароль: ")
    if password == users[user][0]:
        print("Ура! Пароль правильный!")
        correct = True
    else:
        print("Ой-ой! Пароль не правильный!")
        correct = False
else:
    password = input("О нет! Вы не зарегестрированы! Какой будет пароль вашего нового аккаунта: ")
    users[user] = [password, 100]
    filew = open("IWIQ.files", "wb")
    pickle.dump(users, filew)
    filew.close()
    print("Добро пожаловать в IWIQ, ", user, "!")
    print("Внимание! Бонус! Вам 100р за регистрацию!")
    correct = True
if correct:
    while True:
        print("""Чем могу помочь?:
_________________________________________
|          IWIQ BANK 0.2.2              |
|                                       |
|    e. Выйти                           |
|    0. Сменить пароль                  |
|    1. Просмотреть баланс              |
|    2. Пополнить счёт                  |
|    3. Перевести по номеру карты       |
|    4. Перевести пользователю IWIQ     |
|    5. Оплатить [Ранний доступ]        |
|_______________________________________|""")
        f = input('> ')
        if f == "e":
            filew = open("IWIQ.files", "wb")
            pickle.dump(users, filew)
            filew.close()
            print('Спасибо, что пользуешься IWIQ! Пока!')
            break
        elif f == "0":
            print('Подсказка: '+'*'*(len(users[user][0])-2)+users[user][0][len(users[user][0])-2:])
            old_pass = input('Введите старый пароль: ')
            if old_pass == users[user][0]:
                new_pass = input('Введите новый пароль: ')
                users[user][0] = new_pass
                filew = open("IWIQ.files", "wb")
                pickle.dump(users, filew)
                filew.close()
            else:
                print("Ой! Ошибка")
        elif f == "1":
            print("Твой баланс:", users[user][1], "рублей")
        elif f == "2":
            n = input('Введите сумму: ')
            users[user] = [password, users[user][1]+int(n)]
            filew = open("IWIQ.files", "wb")
            pickle.dump(users, filew)
            filew.close()
            print("Твой баланс:", users[user][1], "рублей")
        elif f == "3":
            n = input('Введите сумму: ')
            if n.isdigit():
                input('Введите номер карты: ')
                if int(n) < int(users[user][1]):
                    users[user] = [password, users[user][1]-int(n)]
                else:
                    print("Необходимо чтобы остался хотя бы 1 рубль")
                filew = open("IWIQ.files", "wb")
                pickle.dump(users, filew)
                filew.close()
                print("Твой баланс:", users[user][1], "рублей")
            else:
                print('Ой! Ошибка!')
        elif f == "4":
            n = input('Введите сумму: ')
            if n.isdigit():
                name = input('Введите имя пользователя IWIQ: ')
                if int(n) < int(users[user][1]) and name in users:
                    users[user][1] = users[user][1]-int(n)
                    users[name][1] = users[name][1]+int(n)
                else:
                    print("Ой! Ошибка!")
                filew = open("IWIQ.files", "wb")
                pickle.dump(users, filew)
                filew.close()
            else:
                print('Ой! Ошибка!')
        elif f == '5':
            n = input('Введите сумму: ')
            if n.isdigit():
                input('Введите ИНН: ')
                input('Введите цель платежа:')
                if int(n) < int(users[user][1]):
                    users[user] = [password, users[user][1]-int(n)]
                else:
                    print("Необходимо чтобы остался хотя бы 1 рубль")
                filew = open("IWIQ.files", "wb")
                pickle.dump(users, filew)
                filew.close()
                print("Ваш баланс:", users[user][1], "рублей")
        else:
            print('Ой! Ошибка!')
else:
    print("Вход в аккаунт отклонён")
