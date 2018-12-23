import jwt
from app import app

class Jwt(object):

    @staticmethod
    def create_tkn(graph_id, owner_id):
        return {
            'token': app.config['NOAUTH'],
            'graph_id': graph_id,
            'owner_id': owner_id
        }

    @staticmethod
    def encode(encoded):
        return jwt.encode(encoded, app.config['SECRETJWT_PRIVATE'], algorithm='HS256')