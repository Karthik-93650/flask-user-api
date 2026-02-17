from flask import Flask,request,jsonify

app = Flask(__name__)

#In-memory data store
users = {}
user_id_count = 1

#Get all users
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users),200 #200->status response code

#Get single user
@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]),200
    return jsonify({"error":"User Not Found"}),404

#Create new user 
@app.route('/users',methods=['POST'])
def create_user():
    global user_id_count

    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({'error':'Invalid data'}),400
    
    users[user_id_count] = {
        'name': data['name'],
        'email' : data['email']
    }

    user_id_count += 1
    return jsonify({'message':'User Created'}),201

#Update user
@app.route('/users/<int:user_id>',methods=['PUT'])
def  update_user(user_id):
    if user_id not in users:
        return jsonify({'error':'User not found'}),404
    
    data = request.json
    users[user_id]['name'] = data.get('name',users[user_id]['name'])
    users[user_id]['email'] = data.get('email',users[user_id]['email'])

    return jsonify({'message':'User Updated'}),200

#Delete user
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error':'User not found'}),404
    
    del users[user_id]
    return jsonify({'message':'User deleted'}),200

if __name__ =="__main__":
    app.run(debug=True)