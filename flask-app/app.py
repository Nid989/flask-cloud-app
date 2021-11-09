from flask import Flask, render_template
import requests as req

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/service", methods=["POST"])
def service():

    service_req = req.get("http://127.0.0.1:8080/get-service-area")
    city_list = service_req.json()['cities_arr']
    city_string = '\n'.join(city_list)
    # price_req = req.get("http://127.0.0.1:8081/get-prices")
    # price_list = price_req.json()['price_arr']
    # price_string = '\n'.join(price_list)
    # return render_template("main.html", service=f"{city_string}", price = f"{price_string}")
    return render_template("main.html", service=f"{city_string}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')