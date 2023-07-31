import requests

if __name__ == '__main__':
    client_id = 'e63ae6833e6c2e6211a9'
    client_secret = 'ac32718f2cffb066f503441f42c2f32b04a98a42'
    code = '18193d339280d814149c'
    access_token = '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'

    url = 'https://api.github.com/user/repos'
    payload = {'name' : 'git_api_cf_comunidad'}
    headers = {'Accept':'application/json', 'Authorization': 'token' + access_token}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)


#https://github.com/login/oauth/authorize?client_id=e63ae6833e6c2e6211a9&scope=repo