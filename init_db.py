import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    
    # Create Client table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS client (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        account_type TEXT NOT NULL,
        password TEXT NOT NULL,
        phone INTEGER,
        address_line TEXT,
        address_line2 TEXT,
        city TEXT,
        pincode INTEGER 
    );
    ''')

    # Create Advocate table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS advocate (
        adv_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        account_type TEXT NOT NULL,
        password TEXT NOT NULL,
        phone INTEGER,
        address_line TEXT,
        address_line2 TEXT,
        city TEXT,
        pincode INTEGER,
        specialization TEXT 
    );
    ''')
    # Only create the table if it doesn't already exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS lawyers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            district TEXT,
            legal_area_focus TEXT,
            description TEXT,
            past_cases TEXT,
            photo BLOB
        );
    ''')
    



    # Create Cases table with Foreign Keys
    conn.execute('''
    CREATE TABLE IF NOT EXISTS cases (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_title TEXT NOT NULL,
        case_description TEXT,
        case_status TEXT NOT NULL,
        case_outcome TEXT NOT NULL,
        case_adv INTEGER,
        case_client INTEGER,
        FOREIGN KEY(case_adv) REFERENCES advocate(adv_id),
        FOREIGN KEY(case_client) REFERENCES client(client_id)
    );
    ''')

    # In init_db.py
    conn.execute('''
    CREATE TABLE IF NOT EXISTS client_posts (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        case_title TEXT NOT NULL,
        case_description TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(client_id) REFERENCES client(client_id)
    );
    ''')
    

    try:
        conn.execute('ALTER TABLE client_posts ADD COLUMN reply_text TEXT')
        print("Added 'reply_text' column to 'client_posts' table.")
    except sqlite3.OperationalError:
        print("'reply_text' column already exists in 'client_posts' table.")
    try:
        conn.execute('''
        ALTER TABLE advocate ADD COLUMN approved BOOLEAN DEFAULT 0''')
    except sqlite3.OperationalError:
        print("colum approved already exist")

    try:
        conn.execute('''
        ALTER TABLE advocate ADD COLUMN declined INTEGER DEFAULT 0;''')
    except sqlite3.OperationalError:
        print("colum decline already exist")

    

    conn.commit()
    conn.close()

init_db()