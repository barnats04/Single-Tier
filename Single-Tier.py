import sqlite3

def execute_query(query, params=()):
    with sqlite3.connect("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()


def main():
    execute_query("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
    while True:
        choice = input("1.Add 2.View 3.Delete 4.Exit: ")
        if choice == "1":
            execute_query("INSERT INTO notes (content) VALUES (?)", (input("Note: "),))
        elif choice == "2":
            print("\n".join(f"{n[0]}: {n[1]}" for n in execute_query("SELECT * FROM notes")))
        elif choice == "3":
            execute_query("DELETE FROM notes WHERE id=?", (input("ID: "),))
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
