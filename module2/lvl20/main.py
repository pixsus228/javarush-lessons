import os

import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()


with psycopg.connect(os.getenv("DB_URI"), row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        cur.execute((
            "SELECT * FROM actor"
            " ORDER BY first_name"
        ))

        actors = cur.fetchall()

        for actor in actors:
            print(actor)


# SQL Injection приклад:

# SELECT FROM users IF login = '' OR 1=1; --' AND password = '{password}';
# ' OR 1=1; --


# with psycopg.connect(os.getenv("DB_URI")) as conn:
#     with conn.cursor() as cur:
#         name = input("Enter name: ")

#         cur.execute((
#             "SELECT * FROM actor"
#             " WHERE first_name ILIKE %s"
#             " LIMIT 4"
#         ), (f"%{name}%", ))

#         print(cur.fetchone())
#         print(cur.fetchall())
#         print(cur.fetchone())


# with psycopg.connect(os.getenv("DB_URI")) as conn:
#     with conn.cursor() as cur:
#         try:
#             cur.execute("DELETE FROM payment WHERE payment_id = %s", (3, ))
#             cur.execute("DELETE FROM payment WHERE payment_id = %s", (200000, ))

#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             print("Error occurred, transaction rolled back", e)


# import asyncio

# if os.name == "nt":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


# async def main():
#     db_uri = os.getenv("DB_URI")
#     async with await psycopg.AsyncConnection.connect(db_uri) as aconn:
#         async with aconn.cursor() as acur:
#             await acur.execute("SELECT pg_sleep(2);")
#             result = await acur.fetchone()
#             print("Запит виконано асинхронно!")

# if __name__ == "__main__":
#     asyncio.run(main())