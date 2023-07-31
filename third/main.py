#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


client_id = 'e63ae6833e6c2e6211a9'
client_secret = 'ac32718f2cffb066f503441f42c2f32b04a98a42'

# https://github.com/login/oauth/authorize?client_id=e63ae6833e6c2e6211a9&scope=respo

code = '58d761f660393fe4cc38'
access_token = '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' #I can obtain his username,avaatar, biografia, reposito, etc
#2 hours of use access token (real life) just github does not expire


if __name__ == '__main__':
     url = 'https://github.com/login/oauth/access_token'
     payload = {'client_id' : client_id, 'client_secret': client_secret, 'code': code}
     headers = {'Accept' : 'application/json'}

     response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
     response_json = response.json()    
     access_token = response_json['access_token']
     print(access_token)



   