from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    user_collentions = mongo.db.users
    user_collentions.insert({'name': 'leonardo Setubal'})
    return '<h1>Usuário adicionado</1>'