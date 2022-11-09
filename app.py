#Import Libraries
from flask import Flask, render_template , redirect,url_for, session, request
import model # load model.py
import function

app = Flask(__name__)

# render htmp page
@app.route('/')
def home():
    return render_template('index.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    price_per_sqft = input_features[4]
    area_type = input_features[5]
    availability = input_features[6]
    location = input_features[7]
    
    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       

    listHouse = function.Fetch(predicted_price,total_sqft_int,bhk)

    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of This House is Rs. {} lacs'.format(predicted_price), listHouse=listHouse)

    
if __name__ == "__main__":
    app.run()
    
app.run(debug=True)
