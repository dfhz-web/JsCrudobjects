import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    #  url = 'https://httpbin.org/get?name=Daniel&lastname=Herrera&life=successfull'
    args = { 'name': 'Daniel', 'last name':'Herrera', 'life': 'being desired'}

    response = requests.get(url, params=args)
    print(response.url)


    if response.status_code == 200:


        #DICCIONARIO
        # response_json = response.json()  
        # origin = response_json["headers"]
        # print(origin)


        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)

        # content = response.content
        # print(content)

        # file = open('google.html', 'wb')
        # file.write(content)
        # file.close()



    