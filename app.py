from flask import Flask, render_template, request, redirect
import random
import sqlite3 as sql

import randomname

app = Flask(__name__)

# conn = sqlite3.connect('ss34_database.db')
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# conn.close()


@app.route('/')
@app.route('/home')
def home():
    filter_category = request.args.get('filter_category', default="all", type=str)
    products = []
    categories = [
        {
            'id': 1,
            'name': 'drink'
        },
        {
            'id': 2,
            'name': 'food'
        },
        {
            'id': 3,
            'name': 'fast food'
        },
        {
            'id': 4,
            'name': 'beer'
        },
        {
            'id': 5,
            'name': 'cafe'
        }
    ]
    for item in range(12):
        category = random.choice(categories)
        products.append({
            'id': 1,
            'name': randomname.get_name(noun=('food')),
            'price': 10,
            'discount': 30,
            'category_name': category['name'],
        })

    product_filter = [];
    if filter_category == 'all' or filter_category == '':
        product_filter = products
    else:
        for product_found in products:
            if product_found['category_name'] == filter_category:
                product_filter.append(product_found)

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


@app.route('/admin')
def admin():

    con = sql.connect("ss34_database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()

    return render_template('admin/index.html', rows=rows)


@app.route('/admin/add_student', methods=['POST'])
def add_student():
    if request.method == "POST":
        try:
            name = request.form['name']
            gender = request.form['gender']
            address = request.form['address']
            phone = request.form['phone']

            with sql.connect("ss34_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,gender,address,phone) VALUES (?,?,?,?)",
                            (name, gender, address, phone))
                con.commit()
                msg = "Record successfully added"
                return redirect('/admin')
        except:
            con.rollback()
            msg = "error in insert operation"


@app.route('/product_detail/<string:name>/<string:category>/<string:price>/<string:image>')
def product_detail(name, category, price, image):
    return render_template('product_detail.html', name=name, category=category, price=price, image=image)


if __name__ == '__main__':
    app.run()
