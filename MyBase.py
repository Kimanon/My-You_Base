import socket
import requests
import os
import platform
import uuid
import dns.resolver

# Проверка подключения к интернету
def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Получение локального IP
def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Получение публичного IP
def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json()["ip"]
    except requests.ConnectionError:
        return "Не удалось определить публичный IP."

# Получение имени хоста
def get_hostname():
    return socket.gethostname()

# Получение MAC-адреса
def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(f'{(mac >> 8*i) & 0xff:02x}' for i in reversed(range(6)))

# Получение информации об ОС
def get_os_info():
    return f"{platform.system()} {platform.release()}"

# Получение геолокации по IP
def get_geo_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return (f"Страна: {data['country']}\n"
                f"Город: {data['city']}\n"
                f"Широта: {data['lat']}\n"
                f"Долгота: {data['lon']}")
    except Exception:
        return "Не удалось определить геолокацию."

# Проверка DNS-серверов
def get_dns_servers():
    try:
        resolvers = dns.resolver.Resolver().nameservers
        return resolvers
    except Exception as e:
        return f"Ошибка получения DNS-серверов: {e}"

if __name__ == "__main__":
    print("="*40)
    print("       Информация о системе")
    print("="*40)
    
    if check_internet_connection():
        print("\nПодключение к интернету: активно")
        print("-"*40)

        # Основные функции
        print("Публичный IP:       ", get_public_ip())
        print("Локальный IP:       ", get_local_ip())
        print("Имя хоста:          ", get_hostname())
        print("MAC-адрес:          ", get_mac_address())
        print("Операционная система:", get_os_info())

        print("-"*40)
        print("Геолокация по IP:")
        print(get_geo_location())

        print("-"*40)
        print("DNS-серверы:")
        dns_servers = get_dns_servers()
        if isinstance(dns_servers, list):
            for dns_server in dns_servers:
                print(f"   • {dns_server}")
        else:
            print(dns_servers)  # В случае ошибки
    else:
        print("\nПодключение к интернету отсутствует")
    
    print("="*40)
    os.system("pause")
