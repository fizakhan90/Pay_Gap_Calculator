from flask import Flask, jsonify, render_template
import pandas as pd
from flask_cors import CORS
import matplotlib.pyplot as plt


app= Flask(__name__)
CORS(app)

df = pd.read_csv('Cleaned.csv')



@app.route('/get_mean_salary')
def get_mean_salary():
     
     gender_pay_gap = df['Salary'].mean()
    
     return jsonify({'gender_pay_gap' : gender_pay_gap})

if __name__ == '__main__':
     app.run(debug=True,port=5500)