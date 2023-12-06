from app import app, render_template, request, Response
import randomname
import os
from datetime import datetime
import pdfkit

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
        'page-height': '7in',
        'page-width': '3in',
        'margin-top': '0.1in',
        'margin-right': '0in',
        'margin-bottom': '0.1in',
        'margin-left': '0in',
    }
    pdf = pdfkit.from_string(html, path, options)
    pdf_preview = pdfkit.from_string(html, '', options)

    return Response(pdf_preview, mimetype="application/pdf")
