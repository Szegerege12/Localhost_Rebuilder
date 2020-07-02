import os, json, sys
import subprocess
from subprocess import PIPE, STDOUT
import shutil
from flask import Flask
from flask import request
from flask_mail import Mail, Message
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS
import hashlib
import requests
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.auth import jwt


from resources.github import Github
from resources.google import Google


SCOPES = ['https://www.googleapis.com/auth/calendar.events','https://www.googleapis.com/auth/calendar']
#app
app = Flask(__name__)
api = Api(app,doc='/docs/')
cors = CORS(app)
app.url_map.strict_slashes = False
app.config['MAIL_SERVER']='mail40.mydevil.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'rebuilder@localhost-group.com'
app.config['MAIL_PASSWORD'] = 'd8gtZrNm8JP6vzR'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def hello():
  return "App running, Test positive \n Errors at rebuilder@localhost-group.com"

@app.route("/rebuild")
def rebuild():
  password = request.args.get('password')
  if password == hashlib.md5(b"bardzo_tajne_haslo").hexdigest():
    repo = request.args.get('repo')
    domain = request.args.get('domain')

    abs_path_mydewil = '/usr/home/VPPoland/domains/'+domain+'/public_nodejs/public'
  
    repo_folder = repo.split('/')[-1].split('.')[0]
  
    if os.path.exists(f'./{repo_folder}'):
      shutil.rmtree(f'./{repo_folder}')
  
    cwd = os.path.join(os.getcwd(), repo_folder)
    subprocess.run(f'git clone https://przemocny:Przejebane123!@github.com/{repo} {repo_folder}', shell=True)
  
    with open('log.txt', "w+") as f:
      # return_of_proces = subprocess.Popen('npm install && npm install react && npm install gatsby && gatsby build', cwd=cwd, shell=True, stdout=f).wait()
      return_of_proces = subprocess.Popen('yarn && gatsby build', cwd=cwd, shell=True, stdout=f).wait()
    if return_of_proces ==0:
      if os.path.exists(abs_path_mydewil):
        shutil.rmtree(abs_path_mydewil)
    
      shutil.move(f'./{repo_folder}/public', abs_path_mydewil)
    
      shutil.rmtree(f'./{repo_folder}')
    
      return "Done"
    else:
      msg = Message('Error Occured', sender='rebuilder@localhost-group.com', recipients = ['rebuilder@localhost-group.com'])
      with app.open_resource('log.txt') as fp:
        msg.attach("log.txt", "text/plain", fp.read())
      mail.html = f'Error with building from {repo} at {domain}'
      mail.send(msg)
    
      return f"Error with building from {repo} at {domain}, log sent to rebuilder@localhost-group.com"
  else:
    return "Wrong Password"

git = api.namespace('git_oauth', path='/github')
google = api.namespace('google_calendar', path='/google')

git.add_resource(Github, '/oauth')
google.add_resource(Google, '/calendar')

if __name__ == "__main__":
     app.run()
