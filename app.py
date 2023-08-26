from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    category = [
        {
            'id': 1,
            'name': 'drink',
        },
        {
            'id': 2,
            'name': 'beer',
        },
        {
            'id': 3,
            'name': 'tea',
        },
        {
            'id': 4,
            'name': 'food',
        },
        {
            'id': 4,
            'name': 'food',
        },
        {
            'id': 4,
            'name': 'food',
        },
        {
            'id': 4,
            'name': 'food',
        },
        {
            'id': 4,
            'name': 'food',
        },
        {
            'id': 4,
            'name': 'food',
        }
    ]
    products = [
        {
            'id': 1,
            'name': 'coca cola',
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        },
    ]
    for item in range(100):
        products.append({
            'id': 1,
            'name': 'coca cola',
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        })
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
            'name': 'coca cola',
            'price': 10,
            'discount': 40,
            'category_name': 'drink',
        })
    return render_template('pos_screen.html', rows=rows)


if __name__ == '__main__':
    app.run()
