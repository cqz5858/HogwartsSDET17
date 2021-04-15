import sys
from models import db, UserM
import jwt 
import datetime
from jwt import exceptions
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from flask import g, request
from common import return_error
# from api_rest5 import app

#支持多种验证方式，1、Basic Auth
baseauth = HTTPBasicAuth()          
@baseauth.verify_password#verify_password_callback=True/False,执行验证并返回结果
def verify_password(username,password):
    user = UserM.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

 #2、jwt认证
tokenauth = HTTPTokenAuth()
JWT_SALT = 'JWT_SALT'
@tokenauth.verify_token
def verify_token(access_token):
	access_token = request.args.get('access_token') or request.form.get('access_token')
	# app.logger.info(request.form)
	# app.logger.info(request.args)
	if not access_token:
		tokenauth.error_handler(return_error('PARAMS_ERROR', 'access_token不能为空').__repr__)	
		return False
	try:
		verifed_payload = jwt.decode(access_token, JWT_SALT, True, verify_exp=False)
	except exceptions.ExpiredSignatureError as e:#exp超时就停止验证
		tokenauth.error_handler(return_error('SIGN_ERROR', e).__repr__)	
		return False
	except jwt.DecodeError as e:#header,payload(base64双数据字符),crypto格式不对
		tokenauth.error_handler(return_error('SIGN_ERROR', e).__repr__)	
		return False
	except jwt.InvalidTokenError as e:#格式是对的,header,payload,crypto对不上
		tokenauth.error_handler(return_error('SIGN_ERROR', e).__repr__)	
		return False
	return True

# multiauth = MultiAuth(baseauth,tokenauth)
multiauth = MultiAuth(tokenauth, baseauth)

#生成jwt
def create_token(user, expires=300):
	#构造header
	headers = {
	'tye':'jwt',
	'alg':'HS256'
	}
	#构造payload
	payload = {
	'user_id':user.id,
	'username':user.username,
	'iat': datetime.datetime.now(),
	'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires)#jwt解码时datetime.utcnow()
	}		
	token = jwt.encode(payload=payload, key=JWT_SALT, algorithm='HS256',
		headers=headers).decode('utf-8')
	return token, expires
	
if __name__ == '__main__':
	payload = {'user_id':'1','username':'pig'}
	# token = create_token(payload,1)
	# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInR5ZSI6Imp3dCJ9.eyJ1c2VyX2lkIjoiMSIsInVzZXJuYW1lIjoicGlnIiwiZXhwIjoxNTc4MzgxMjk1fQ.GHK1R6JNmXjWjwVMqAiUvj2yscmNix7juemEVw-WGkU'
	token = b'1.1.1'
	print(token)
	print(verify_token(token))


