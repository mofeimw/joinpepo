import sqlite3

"""
Debug utility to dump all entries in score_submissions table, including course.
Run this script from the project root:
    python dump_score_submissions.py
"""

def dump_score_submissions(db_path='pepo.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Select id, email, phone, course, created_at
    cursor.execute('SELECT id, email, phone, course, created_at FROM score_submissions')
    rows = cursor.fetchall()

    # Print header
    header = ('ID', 'Email', 'Phone', 'Course', 'Created_at')
    print(f"{header[0]:<5} {header[1]:<25} {header[2]:<15} {header[3]:<15} {header[4]}")
    print('-' * 90)

    # Print rows
    for id_, email, phone, course, created_at in rows:
        print(f"{id_:<5} {email or '':<25} {phone or '':<15} {course or '':<15} {created_at}")

    conn.close()

if __name__ == '__main__':
    dump_score_submissions()
