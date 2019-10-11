from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    # 初始化项目对象
    app = Flask(__name__)
    # 配置
    app.config.from_object(config_class)

    # 解决跨域问题
    CORS(app)

    db.init_app(app)
    migrate.init_app(app,db)

    # 注册蓝图
    from app.api import bp
    app.register_blueprint(bp)


    return app

from app import models
