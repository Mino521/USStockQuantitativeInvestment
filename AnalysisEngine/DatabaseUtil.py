from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime,Numeric,Date,Time
import pymysql
import Config
pymysql.install_as_MySQLdb()
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:3306/%s'%(Config.caDBusername,Config.caDBpassword,Config.caDBserver,Config.DBname)
app.config['SQLACHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class AlgorithmLib(db.Model):
    __tablename__ = 'AlgorithmLib'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    AlgorithmName = db.Column(db.String(256),unique=True)
    Description = db.Column(db.Text)
    Parameter = db.Column(db.Text)
    Output = db.Column(db.Text)

def model_to_dict(model):
    for col in model.__table__.columns:
        if isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)
        
def model_list_to_dict_list(models):
    lst = []
    for model in models:
        gen = model_to_dict(model)
        dit = dict((g[0],g[1]) for g in gen)
        lst.append(dit)
    return lst    
    
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
