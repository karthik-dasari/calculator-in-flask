from flask import Flask,render_template,redirect,url_for,request,session
from flask_mysqldb import MySQL

app=Flask(__name__)

app.secret_key='abcdefghijklmnopqrstuvwxyz'

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='calculator'

mysql=MySQL(app)

@app.route('/')
@app.route('/home')
def main():
    return render_template('app.html')


@app.route('/senddata', methods=['POST'])
def senddata():
    if request.method == 'POST':
        num1 = request.form['op1']
        num2 = request.form['op2']
        operation = request.form['op']
        sum= request.form['ans']

        cursor=mysql.connection.cursor()            
        cursor.execute(' INSERT INTO data (op1,operator,op2,result) VALUES(%s,%s,%s,%s) ',(num1,operation,num2,sum))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!!"

@app.route('/getdata',methods=['POST','GET'])
def getdata():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM data')
    data=cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('history.html',data=data)

@app.route('/delete/<string:name_data>', methods = ['POST','GET'])
def delete(name_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data WHERE id = %s",(name_data,))
    mysql.connection.commit()
    return redirect('/getdata')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)