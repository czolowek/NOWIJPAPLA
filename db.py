import sqlite3


def create_db(name_db: str):
    try:
        sql_con = sqlite3.connect(name_db)
        cursor = sql_con.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            last_name VARCHAR(200),
            rost REAL
        );
        """
        print("Запит успішно сформовано")
        cursor.execute(query)
        sql_con.commit()
        print("Таблиця успішно створена")

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("З'єднання з базою даних успішно завершене")


def add_pizza(name, ingredients, price):
    try:
        sql_con = sqlite3.connect("my_first.db")
        cursor = sql_con.cursor()

        query = """
        INSERT INTO Students (name, last_name, rost) VALUES (?, ?, ?)
        """

        cursor.execute(query, (name, ingredients, price))
        sql_con.commit()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print("Помилка: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("Підключення успішно завершене")


def get_pizzas():
    try:
        sql_con = sqlite3.connect("my_first.db")
        cursor = sql_con.cursor()

        query = """
        SELECT * FROM Students;
        """

        return cursor.execute(query).fetchall()

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()


create_db("my_first.db")

# add_pizzas("Перша піца", "помідор, сир", 50)
# add_pizzas("Друга піца", "перець, сир", 60)
# add_pizzas("Класична", "гриби, перець, сир", 60)