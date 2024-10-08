class User:
    def __init__(self, user_id: int, user_name: str, access: str = 'user') -> None:
        self._user_id = user_id
        self._user_name = user_name
        self._access = access

        if access == 'user':
            print(f'Создан новый пользователь: {self._user_name}')
        else:
            print(f'Создан новый администратор: {self._user_name}')

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._user_name

    @property
    def access(self) -> str:
        return self._access


class Admin(User):
    def __init__(self, user_id: int, user_name: str) -> None:
        super().__init__(user_id, user_name, access='admin')
        self.__user_list: list[User] = []

    def add_user(self, one_user) -> None:
        if isinstance(one_user, User):
            self.__user_list.append(one_user)
            print(f'Пользователь {one_user.name} добавлен')
        else:
            print('Ошибка: можно добавлять только объекты класса User')

    def remove_user(self, user_id) -> None:
        for item in self.__user_list:
            if item.user_id == user_id:
                removed_name: str = item.name
                self.__user_list.remove(item)
                print(f'Пользователь {removed_name} удалён')
                return
        print('Пользователь с таким ID не найден')

    @property
    def user_list(self) -> list[User]:
        return self.__user_list


print('Создаю двух пользователей')
user_1 = User(1, 'Евгений')
user_2 = User(2, 'Екатерина')

print('\nСоздаю администратора')
admin = Admin(0, 'Макар')

print('\nДобавляю пользователей в список')
admin.add_user(user_1)
admin.add_user(user_2)

print('\nВывожу список пользователей')
for elem in admin.user_list:
    print(f'Идентификатор пользователя: {elem.user_id}, Имя: {elem.name}, Уровень доступа: {elem.access}')

print('\nУдаляю пользователя')
admin.remove_user(1)

print('\nВывожу список пользователей')
for elem in admin.user_list:
    print(f'Идентификатор пользователя: {elem.user_id}, Имя: {elem.name}, Уровень доступа: {elem.access}')