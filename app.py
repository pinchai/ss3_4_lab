from flask import Flask, render_template, request
import random

import randomname

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    filter_category = request.args.get('filter_category', default="all", type=str)
    products = []
    categories = [
        {
            "id": 1,
            'name': 'drink'
        },
        {
            'id': 2,
            'name': 'food'
        },
        {
            'id': 3,
            'name': 'beer'
        },
        {
            'id': 4,
            'name': 'fast food'
        },
        {
            'id': 5,
            'name': 'coffee'
        },
        {
            'id': 6,
            'name': 'tea'
        },
    ]

    for item in range(12):
        category = random.choice(categories)
        products.append({
            'id': 1,
            'name': randomname.get_name(noun=('food')),
            'price': random.randint(1, 1000),
            'discount': random.randint(1, 100),
            'category_name': category['name'],
        })

    product_filter = []
    if filter_category == 'all' or filter_category == '':
        product_filter = products
    else:
        for pro_item in products:
            if pro_item['category_name'] == filter_category:
                product_filter.append(pro_item)

    return render_template(
        'index.html',
        products=product_filter,
        category=categories,
        filter_category=filter_category
    )


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
