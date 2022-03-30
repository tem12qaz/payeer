import base64

from flask import Flask, render_template, request

from config import CURRENCY, SHOP, DESCRIPTION
from signature import make_sign

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print(request.data)
        print(request)

    order = "1"
    amount = "10.00"

    return render_template(
        'form.html',
        shop=SHOP,
        orderid=order,
        amount=amount,
        curr=CURRENCY,
        desc=base64.b64encode(bytes(DESCRIPTION, encoding='utf-8')).decode('utf-8'),
        sign=make_sign(order, amount)
    )