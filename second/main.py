import requests


def get_pokemons(url='https://pokeapi.co/api/v2/generation/3/', offset=0):
                 
    args= {'offset' : offset} if offset else {}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:

        payload = response.json()
        results = payload.get('abilities',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)


        next = input("Keep going? [Y/N]")
        if next =='y':
            get_pokemons(offset=offset+5)




if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/generation/3/'
    get_pokemons()

   
   

