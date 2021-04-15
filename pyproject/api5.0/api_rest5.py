from flask import Flask, request
from flask_restful import Api, Resource, reqparse, marshal
import datetime, time
from common import user_fields,return_success, return_error
from auths import multiauth, baseauth, tokenauth, create_token
from models import RoleM, UserM, db

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
app.config.from_object('config')
db.init_app(app)
api = Api(app)


class User(Resource): # 用户资源
	def __init__(self):	
		self.parser = reqparse.RequestParser()  # 实例化参数解析器
		self.parser.add_argument('id', type=str)  # 定义将要解析的参数
		self.parser.add_argument('username', type=str)
		self.parser.add_argument('password', type=str)
		self.parser.add_argument('grant_type', type=str)
		self.parser.add_argument('name', type=str)
		self.parser.add_argument('job', type=str)		
		self.parser.add_argument('gender', type=str, choices=("男", "女"), help='性别请输入男或女')
		self.parser.add_argument('age', type=int)
		self.parser.add_argument('phone', type=str)
		self.parser.add_argument('role_id', type=int, default=3)
		self.parser.add_argument('access_token', type=str)

	@baseauth.login_required
	def post(self):  # 创建用户
		parser_post = self.parser.copy()
		parser_post.replace_argument('username', type=str, required=True, help='username 必填')
		parser_post.replace_argument('password', type=str, required=True, help='password 必填')
		args = parser_post.parse_args()
		if UserM.query.filter(UserM.username==args['username']).all():
			return {"success": False, 'code': '2001', 'msg': '%s已存在'%args['username']}
		user = UserM(
		username=args['username'], name=args['name'], 
		job=args['job'], gender=args['gender'], age=args['age'], phone=args['phone'],role_id=args['role_id'] 
		)
		user.hash_password(args['password'])
		try:
			db.session.add(user)
			db.session.commit()
			obj = UserM.query.filter(UserM.username == args['username']).all()
			dic = marshal(obj, user_fields)
			return return_success('CREATE_OK', dic)
		except Exception as e:
			return {'success':False, 'code':'2004', 'msg':'创建失败%s'%e.args}

	@baseauth.login_required
	@tokenauth.login_required
	def get(self):  # 根据用户id查询用户
		args = self.parser.parse_args()
		if args['id']:
			obj = UserM.query.filter(UserM.id == args['id']).all()
			if obj:
				dic = marshal(obj,user_fields)	
				return return_success('SUCCESS', dic)
			else:
				return return_error('NODATA')
		obj = db.session.query(UserM).outerjoin(RoleM).all()
		dic = marshal(obj, user_fields)
		return return_success('SUCCESS', dic)

	@baseauth.login_required
	@tokenauth.login_required
	def put(self):  # 根据用户id更新用户
		args = self.parser.parse_args()
		user = UserM.query.get(args['id'])
		if not user:
			return {"success": False, 'msg': 'id:%s不存在！！' % args['id']}
		try:
			if args['name']:
				user.name = args['name']
			if args['job']:
				user.job = args['job']
			if args['gender']:
				user.gender = args['gender']
			if args['age']:	
				user.age = args['age']
			if args['phone']:
				user.phone = args['phone']
			db.session.add(user)
			if not db.session.commit():
				obj = UserM.query.get(args['id'])
				dic = marshal(obj, user_fields)
				return return_success('UPDATE_OK', dic)
		except Exception as e:
			return {"success": False, 'msg': '更新失败！！', 'code': 3004, 'error': e.args[0]}
	
	@baseauth.login_required
	@tokenauth.login_required
	def delete(self):#根据用户id删除用户,需要Basic Auth 和 jwt 认证。
		args = self.parser.parse_args()
		if not args['id']:
			return return_error("PARAMS_ERROR",'id不能为空')
		user = UserM.query.get(args['id'])
		if user:
			try:
				db.session.delete(user)
				if not db.session.commit():
					return return_success('DELETE_OK')
			except Exception as e:
				return return_error('DELETE_ERROR','id%s删除失败： %s'%(e.args[0], args['id']))
		else:
			return return_error("ID_NOT_EXISTS",'id%s不存在'%args['id'])

class Login(User):#用户登录返回access_token
	@baseauth.login_required
	def post(self):
		args = self.parser.parse_args()
		if not args['username'] or not args['password']:
			return return_error("PARAMS_ERROR","用户或密码不能为空")
		user = UserM.query.filter_by(username=args['username']).first()
		if user and user.verify_password(args['password']):
			access_token,expires= create_token(user, expires=360000)
			# app.logger.info(token)#登录成功返回token
			user.login_at = datetime.datetime.now()
			db.session.add(user)
			db.session.commit()
			data = {'user':user.username, 'access_token':access_token, 'expires':expires}
			return return_success("LOGIN_OK",data) 
		return 	return_error('LOGIN_ERROR')

#定义路由
api.add_resource(User,'/test/api/v1.0/users','/test/api/v1.0/users/<int:id>',endpoint='user')
api.add_resource(Login,'/test/api/v1.0/login',endpoint='login')

#以调试模式启动服务
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8899, threaded=10)
