from os import environ
from flask import Flask, request
from werkzeug.exceptions import BadRequest, Unauthorized

from chains.kilt import Kilt
from chains.moonriver import Moonriver
from chains.moonbeam import Moonbeam
from chains.polkadot import Polkadot
from chains.kusama import Kusama
from chains.astar import Astar

app = Flask(__name__)

NETWORKS = {"kilt": Kilt(), 
        "moonbeam": Moonbeam(), 
        "moonriver": Moonriver(), 
        "kusama": Kusama(), 
        "polkadot": Polkadot(), 
        "astar": Astar()}

AUTH_HEADER_NAME = "X-API-KEY"
AUTH_HEADER = {AUTH_HEADER_NAME: environ["REWARDS_API_KEY"]}


def get_reward(network, address):
    instance = NETWORKS.get(network)
    return instance.get_rewards(address)

def check_api_key(headers):
    auth_header = headers.get(AUTH_HEADER_NAME) 
    if auth_header is None:
        raise BadRequest("X-API-KEY Authentication header is missing")
    if auth_header != AUTH_HEADER[AUTH_HEADER_NAME]:
        raise Unauthorized("Wrong API key")


@app.route("/rewards", methods=['GET'])
def index():
    check_api_key(request.headers)
    if len(request.args) != 2:
        raise BadRequest("API expect two arguments - network and address")
    network = request.args.get("network")
    if network not in NETWORKS.keys():
        raise BadRequest("This network is not supported")
    address = request.args.get("address")
    return str(get_reward(network, address))
app.run()
