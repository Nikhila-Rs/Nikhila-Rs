import sqlite3
import logging
import random

logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def initialize_databases():
    """Initialize databases for admin and user data."""
    with sqlite3.connect("admin_database.db") as admin_conn:
        admin_cursor = admin_conn.cursor()
        admin_cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_data (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            sensitive_info TEXT NOT NULL
        )
        ''')
        admin_cursor.executemany('''
        INSERT INTO admin_data (username, password, sensitive_info)
        VALUES (?, ?, ?)
        ''', [
            ("admin", "admin123", "Confidential Report A"),
            ("admin", "admin123", "Sensitive Data B"),
        ])
        admin_conn.commit()

    with sqlite3.connect("user_database.db") as user_conn:
        user_cursor = user_conn.cursor()
        user_cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            info TEXT
        )
        ''')
        user_conn.commit()

def log_activity(message):
    """Log activity to a file."""
    logging.info(message)

def validate_input(input_string):
    """Basic validation to prevent SQL injection."""
    suspicious_patterns = ["--", ";", "/*", "*/", "DROP", "UNION", "SELECT", "OR", "AND", "="]
    for pattern in suspicious_patterns:
        if pattern in input_string.upper():
            return False
    return True

def random_detection():
    """Random detection mechanism for anomalies."""
    if random.choice([True, False]):
        alert = "Random Detection Alert! Potential security breach detected."
        print(alert)
        log_activity(alert)

def authenticate(username, password):
    """Authenticate users as admin or regular users."""
    if username == "admin" and password == "admin123":
        return "admin"
    with sqlite3.connect("user_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_data WHERE username = ? AND password = ?", (username, password))
        if cursor.fetchone():
            return "user"
    return None

def admin_dashboard():
    """Admin dashboard for managing sensitive data."""
    print("\n--- Admin Dashboard ---")
    while True:
        print("\n1. Check for Data Leakage")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            random_detection()
            username = input("Enter a username to check in admin database: ")
            detect_data_leakage("admin_database.db", "admin_data", username)
        elif choice == "2":
            print("Logging out of Admin Dashboard.")
            break
        else:
            print("Invalid choice. Please try again.")

def detect_data_leakage(database, table, user_input):
    """Detect data leakage attempts."""
    if not validate_input(user_input):
        print("Invalid input detected! Potential SQL Injection attempt.")
        log_activity(f"SQL Injection attempt: {user_input}")
        return

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table} WHERE username = ?", (user_input,))
            results = cursor.fetchall()
            if len(results) > 1:
                print("Data Leakage Detected!")
                log_activity(f"Data Leakage Detected for input: {user_input}")
            else:
                print("No data leakage detected.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            log_activity(f"Database error: {e}")

def user_dashboard(username):
    """User dashboard for managing personal data."""
    print(f"\n--- User Dashboard for {username} ---")
    while True:
        print("\n1. Add Data")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user_data(username)
        elif choice == "2":
            print("Logging out of User Dashboard.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_user_data(username):
    """Allow users to add personal data."""
    with sqlite3.connect("user_database.db") as conn:
        cursor = conn.cursor()
        info = input("Enter the information to store: ")
        if not validate_input(info):
            print("Invalid data! Potentially malicious content.")
            log_activity(f"Invalid data attempt by user {username}: {info}")
            return
        try:
            cursor.execute("UPDATE user_data SET info = ? WHERE username = ?", (info, username))
            conn.commit()
            print("Data added successfully.")
        except sqlite3.Error as e:
            print(f"Error updating data: {e}")
            log_activity(f"Error updating data for user {username}: {e}")

def register_new_user():
    """Register a new user."""
    print("\n--- Register New User ---")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    if not validate_input(username) or not validate_input(password):
        print("Invalid username or password. Registration failed.")
        log_activity(f"Invalid registration attempt: {username}")
        return

    with sqlite3.connect("user_database.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO user_data (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try another.")
        except sqlite3.Error as e:
            print(f"Registration error: {e}")
            log_activity(f"Registration error for {username}: {e}")

def main():
    initialize_databases()
    print("Databases initialized.")
    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_type = authenticate(username, password)
            if user_type == "admin":
                admin_dashboard()
            elif user_type == "user":
                user_dashboard(username)
            else:
                print("Invalid credentials.")
        elif choice == "2":
            register_new_user()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
