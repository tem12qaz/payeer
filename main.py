import base64

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(
        'form.html',
        action='https://4roonas.xyz',
        shop='1630953878',
        orderid='1',
        amount='10.00',
        curr='RUB',
        desc=base64.b64encode(bytes('Test payment')),
        sign='y562xRkL89549065gjkp6ycvbe34qxbnjk8'
    )