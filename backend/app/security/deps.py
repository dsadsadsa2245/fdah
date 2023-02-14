import datetime

import jwt

SECRET = 'GHDSJOHGO*#$U@P(#@H*HF#(PWHF*(H'


def create_access_token(user_id: int): #можно любой арг
    encoded_jwt = jwt.encode(   #encode-хеширует данные токена.У нас это sub и exptime
        {'sub': user_id, 'exp_date': (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()},
        SECRET,
        algorithm='HS256' # алгоритм хеширования
    )
    return encoded_jwt
