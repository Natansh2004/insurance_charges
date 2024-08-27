from flask import Flask,render_template,url_for,request
import joblib
import sqlite3

model = joblib.load('./models/linear_model.lb')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        userage = int(request.form['userage'])
        usersex = int(request.form['usersex'])
        userbmi = float(request.form['userbmi'])
        userchildren = int(request.form['userchildren'])
        usersmoker = int(request.form['usersmoker'])
        userregion = int(request.form['userregion'])

        UNSEEN_DATA = [[userage,usersex,userbmi,userchildren,usersmoker,userregion]]
        PREDICTION = model.predict(UNSEEN_DATA)[0][0]

        # INSERTING DATA 

        dict_sex = {1:'Male',2:'Female'}
        dict_smoker = {1:'yes',0:'no'}
        dict_region = {1:'northeast',2:'northwest',3:'southeast',4:'southwest'}

        conn = sqlite3.connect('insurance_charges.db')
        cur = conn.cursor()

        query = """
            insert into insurance_data values(?,?,?,?,?,?,?)
        """

        data = [userage,dict_sex[usersex],userbmi,userchildren,\
                dict_smoker[usersmoker],dict_region[userregion],\
                round(PREDICTION,2)]
        
        cur.execute(query,data)
        conn.commit()
        print('YOUR RECORD HAS BEEN STORED IN OUR DATABASE')
        cur.close()
        conn.close()

        return render_template('home.html',predicted_charges=round(PREDICTION,2))

if __name__ == '__main__':
    app.run(debug=True)