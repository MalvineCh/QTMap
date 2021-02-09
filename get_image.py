import requests
import sys


def getImage(self):
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    self.map_file = "map.png"
    with open(self.map_file, "wb") as file:
        file.write(response.content)
    return self.map_file
