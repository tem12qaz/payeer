import base64

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print(request.data)
        print(request)
    return render_template(
        'form.html',
        action='https://4roonas.xyz',
        shop='1630953878',
        orderid='1',
        amount='10.00',
        curr='RUB',
        desc=base64.b64encode(bytes('Test payment', encoding='utf-8')),
        sign='y562xRkL89549065gjkp6ycvbe34qxbnjk8'
    )