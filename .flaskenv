# .flaskenv 
FLASK_DEBUG=1
FLASK_ENV=development
FLASK_APP="app:create_app('development')"
#flask会自动从环境变量FLASK_APP的值定义的模块中寻找名称为create_app()或make_app()的工厂函数，自动调用工厂函数创建程序实例并运行。