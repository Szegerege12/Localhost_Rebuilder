from flask import request
from flask_restx import Api, Resource, reqparse
import requests

code_parse = reqparse.RequestParser()
code_parse.add_argument('code')

class Github(Resource):
  def post(self):
    CLIENT_ID = '423ce2815e11fd57096f'
    CLIENT_SECRET = '8230d43e5b914aaffe9ae5daf53aa517560908de'
    args = code_parse.parse_args()
    code = args['code']

    url=  f'https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code}'

    r = requests.post(url = url)
    response = r.text.replace('%3A',':')
    data = dict(item.split("=") for item in response.split("&"))
    print(data)
    credentials  = requests.get(f'https://api.github.com/user?access_token={data["access_token"]}&scope={data["scope"]}&token_type=${data["token_type"]}')
    creds = credentials.json()

    return creds, 200, {'Access-Control-Allow-Credentials': 'true'}