from Database import Database
    
if __name__ == '__main__':

    db1 = Database()
    db1.set_connection('SQLite')
    print("db1:", db1.get_connection())

    db2 = Database()
    db2.set_connection('MYSQL')
    print("db2:", db2.get_connection())
    
    print("\n")

    print("Memory address:")
    print(f"db1: {id(db1)}")
    print(f"db2: {id(db2)}")

    print("\n")    

    res = db1.query("SELECT * FROM table;")
    print(res)
