# https://snyk.io/blog/code-injection-python-prevention-examples/
# Exploit of user entered input
import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()
user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
cur.execute(query)
conn.close()

# Insecure use of eval() and related functions
user_input = input("Enter expression: ")
result = eval(user_input)  # Unsafe

# Lack of input validation and sanitization
user_input = input("Enter filename: ")
with open(user_input, 'r') as file:  # Vulnerable to directory traversal
    content = file.read()

# Risks associated with dynamic code construction
import os

directory = input("Enter the directory to list: ")
command = f"ls {directory}"  # Vulnerable to Command Injection
os.system(command)

# Insecure deserialization
import pickle
serialized_data = input("Enter serialized data: ")
deserialized_data = pickle.loads(serialized_data.encode('latin1'))  # Unsafe deserialization

# Safeguard user-controlled inputs
ALLOWED_COMMANDS = ["start", "stop", "restart"]
user_input = input("Enter your command: ")
if user_input in ALLOWED_COMMANDS:
    exec(user_input)
else:
    print("Invalid command.")