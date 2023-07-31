import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
  
    payload = { 'name': 'Daniel', 'last name':'Herrera', 'life': 'being desired'}
    headers = {'Conten-Type' : 'application/json', 'access-token':'12255'}

    #response = requests.post(url, json=payload)  # json=payload includes headers already
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)


    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #Dic
        #print(headers_response)
        server = headers_response['Server']
        print(server)

    