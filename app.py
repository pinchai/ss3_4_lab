from flask import Flask, render_template, request

import randomname

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    filter_category = request.args.get('filter_category', default="all", type=str)
    category = []
    products = []

    for item in range(50):
        products.append({
            'id': 1,
            'name': randomname.get_name(noun=('food', 'cats')),
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        })
    for item in range(5):
        category.append(
            {
                'id': 1,
                'name': randomname.get_name(noun=('gaming')),
            },
        )

    return render_template('index.html', products=products, category=category, filter_category=filter_category)


@app.route('/pos')
def pos_index():
    rows = [
        {
            'id': 1,
            'name': 'coca cola',
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        },
    ]
    for item in range(10):
        rows.append({
            'id': 1,
            'name': randomname.get_name(noun=('food', 'cats')),
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        })
    return render_template('pos_screen.html', rows=rows)


@app.route('/product_detail/<string:name>/<string:category>/<string:price>/<string:image>')
def product_detail(name, category, price, image):

    return render_template('product_detail.html', name=name, category=category, price=price, image=image)


if __name__ == '__main__':
    app.run()
