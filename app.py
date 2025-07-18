from flask import Flask, render_template, request 

import pickle

model=pickle.load(open("Finalized_Fake_Model.pkl",'rb'))
vector=pickle.load(open("vectorizer.pkl",'rb'))
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have a templates/index.html file

@app.route('/predict' , methods=['GET','POST'])
def predict():
    

    if request.method=='POST':
        news=request.form["news_text"]
        print(news)
        predict=model.predict(vector.transform([news]))
        print(predict)
        return render_template('prediction.html',prediction_text="News HeadLine is ->{}".format(predict))

    else:
        return render_template('prediction.html')


    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)