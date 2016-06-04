import boto3
import re

client = boto3.client('lambda')

def delete_function(function):
    print("Deleting %s" % (function.get('FunctionName')))
    response = client.delete_function(FunctionName=function.get('FunctionName'))

def delete_functions(regex):
    response = client.list_functions()

    for function in response.get('Functions'):
        name = function.get('FunctionName')
        if re.match(regex, name):
            delete_function(function)

delete_functions(r"clipps-(.+)")
