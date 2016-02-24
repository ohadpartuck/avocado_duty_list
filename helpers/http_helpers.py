import re
import json
from bson.objectid import ObjectId
from flask import Response, render_template

regex_type = type(re.compile('hello, world'))
# overwriting the default JSONEncoder.
# why ? because it can't deserialize ObjectId and regex
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId) or isinstance(obj, regex_type):
            return str(obj)
        else:
            return obj

def output_json(data, code, headers=None):
    #Encoder - handles bson ids
    resp = Response(json.dumps(data, cls=Encoder),mimetype='application/json')
    resp.status_code = code
    return resp


def render_global(**kwargs):
    kwargs.setdefault('specific_assets',{})
    page = kwargs.get('page', 'global/application.html')
    return render_template(page,
                           **kwargs)
