import mysql.connector as mcon


def database_connection():
    conn = mcon.connect(host="127.0.0.1", user="steve", password="sijui!", database="SpringJDBC")

    cursor = conn.cursor()

    cursor.execute("show tables")

    data = cursor.fetchall()

    print(f"output : {data}")

    cursor.execute("select * from StudentLogin")

    data = cursor.fetchall()

    print(f"output : {data}")

    conn.close()


if __name__ == "__main__":
    database_connection()
