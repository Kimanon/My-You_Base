import requests
import os

def get_ip_details(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return (f"Страна: {data['country']}\n"
                        f"Город: {data['city']}\n"
                        f"Широта: {data['lat']}\n"
                        f"Долгота: {data['lon']}\n"
                        f"Организация: {data.get('org', 'Неизвестно')}\n"
                        f"Прокси/VPN: {'Да' if data.get('proxy', False) else 'Нет'}")
            else:
                return f"Не удалось найти данные для IP {ip_address}."
        else:
            return f"Ошибка: Не удалось подключиться к API (код {response.status_code})."
    except Exception as e:
        return f"Произошла ошибка: {e}"

if __name__ == "__main__":
    print("=" * 40)
    print("      Определение информации по IP")
    print("=" * 40)
    ip_address = input("Введите IP-адрес: ")
    print("-" * 40)
    print(get_ip_details(ip_address))
    print("-" * 40)
    print("Нажмите любую клавишу для завершения...")
    os.system("pause")
