from app import create_app

if __name__ == '__main__':
    app = create_app() 
    app.run(host='0.0.0.0', port=5001, debug=False, threaded = False, processes=5)
    # 即多个客户端同时调用访问restful接口，这个服务程序是以多线程方式处理的