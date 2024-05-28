import requests

def get(ip):
    api_url = f"https://api.mcsrvstat.us/2/{ip}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get('online'):
            print(f"Сервер {ip} онлайн")
            print(f"Онлайн игроков: {data['players']['online']}/{data['players']['max']}")
            print(f"Версия: {data['version']}")
            print(f"Мотд: {data['motd']['clean']}")
        else:
            print(f"Сервер {ip} недоступен")
    else:
        print(f"Не удалось получить данные о сервере. Код ошибки: {response.status_code}")

ip = input("Введите IP сервера: ")
get(ip)