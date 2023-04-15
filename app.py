from flask import Flask,redirect,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


model=pickle.load(open('model.pkl','rb'))
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        try:
            f1=float(request.form['f1'])
            f2=float(request.form['f2'])
            f3=float(request.form['f3'])
            f4=float(request.form['f4'])
            f5=float(request.form['f5'])
            f6=float(request.form['f6'])
            f7=float(request.form['f7'])
            f8=float(request.form['f8'])
            f9=float(request.form['f9'])
        except(Exception)  :
            return render_template('index.html',prediction='Please enter numeric values')  
        output=model.predict(pd.DataFrame([[f1,f2,f3,f4,f5,f6,f7,f8,f9]]))[0]
        output=round(output,2)
        result='Forecast sale is ${}'.format(output)
        return render_template('index.html',prediction=result)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
