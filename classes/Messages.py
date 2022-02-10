import json

class Messages():
    default_response = json.dumps({'status':'Default response'})
    fail_message = json.dumps({'error':'Value not valid'})
    ok_message = json.dumps({'status':'Test OK'})
