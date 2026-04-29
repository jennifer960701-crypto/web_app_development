import os
from flask import Flask
from dotenv import load_dotenv

# 引入路由註冊函式與資料庫初始化函式
from app.routes import register_routes
from app.models.db import init_db

# 載入環境變數
load_dotenv()

def create_app():
    """初始化 Flask App"""
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    # 設定 SECRET_KEY 用於 Session 與 Flash Message
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_default_secret')
    
    # 確保 instance 目錄存在，並初始化資料庫結構
    os.makedirs(os.path.join(app.root_path, '..', 'instance'), exist_ok=True)
    init_db()
    
    # 註冊所有的 Blueprints
    register_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
