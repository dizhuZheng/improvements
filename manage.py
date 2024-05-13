from app import create_app

if __name__ == '__main__':
    app = create_app() # 接受一个参数，是应用使用的配置名。
    app.run(use_reloader=True, port=5000)