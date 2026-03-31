# ===============================
# TASK 1 - FILE WRITE
# ===============================

with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables\n")
    f.write("Topic 2: Lists\n")
    print("File written")

with open("python_notes.txt", "a") as f:
    f.write("\nExtra line")
    print("Appended")

# read
with open("python_notes.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    print(i+1, lines[i].strip())

# ===============================
# TASK 2 - API
# ===============================
import requests

try:
    res = requests.get("https://dummyjson.com/products?limit=5")
    data = res.json()

    for p in data["products"]:
        print(p["title"], p["price"])

except Exception as e:
    print("Error:", e)

# ===============================
# TASK 3 - EXCEPTION
# ===============================

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Invalid input"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# ===============================
# TASK 4 - LOGGING
# ===============================
from datetime import datetime

def log_error(msg):
    with open("error_log.txt", "a") as f:
        f.write(str(datetime.now()) + " - " + msg + "\n")

try:
    x = 10 / 0
except:
    log_error("Division error")

print("Check error_log.txt")