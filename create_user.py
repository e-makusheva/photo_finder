from getpass import getpass
import sys

from photo_app import create_app
from photo_app.modules import User, db

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    email = input('Введите email: ')
    if User.query.filter(User.email == email).count():
        print('Такой пользователь уже существует')
        sys.exit(0)


    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')

    if not password == password2:
        print('Пароли не совпадают')
        sys.exit(0)

    new_user = User(username=username, email=email, roles='1')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))
