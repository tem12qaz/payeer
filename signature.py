import base64
from hashlib import sha256

from config import DESCRIPTION, SHOP, CURRENCY, SECRET_KEY


def make_sign(m_orderid, m_amount):
    m_desc = base64.b64encode(bytes(DESCRIPTION, encoding='utf-8'))
    list_of_value_for_sign = map(str, [SHOP, m_orderid, m_amount, CURRENCY, m_desc, SECRET_KEY])
    result_string = bytes(":".join(list_of_value_for_sign), encoding='utf-8')
    sign_hash = sha256(result_string)
    sign = sign_hash.hexdigest().upper()
    return sign
