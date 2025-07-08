import sqlite3

def dump_start_info(db_path='pepo.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, created_at FROM start_info')
    rows = cursor.fetchall()

    # Print header
    header = ('ID', 'Name', 'Email', 'Created_at')
    print(f"{header[0]:<5} {header[1]:<30} {header[2]:<15} {header[3]}")
    print('-' * 70)

    # Print rows
    for row in rows:
        id_, name, email, created_at = row
        print(f"{id_:<5} {name or '':<30} {email or '':<15} {created_at}")

    conn.close()

if __name__ == '__main__':
    dump_start_info()
