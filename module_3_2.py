def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if ".com" not in recipient[-4:]:
        if ".ru" not in recipient[-4:]:
            if ".net" not in recipient[-4:]:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if ".net" not in sender[-4:]:
        if ".ru" not in sender[-4:]:
            if ".com" not in sender[-4:]:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                if sender != "university.help@gmail.com":
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        print("Нельзя отправить письмо самому себе")

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email("Вы видите это сообщение, как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email("Пожалуйста исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")