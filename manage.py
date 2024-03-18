from app import create_app
# import os

if __name__ == '__main__':
    # app = create_app(os.getenv('CONFIG') or 'default')
    app = create_app('development')
    app.run()