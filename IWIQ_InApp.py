import IWIQ_server
def pay(bill, payee, licence):
    bill = str(bill)
    if bill.isdigit():
        lic_list = ['35', '48', '78', '10']
        print('IWIQ InApp [Demo]')
        if str(licence).isdigit():
            if len(str(licence))==8:
                if int(str(licence)[:6]) % 2==0:
                    if str(licence)[6:] in lic_list:
                        print('Ключ полностью безопасен')
                        save = 100
                    else:
                        print('Ключ безопасный')
                        save = 75
                else:
                    print('Ключ проверен')
                    save = 50
            else:
                print('Ключ не проверен')
                save = 25
        else:
            print('Ключ опасен')
            save = 0
        if save!=0:
            print('Оплата')
            print('Получатель: ', str(payee))
            print('Сумма: ', str(bill))
            print('Безопастность получателя: ', str(save), '%')
            users = IWIQ_server.IWIQ_get()
            user = input('Введите пользователя: ')
            if user in users:
                password = input('Введите пароль: ')
                if int(bill) < int(users[user][1]) and password == users[user][0]:
                    users[user] = [password, users[user][1] - int(bill)]
                    print('Готово! Ваш баланс: ',str(users[user][1]))
                    done = True
                    IWIQ_server.IWIQ_update(users)
                else:
                    print("Ошибка!")
                    done = False
            else:
                print("Ошибка!")
                done = False
            return done
        else:
            return False
    else:
        return False
    input()

def donate(payee, licence):
    lic_list = ['35', '48', '78', '10']
    print('IWIQ InApp [Demo]')
    if str(licence).isdigit():
        if len(str(licence))==8:
            if int(str(licence)[:6]) % 2==0:
                if str(licence)[6:] in lic_list:
                    print('Ключ полностью безопасен')
                    save = 100
                else:
                    print('Ключ безопасный')
                    save = 75
            else:
                print('Ключ проверен')
                save = 50
        else:
            print('Ключ не проверен')
            save = 25
    else:
        print('Ключ опасен')
        save = 0
    if save!=0:
        print('Донат')
        print('Проект: ', str(payee))
        print('Безопастность получателя: ', str(save), '%')
        bill = input('Введите сумму: ')
        if bill.isdigit():
            users = IWIQ_server.IWIQ_get()
            user = input('Введите пользователя: ')
            if user in users:
                password = input('Введите пароль: ')
                if int(bill) < int(users[user][1]) and password == users[user][0]:
                    users[user] = [password, users[user][1] - int(bill)]
                    print('Готово! Ваш баланс: ',str(users[user][1]))
                    done = True
                    IWIQ_server.IWIQ_update(users)
                else:
                    print("Ошибка!")
                    done = False
            else:
                print("Ошибка!")
                done = False
        else:
            print("Ошибка!")
            done = False
        return done
    else:
        return False
    input()
