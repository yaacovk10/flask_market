from flask import Flask, render_template, redirect
import logging



app = Flask(__name__)

market = [{'name': 'cola', 'price': 10},
          {'name': 'coffee', 'price': 20},
          {'name': 'tea', 'price': 5},
          {'name': 'apple', 'price': 2},
          {'name': 'milk', 'price': 6},
          {'name': 'yogourt', 'price': 1},
          {'name': 'xl', 'price': 15}]

cart = []
total_sum = 0

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/shop')
def index():
    return render_template("index.html", market=market, cart=cart, total_sum=total_sum)

@app.route('/buy/<int:product_index>')
def buy_product(product_index):
    global total_sum
    if 0 <= product_index < len(market):
        name = market[product_index]['name']
        item_in_cart = next((item for item in cart if item['name'] == name), None)
        if item_in_cart:
            item_in_cart['amount'] += 1
        else:
            cart.append({"name": name, "amount": 1})
        total_sum += market[product_index]['price']
    return redirect('/shop')



if __name__ == '__main__':
    app.run(debug=True)

