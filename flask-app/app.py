from flask import Flask, render_template
import requests as req

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/service", methods=["POST"])
def service():

    service_req = req.get("http://13.233.19.226:8080/get-service-area")
    city_list = service_req.json()['cities_arr']
    city_string = ''.join(city_list)
    price_req = req.get("http://13.233.19.226:8081/get-prices")
    price_list = price_req.json()['price_arr']
    price_string = ''.join(price_list)
    return render_template("main.html", service=f"{city_string}", prices=f"{price_string}")
#     return render_template("main.html", service=f"{city_string}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
