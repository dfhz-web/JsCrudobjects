#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


client_id = 'e63ae6833e6c2e6211a9'
client_secret = 'ac32718f2cffb066f503441f42c2f32b04a98a42'

# https://github.com/login/oauth/authorize?client_id=e63ae6833e6c2e6211a9&scope=respo

code = '12913d1189e270ea3534'
access_token = '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' #I can obtain his username,avaatar, biografia, reposito, imagen, correo electro,etc
#2 hours of use access token (real life) just github does not expire


if __name__ == '__main__':
   url = 'https://api.github.com/user/repos'  #we can send the  access token within the headers or url , but preferable, go a head within headers based exp
   headers = { 'Authorization' : 'token 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' }

   response = requests.get(url, headers=headers)

   if response.status_code == 200:
      payload = response.json()

      for project in payload:
         name = [project['name']]
         print('name')
   else:
      print(response.content)