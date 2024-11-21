import psycopg2

def create_table_users(conn):
    cur = conn.cursor()
    create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """
    cur.execute(create_table)
    conn.commit()
    cur.close()
    print("Таблица пользователей создана")

def insert_table_users(conn):
    cur = conn.cursor()
    insert_table = """
    INSERT INTO users (email, password)
    VALUES ('anton-ivanov-080203@mail.ru', '4682671')
    """
    cur.execute(insert_table)
    conn.commit()
    cur.close()
    print("Пользователи были добавлены")

if __name__ == "__main__":
    conn = psycopg2.connect("host=83.166.232.148 dbname=PostgreSQL-accounts user=user password=AincOlGon4682671!")
    print("Соединение с базой установленно")
    create_table_users(conn)
    #insert_table_users(conn)
    conn.close()
    print("Соединение с базой разорвано")