from flask import request
import logging as logger
import jsonpickle

from api import flask_app_instance
from util.custom_class import class_instance as some_instance


@flask_app_instance.route("/task", methods=['POST'])
def task():

    logger.debug("executing output method...")
    
    request_dict = jsonpickle.decode(request.data)
    
    some_string, counter, np_array = some_instance.get_attributes()

    return_dict = {}
    return_dict['message'] = 'executing output method'
    return_dict['some_string'] = some_string
    return_dict['counter'] = str(counter)
    return_dict['np_array'] = np_array
    return_dict['image'] = request_dict['image']
    
    response = jsonpickle.encode(return_dict)

    return response, 200
