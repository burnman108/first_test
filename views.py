#-*- coding: utf-8 -*-
#encoding=utf-8
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'my is  some_secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/climatetest'
db = SQLAlchemy(app)


# class Duty(db.Model):
#     __tablename__ = "du_duty"
#     duty_id = db.Column(db.Integer, primary_key=True)
#     category_id = db.Column(db.Integer, unique=True)
#     user_id = db.Column(db.Integer, unique=True)
#     title = db.Column(db.String(64), unique=True)
#     status = db.Column(db.Integer, unique=True)
#     is_show = db.Column(db.Integer, unique=True)
#     create_time = db.Column(db.Integer, unique=True)
#
#     def __init__(self, category_id, user_id, title, status, is_show, create_time):
#         self.category_id = category_id
#         self.user_id = user_id
#         self.title = title
#         self.status = status
#         self.is_show = is_show
#         self.create_time = create_time
#
#     def __repr__(self):
#         return self.title
class climateBeijing(db.Model):
    __tablename__ = "wh_qx_beijing"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    WindDir = db.Column(db.String(64), nullable=True)
    Pressure = db.Column(db.String(64), nullable=True)
    Temp = db.Column(db.String(64), nullable=False)
    Visibility = db.Column(db.String(64), nullable=True)
    DewPoint = db.Column(db.String(64), nullable=True)
    Precip = db.Column(db.String(64), nullable=True)
    time = db.Column(db.String(64), nullable=False)
    WindSpeed = db.Column(db.String(64), nullable=True)
    date = db.Column(db.String(64), nullable=False)
    Humidity = db.Column(db.String(64), nullable=True)
    Condition = db.Column(db.String(64), nullable=True)
    GustSpeed = db.Column(db.String(64), nullable=True)
    WindChill_HeatIndex = db.Column(db.String(64), nullable=True)
    Events = db.Column(db.String(64), nullable=True)
    def __init__(self, date, time):
        self.date = date
        self.time = time
    def __repr__(self):
        return self.date



@app.route('/show',methods=['GET', 'POST'])
def show():
    if request.method == 'GET' and request.args.get('date', 'city'):
        city = request.args.get('city')
        date_id = request.args.get('date')
        sql = 'select * from wh_qx_%s where date = %s' % (city,date_id)
    wh_list = db.session.execute(sql).fetchall()
    # category_list = Category.query.order_by(Category.category_id).all()
    return render_template('show.html',wh_list = wh_list) #,category_list=category_list,myname=myname)


if __name__ == '__main__':
	app.debug = True
	app.run()