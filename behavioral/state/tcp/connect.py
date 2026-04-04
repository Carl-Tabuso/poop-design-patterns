from TCPConnection import TCPConnection

if __name__ == "__main__":
    conn = TCPConnection()
    
    print(f"Before opening, connection is {conn.get_state()}")
    conn.open()
    print(f"After opening, connection is {conn.get_state()}",)
