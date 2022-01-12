#!/usr/bin/python3

import security_audit
import pytest


#This function tests if the entered data is of the correct data type required by the program

def variable_test(name: str, id: int, user_id: int, jwt_token: str, public_key: str, token: str):

	assert type(name) is str, "This is not a name format."
	print ("The name given is: ",name)
	assert type(id) is int, "Please provide a number."
	print ("The ID number given is: ",id)
	assert type(user_id) is int, "Please provide a number"
	print ("The user ID provided is: ",user_id)
	assert type(jwt_token) is str, "This is not the correct format."
	print ("The token provided is: ",jwt_token)
	assert type(public_key) is str, "This is not the correct format."
	print ("The public key provided is: ",public_key)
	assert type(token) is str, "This is not the correct format."
	print ("The token provided is: ",token)


def auth_test(mocker):
	if jwt_payload is True:
		return mocker.patch('security_audit.jwt_payload')
	if external_user_id is True:
		return mocker.patch('security_audit.external_user_id')
	if user is True:
		return mocker.patch('security_audit.user')

