import sqlite3

def dump_users(db_path='pepo.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT parent_name, email, created_at FROM users')
    rows = cursor.fetchall()

    # Print header
    header = ('Parent Name', 'Email', 'Created At')
    print(f"{header[0]:<30} {header[1]:<30} {header[2]}")
    print('-' * 80)

    # Print rows
    for parent_name, email, created_at in rows:
        print(f"{parent_name:<30} {email:<30} {created_at}")

    conn.close()

if __name__ == '__main__':
    dump_users()

