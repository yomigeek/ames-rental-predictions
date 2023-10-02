from flask import Flask, request, render_template, jsonify
import util

app = Flask(__name__,
            static_url_path='',
            template_folder='../client/pages')


@app.route('/predict_sales_price', methods=['GET', 'POST'])
def predict_sales_price():
    neighborhood = request.form['neighborhood']
    overall_qual = int(request.form['overall_qual'])
    gr_liv_area = int(request.form['gr_liv_area'])
    year_built = int(request.form['year_built'])
    garage_area = int(request.form['garage_area'])

    response = jsonify({
        'estimated_sales_price': util.predict_sale_price(neighborhood, overall_qual, gr_liv_area, year_built, garage_area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/home')
def find_search():
    return render_template('index.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Sales Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
