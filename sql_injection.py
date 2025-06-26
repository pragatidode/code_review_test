import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # VULNERABLE CODE:  Building SQL query with string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
    else:
        print("Login failed.")

# Attacker's crafted input
malicious_username = "' OR '1'='1"
malicious_password = ""

login(malicious_username, malicious_password)