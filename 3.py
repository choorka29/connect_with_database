# 1. Классы исключений:

# ```python
class FirstException(BaseException):
        pass

class SecondException(BaseException):
        pass
class ThirdException(BaseException):
        pass
  

# 2. Класс `Database` имеет три метода для работы с базой данных:
# - `connect` - метод для установления соединения с базой данных;
# - `query` - метод для выполнения запроса к базе данных;
# - `disconnect` - метод для закрытия соединения с базой данных.

# При возникновении ошибок или нестандартного поведения методы выбрасывают соответствующие исключения:

# ```python
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def connect(self):
        if not self.db_name:
            raise FirstException("Отсутствует имя базы данных!")
        if self.connected:
            raise SecondException("Соединение уже установлено!")
        # код для установления соединения
        self.connected = True

    def query(self, sql):
        if not self.connected:
            raise ThirdException("Соединение с базой данных не установлено!")
        # код для выполнения запроса
        pass

    def disconnect(self):
        if not self.connected:
            raise ThirdException("Соединение с базой данных не установлено!")
        # код для закрытия соединения
        self.connected = False


# 3. Класс `DatabaseManager` имеет методы для работы с объектами класса `Database` и обработки исключений:

# ```python
class DatabaseManager:
    def __init__(self):
        self.databases = []

    def add_database(self, database):
        try:
            database.connect()
        except FirstException as e:
            print(f"Ошибка: {e}")
        except SecondException as e:
            print(f"Ошибка: {e}")
        else:
            self.databases.append(database)
            print(f"Соединение с базой данных {database.db_name} установлено")

    def remove_database(self, database):
        try:
            database.disconnect()
        except ThirdException as e:
            print(f"Ошибка: {e}")
        else:
            self.databases.remove(database)
            print(f"Соединение с базой данных {database.db_name} разорвано")

if __name__ == '__main__':
    db1 = Database("test_db")
    db2 = Database("")
    manager = DatabaseManager()

    manager.add_database(db1)
    manager.add_database(db2)
    # Output:
    # Соединение с базой данных test_db установлено
    # Ошибка: Отсутствует имя базы данных!

    manager.remove_database(db1)
    manager.remove_database(db2)
    # Output:
    # Соединение с базой данных test_db разорвано
    # Ошибка: Соединение с базой данных не установлено!
