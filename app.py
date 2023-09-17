from flask import Flask, jsonify
import pandas as pd

app= Flask(__name__)

df = pd.read_csv('Cleaned.csv')

@app.route('/get_mean_salary')
def get_mean_salary():
     
     mean_salary = df['Salary'].mean()
     return jsonify({'mean_salary' : mean_salary})

if __name__ == '__main__':
     from waitress import serve
     serve(app, host="0.0.0.0", port=8080)
     app.run()