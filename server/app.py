#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:contract_id>')
def get_contract(contract_id):
    """
    return contract information if found (200), otherwise 404
    """
    #Search for contract by id
    for contract in contracts:
        if contract['id'] == contract_id:
            #Return the contract_information with 200 OK
            return contract['contract_information'], 200
    #Not found
    return '', 404

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """
    return 204 if customer exists (no data), otherwise 404.
    """
    # Case-insensitive lookup
    if customer_name.lower() in customers:
        # Successful but no content to return
        return '', 204
    #Not found
    return '', 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
