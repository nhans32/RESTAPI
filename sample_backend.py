from flask import Flask, request, jsonify
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def generate_id():
   letters = string.ascii_lowercase
   numbers = string.digits
   id1 = ''.join(random.choice(letters) for i in range(3))
   id2 = ''.join(random.choice(numbers) for i in range(3))
   return id1 + id2

users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123',
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222',
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999',
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list': []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      for user in users['users_list']:
         if user['id'] == userToDelete['id']:
            users['users_list'].remove(user)
            resp = jsonify(success=True)
            return resp
      return userToDelete['id']
   elif request.method == 'POST':
      userToAdd = request.get_json()
      id = generate_id()
      userToAdd['id'] = id
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True, id=userToAdd['id'], name=userToAdd['name'], job=userToAdd['job'])
      resp.status_code = 201
      return resp

@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users