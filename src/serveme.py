from waitress import serve
from djangolite.wsgi import application

if __name__ == '__main__':
    serve(application,port='80')