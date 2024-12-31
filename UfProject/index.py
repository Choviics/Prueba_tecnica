from src import init_app

class Config:
    DEBUG = True
    
app = init_app(Config)

if __name__ == '__main__':
    app.run(port=3000)