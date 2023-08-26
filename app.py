from flask import Flask, render_template

import randomname

app = Flask(__name__)


@app.route('/')
def hello_world():
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
    return render_template('index.html', products=products, category=category)


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


if __name__ == '__main__':
    app.run()
