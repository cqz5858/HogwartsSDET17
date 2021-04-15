import datetime, time
from flask import Flask
#
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, not_
from passlib.apps import custom_app_context as pwd_context

# 配置sqlalchemy,配置文件config
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

'''定义模型，建立关系'''
class RoleM(db.Model):
	__tablename__ = 'roles'#定义表名

	#定义对象
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	create_at = db.Column(db.DateTime, default=datetime.datetime.now)
	update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
	user = db.relationship('UserM', backref='roles', lazy='joined', uselist=True)

	# def __repr__(self):
	# 	return '{"id":%d, "name":"%s"}'%(self.id, self.name)

class UserM(db.Model):
	__tablename__ = 'users'#定义表名

	#定义对象
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64),nullable=False,unique=True,index=True)
	#sha512_crypt至少120字节，列长度不足ValueError: malformed SHA512 hash (checksum must be exactly 86 chars)
	password_hash = db.Column(db.String(128),nullable=False)
	name = db.Column(db.String(64),index=True)
	gender = db.Column(db.String(64),index=True)
	age = db.Column(db.Integer)
	job = db.Column(db.String(64),index=True)
	phone = db.Column(db.String(64),index=True)
	create_at = db.Column(db.DateTime,default=datetime.datetime.now)
	update_at = db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)
	login_at = db.Column(db.DateTime)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=3)#建立外键表明可以在roles表查询记录
	
	def hash_password(self,password):#密码加密
		self.password_hash = pwd_context.encrypt(password)
	
	def verify_password(self,password):#验证密码
		try:
			result = pwd_context.verify(password, self.password_hash)
			return result
		except Exception as e:
			# app.logger.warning(e)
			print(e)
			return False
'''进行数据库操作'''
if __name__ == '__main__':
	#数据迁移
	#删、建表
	# db.drop_all()
	# db.create_all()

	# # #插入数据
	# try:
	# 	Role_admin = RoleM(name='admin')
	# 	Role_mod = RoleM(name='moderator')
	# 	Role_user = RoleM(name='user')

	# # 	User_admin = UserM(username='admin', password_hash='123456', roles=Role_admin)
	# # 	User_cqz= UserM(username='cqz', password_hash='123456', roles=Role_user)
	# # 	User_test = UserM(username='test', password_hash='123456', roles=Role_user)

	# 	db.session.add_all([Role_admin,Role_mod,Role_user])
	# # 	db.session.add_all([Role_admin,Role_mod,Role_user,User_admin,User_cqz,User_test])
	# 	db.session.commit()
	# 	print('数据插入成功！！')
	# except Exception as e:
	# 	print(e.args)
	# #修改数据
	# admin_Role.name = 'Administrator'
	# db.session.add(admin_Role)
	# db.session.commit()

	# #删除数据
	# db.session.delete(mod_Role)
	# db.session.commit()

	#查询数据
	# print(RoleM.query.all())
	# print(UserM.query.all())
	# res = User.query.filter(or_(User.username=='cqz', User.name=='test').all()
	# a = 'name'
	# User = db.session.query(User).join(Role).all()
	# User = User.join(Role).query.all()
	# User.__dict__[a] = '管理员'
	# User.name = 'admin1111'
	# db.session.delete(User)
	# db.session.commit()
	# user = db.session.query(UserM).outerjoin(RoleM).all()
	# user = db.session.query(UserM).outerjoin(RoleM)
	# user = UserM.query.filter(UserM.username=='test').first()
	# user = UserM.query.outerjoin(RoleM,UserM.id==RoleM.id)
	# user = UserM.query.all()
	# print(user[0].roles)
	# print(type(user))
	# print(user)
	# user = UserM.query.filter_by(username='cqz').first()
	# # token = user.getTokenSeq(600)
	# # print(token)
	# # # print(token[2:-1])
	# result = user.verify_password('1111')
	# print(user.password_hash)
	# print(result)
	pass