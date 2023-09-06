from flask import Flask, render_template, request

app = Flask(__name__)

market = [{'name': 'cola', 'price' : 10},
          {'name':'cafe', 'price': 20},
          {'name':'tea', 'price': 5},
          {'name':'apple', 'price': 2},
            {'name':'milk', 'price': 6},
              {'name':'yogourt', 'price': 1},
                {'name':'xl', 'price': 15},  ]

cart = []
total_sum = 0

@app.route('/')
def index():
    global total_sum
    product_index = request.args.get('prod')
    print (product_index)
    if product_index:
        print(market[int(product_index)])
        cart.append(market[int(product_index)]['name'])
        total_sum += market[int(product_index)]['price']
        print(f"total is {total_sum}")
    return render_template ("index.html", list = market, product = product_index, cart = cart, total_sum = total_sum)



if __name__ == '__main__':
    app.run(debug=True)