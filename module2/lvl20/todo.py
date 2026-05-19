import os
from dataclasses import dataclass

import psycopg
from psycopg import Connection
from psycopg.rows import dict_row


from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI", None)

if not DB_URI:
    raise ValueError("DB_URI environment variable is not set")
    


def create_tables(conn: Connection):
    # Tasks table
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                is_done BOOLEAN DEFAULT FALSE
            )
        """)


def add_task(conn: Connection, title: str) -> None:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO tasks (title) VALUES (%s)",
                    (title, ))
        conn.commit()
        
        
def complete_task(conn: Connection, task_id: int) -> None:
    with conn.cursor() as cur:
        cur.execute("UPDATE tasks SET is_done = True WHERE id = %s",
                    (task_id, ))
        conn.commit()


def list_tasks(conn: Connection) -> None:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tasks ORDER BY id")

        print("\n==== ТАСКИ ====")
        for task in cur:
            status = '✅' if task['is_done'] else ''
            print(f"{task['id']}. {status} {task['title']}")


def delete_tasks(conn: Connection, task_id: int) -> None:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM tasks WHERE id = %s",
                    (task_id, ))
        conn.commit()
        

def show_menu():
    print("==== TODO LIST ====")
    print("1. Додати задачу")
    print("2. Позначити як виконану")
    print("3. Переглянути всі задачі")
    print("4. Видалити задачу")
    print("0. Вийти")


def main():
    with psycopg.connect(DB_URI, row_factory=dict_row) as conn:
        create_tables(conn)
        
        while True:
            show_menu()
            choice = input().strip()

            if choice == "1":
                task_title = input("Введи назву: ")
                add_task(conn, task_title)
                print("Задачу добавлено!\n")
                
            elif choice == "2":
                list_tasks(conn)
                n = input("Оберіть задачу: ").strip()

                if n.isdigit():
                    complete_task(conn, n)
                    print("Позначено виконаним!")

            elif choice == "3":
                list_tasks(conn)

            elif choice == "4":
                list_tasks(conn)
                n = input("Оберіть задачу: ").strip()

                if n.isdigit():
                    delete_tasks(conn, n)
                    print("Видалено!")

            elif choice == "0":
                print("Bye!")
                exit(0)

            input()


if __name__ == "__main__":
    main()