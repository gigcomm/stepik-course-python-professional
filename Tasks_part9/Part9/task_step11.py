from functools import partial


def send_email(name, email_address, text):
    pass

to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
invitation_text =  "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут...."
send_an_invitation = partial(send_email, text=invitation_text)
