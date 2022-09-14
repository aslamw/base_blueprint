# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 8:15:20 2022

@author: Marcos Wagner
"""

from flask import Blueprint, request, render_template
import json

my_url = Blueprint('api', __name__, url_prefix='/basic_api')

@my_url.route('/')
def hello_world():
    return {'message': 'Hello World!'}
    
@my_url.route('/test', methods=['GET','POST'])
def basic_api():
    if request.method == 'GET':
        return{
            'message':'ok 200',
            'method': request.method
        }
    elif request.method == "POST":
        return{
            'message': 'ok 200',
            'method': 'request.method',
            'body': request.json
        }
@my_url.route('/test/<int:test_id>', methods=['GET','PUT','DELETE'])
def test(teste_id):
    if request.method == 'GET':
        return {
            'id':teste_id,
            'message':'ok 200',
            'method':request.method
        }
    if request.method == 'PUT':
        return {
            'id':teste_id,
            'message':'ok 200',
            'method':request.method,
            'body':request.json
        }
    if request.method == 'DELETE':
        return {
            'id':teste_id,
            'message':'ok 200',
            'method':request.method
        }








