

"""
Account Service

This microservice handles the lifecycle of Accounts.
"""
# pylint: disable=unused-import
from flask import jsonify, request, make_response
from service.models import Account
from service.common import status  # HTTP Status codes
from . import app  # Import Flask application


###############################################
# Health Endpoint
###############################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


###############################################
# GET INDEX
###############################################
@app.route("/")
def index():
    """Index endpoint"""
    return jsonify(dict(message="Welcome to Account Service")), status.HTTP_200_OK


###############################################
# GET ALL ACCOUNTS
###############################################
@app.route("/accounts", methods=["GET"])
def get_accounts():
    """Retrieve all accounts"""
    accounts = Account.query.all()
    results = [account.to_dict() for account in accounts]
    return jsonify(results), status.HTTP_200_OK


###############################################
# GET ACCOUNT BY ID
###############################################
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """Retrieve a single account"""
    account = Account.query.get_or_404(account_id)
    return jsonify(account.to_dict()), status.HTTP_200_OK


###############################################
# CREATE ACCOUNT
###############################################
@app.route("/accounts", methods=["POST"])
def create_account():
    """Create a new account"""
    data = request.get_json()
    account = Account(**data)
    account.save()
    return jsonify(account.to_dict()), status.HTTP_201_CREATED


###############################################
# UPDATE ACCOUNT
###############################################
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an existing account"""
    account = Account.query.get_or_404(account_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(account, key, value)
    account.save()
    return jsonify(account.to_dict()), status.HTTP_200_OK


###############################################
# DELETE ACCOUNT
###############################################
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account"""
    account = Account.query.get_or_404(account_id)
    account.delete()
    return "", status.HTTP_204_NO_CONTENT


