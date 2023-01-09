from datetime import datetime
from flask import jsonify, make_response # redirect, request, url_for, current_app, flash, 
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
import json

import config
import authinfo
import tides as mst
import myGlobals as mg
from common.utils import myprint, masked

def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


class TidesAPI(Resource):

    def __init__(self):
        pass
    
    def get(self, id):
        info = mst.getTidesInfo(id)
        myprint(1, json.dumps(info, ensure_ascii=False))
        return info

    def put(self, id):
        pass

    def delete(self, id):
        pass


class TodayTidesAPI(Resource):

    def __init__(self):
        pass
    
    def get(self):
        info = mst.getTidesInfo(datetime.now().strftime('%d%m%y'))
        myprint(1, json.dumps(info, ensure_ascii=False))
        return info

    def put(self, id):
        pass

    def delete(self, id):
        pass
    
