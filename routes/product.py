from app import app, render_template, connection, text
import randomname


@app.route('/getAllProduct')
def getAllProduct():
    products = connection.execute(text('select * from product'))
    connection.commit()

    json_string = []
    for product in products:
        json_string.append(
            {
                'id': product.id,
                'name': product.name,
                'cost': product.cost,
                'price': product.price,
            }
        )

    return json_string


@app.route('/createProduct', methods=['POST'])
def createAllProduct():
    connection.execute(text("INSERT INTO product (name, cost, price) VALUES ('coca', 1, 10)"))
    connection.commit()
    return 'created successfully'
