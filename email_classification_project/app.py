from flask import Flask,render_template,url_for,request
import joblib
model = joblib.load(r'C:\Users\ASUS ROG\OneDrive\Desktop\email_classification_project\email_classification_project\models\bernouliNB,lb')
app = Flask(__name__)

bow_obj = joblib.load('./models/bag_of_words.lb')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods = ['POST','GET'])
def prediction():
    if request.method == 'POST':
        message = str(request.form['message'])
        email_message = [message]
        email_converted = bow_obj.transform(email_message).toarray()
        prediction = model.predict(email_converted)[0]
        label_dict = {'0':'Ham','1':'spam'}
        return render_template('output.html',output=label_dict[str(prediction)])

       


if __name__ == "__main__":
    app.run(debug=True)