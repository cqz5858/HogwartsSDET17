from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import UserM, RoleM, db, app

manager = Manager(app)
migrate = Migrate(app, db)
# print(app.config)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
'''第一执行：
python manager.py db nit
   以后只执行：

python manager.py db migrate & python manager.py db upgrade

'''
