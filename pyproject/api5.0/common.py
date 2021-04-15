import time, datetime, decimal
from flask_restful import fields

#响应数据对应字典
scm = {
	'LOGIN_OK':(True,"4000","登录成功"),
	'LOGIN_ERROR':(False,"4001","登录失败,用户名或密码错误"),
	'DELETE_OK':(True,"5000","删除成功"),
	'DELETE_ERROR':(True,"5001","删除失败"),
	'ID_NOT_EXISTS':(False,"5002","用户ID不存在"),
	'CREATE_OK':(True,"2000","创建成功"),
	'UPDATE_OK':(True,"3000","更新成功"),
	'SUCCESS':(True,"0000","查询成功"),
	'NODATA':(False,"0001","查询成功无记录"),
	'FEAILED':(False,"0002","查询失败"),
	'ACCOUNT_ERROR':(False,"1000", "账户不存在或被禁用"),
	'API_NOT_EXISTS':(False,"1001", "请求的接口不存在"),
	'API_NOT_PER':(False,"1002", "没有该接口的访问权限"),
	'PARAMS_ERROR':(False,"1004", "参数为空或格式错误"),
	'SIGN_ERROR':(False,"1005", "数据签名错误"),
	'AMOUNT_NOT_QUERY':(False,"1010", "余额不够，无法进行查询"),
	'API_DISABLE':(False,"1011", "查询权限已被限制"),
	'UNKNOWN_IP':(False,"1099", "非法IP请求"),
	'SYSTEM_ERROR':(False,"9999", "系统异常")
}
#格式化或过滤输出数据
user_fields = {
	'username':fields.String,
	'role':fields.String(attribute='roles.name'),
	'name':fields.String,
	'age':fields.Integer,
	'phone':fields.String,
	'gender': fields.String,
	'job':fields.String,
	'uri':fields.Url('user', absolute=True),
	'create_at':fields.DateTime(dt_format='iso8601'),
	'update_at':fields.DateTime(dt_format='iso8601'),
	'login_at':fields.DateTime(dt_format='iso8601'),
}

def return_error(scm_key,msg=None):
# 生成错误json
	dic = {
		'success':scm[scm_key][0],
		   'code':scm[scm_key][1],
		    'error':scm[scm_key][2]
	}
	if msg:
		dic['error'] = msg
	return dic

#形参：指的是形式参数，是虚拟的，不占用内存空间，形参单元只有被调用的时才分配内存单元
#实参：指的是实际参数，是一个变量，占用内存空间，数据传递单向，实参传给形参，形参不能传给实参
def return_success(scm_key,data='null'):
	# print(id(dic),type(dic))
	# 生成正确json,code默认200
	dic = {
		'success':scm[scm_key][0],
		   'code':scm[scm_key][1],
		    'msg':scm[scm_key][2],
		   'data': data,
		  'total': len(data)
	}
	# if status == 'CREATE_OK' or status == 'UPDATE_OK':
	# 	del dic['total']
	# return id(dic),type(dic)
	if isinstance(data,dict) or data=='null':
		#dic['total'] = 1
		del dic['total']
	return dic

# print(return_error('NODATA'))