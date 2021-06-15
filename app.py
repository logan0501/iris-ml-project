from flask import Flask,render_template,url_for,request,redirect
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method =='POST':
        return redirect('/');
    else:
        return render_template('index.html')



@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        sl = request.form['sl']
        sw = request.form['sw']
        pl = request.form['pl']
        pw = request.form['pw']
        try:
            test_data = [int(sl),int(sw),int(pl),int(pw)]
            test_data = np.array(test_data)
            test_data = test_data.reshape(1,-1)
            print(test_data)
            file = open('static\model\decisiontreemodel.pkl','rb')
            trained_model = joblib.load(file)
            prediction = trained_model.predict(test_data)
            print(prediction)
            return render_template('result.html',data=prediction[0]);
        except Exception as e:
            print(e)
            return 'Error';
          
    else:
        return 'Error';  
    
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
