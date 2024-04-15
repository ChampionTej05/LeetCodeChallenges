import sqlite3

try:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    # ... perform some SQL operations ...

    conn.commit()
except sqlite3.IntegrityError:
    print("Integrity Error occurred")
    conn.rollback()
except sqlite3.DataError:
    print("Data Error occurred")
    conn.rollback()
except sqlite3.ProgrammingError:
    print("Programming Error occurred")
    conn.rollback()
except sqlite3.OperationalError:
    print("Operational Error occurred")
    conn.rollback()
except sqlite3.NotSupportedError:
    print("Not Supported operation attempted")
    conn.rollback()
except sqlite3.DatabaseError:
    print("Generic Database Error occurred")
    conn.rollback()
except sqlite3.Error:
    print("General SQLite Error occurred")
    conn.rollback()
except Exception as e:
    print(f"Non-SQLite error occurred: {e}")
    conn.rollback()
finally:
    conn.close()
