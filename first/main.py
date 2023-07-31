import requests
import json

if __name__ == '__main__':
    url = 'https://i.imgur.com/RyT5qcj.jpeg'

    response = requests.get(url, stream=True) #realiza la peticion sin descargar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)

    response.close()