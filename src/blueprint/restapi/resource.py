from flask import request, jsonify 
from flask_restx import Resource 
from flask_bcrypt import generate_password_hash, check_password_hash
from src.model import db,User 


class Login(Resource):

    def post(self):
        data = request.get_json()
        if data is None: 
            return jsonify({'message':'Campos vazios'})

        username = data['username']
        password = data['password'] 

        if username == "" and password == "":
            return jsonify({'message':'username ou password estão vazios'})
        login = User.query.filter_by(username=username).first() 

        if login is None:
            return jsonify({'message':'usuario não existe por favor tente novamente'})
        
        if check_password_hash(login['password'], password):
            
        else:
            return jsonify({'message':'password incorreta tenta novamente'})
        

            
        


        


class UserRoute(Resource):
    
    def get(self):
        user = User.query.all()
        return jsonify({'data': [row.to_dict() for row in user] })
    def post(self):
        
        data = request.get_json()
        if data is None:
            messagem = "Campos vazios"
        else:
            self.data_user(data)

        return jsonify({'message':'usuario foi criado com sucesso'})

        

    
    def data_user(self, data):
        username = data['username']
        email = data['email']
        password = generate_password_hash(data['password'],8).decode('utf-8')
       # newpassword = password.replace(' ', '')
        user_create = User(user_name=username,email=email,password=password)
        db.session.add(user_create)
        db.session.commit()
       

    def delete(self,user_id):
        if user_id:
            user_delete  = User.query.filter_by(user_id=user_id).first()
            if use_delete is None:
                return jsonify({'message':'usuario não foi encontrado'})

            db.session.delete(user_delete)
            db.session.commit() 

        return jsonify({'message':'usuario foi deletado com sucesso'})
        
        
    def put(self):
        return ""
