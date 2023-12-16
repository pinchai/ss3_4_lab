from app import app, render_template, request, Response, connection, text
import randomname
import pdfkit
import os
import json
from datetime import datetime

@app.route('/pos')
def pos_index():
    return render_template('pos_screen.html')


@app.route("/pdf")
def index_pdf():
    path = os.getcwd() + '../pdf/invoice.pdf'
    if not os.path.exists(path):
        os.makedirs(os.getcwd() + '../pdf')

    data = [
        {'id': 1, 'name': 'កូកាកូឡា', 'qty': 20, 'price': 0.25},
        {'id': 1, 'name': 'sting', 'qty': 10, 'price': 0.25},
        {'id': 1, 'name': 'abc', 'qty': 3, 'price': 25},
        {'id': 1, 'name': 'Anchor', 'qty': 6, 'price': 25},
        {'id': 1, 'name': 'KRUD', 'qty': 4, 'price': 25},
        {'id': 1, 'name': 'VATANAK', 'qty': 1, 'price': 25},
        {'id': 1, 'name': 'DRAGON', 'qty': 2, 'price': 25},
    ]
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M")
    server_url = request.url_root
    html = render_template("invoice.html", data=data, now=created_at, server_url=server_url)
    options = {
        # 'page-size': 'a7',
        'page-height': '10in',
        'page-width': '3in',
        'margin-top': '0.1in',
        'margin-right': '0in',
        'margin-bottom': '0.1in',
        'margin-left': '0in',
    }
    pdf = pdfkit.from_string(html, path, options)
    pdf_preview = pdfkit.from_string(html, '', options)

    return Response(pdf_preview, mimetype="application/pdf")


@app.route('/pos/create_transaction', methods=['post'])
def create_transaction():
    total_price = request.form.get('total_price')
    received_amount = request.form.get('received_amount')
    selected_product = request.form.get('selected_product')

    # insert sale transaction
    result = connection.execute(text("INSERT INTO sale (date, customer_id) VALUES ('2023-12-16', 1)"))
    sale_id = result.lastrowid
    connection.commit()
    return '12'
