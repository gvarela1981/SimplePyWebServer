import http.server as server
import socketserver
import json


class PyJSONHandler(server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
    def do_GET(s):
        """
        Respond to a GET request.
        """
        json_response = json.dumps({'status':'Default response'})
        checkPath = s.path[0:].split('/')
        if(checkPath[1] == ''):
            s.do_ResponseOK(json_response)
        else:
            s.do_Header()
    def do_Header(s):
        '''
        Respond only requested header
        '''
        acceptedValues = [
                            'catalog.xlsx',
                            'catalog.csv'
                        ]

        # Remove first '/' from request string
        requestesHeader = s.path[1:].split('/')
        dict_s = dict(s.headers)
        if str(requestesHeader[0]) in acceptedValues:
            json_response = json.dumps({'status':'Test OK'})
            s.do_ResponseOK(json_response)
        else:
            json_response = json.dumps({'error':'Value not valid'})
            s.do_ResponseFAIL(json_response)
    def do_ResponseOK(s, response):
        '''
        Send Response
        '''
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write(response.encode("utf-8"))
        s.end_headers()
    def do_ResponseFAIL(s, response):
        '''
        Send Failed Response
        '''
        s.send_response(400)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write(response.encode("utf-8"))
        s.end_headers()