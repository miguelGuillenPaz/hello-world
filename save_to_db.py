import sqlite3
import sys


def save_message(db_path, message):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)"
    )
    cur.execute("INSERT INTO messages (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = input("Ingrese el mensaje a guardar: ")
    save_message("data.db", msg)
    print("Mensaje guardado en la base de datos.")
