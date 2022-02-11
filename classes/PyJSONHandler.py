import http.server as server
import socketserver
import json
import os,sys,inspect

# Import classes and Handlers
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
classes_dir = os.path.join(current_dir, "classes")
sys.path.insert(0,classes_dir) 
from Messages import Messages
from CheckUrls import CheckUrls

class PyJSONHandler(server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
    def do_GET(s):
        """
        Respond to a GET request.
        """
        url = CheckUrls.checkUrl(s)
        if(url == "root"):
            s.do_Response(Messages.default_response, Messages.ok_status)
        else:
            if(url == "accepted_value"):
                s.do_Response(Messages.ok_message, Messages.ok_status)
            else:
                s.do_Response(Messages.fail_message, Messages.not_found_status)
    def do_ResponseOK(s, response):
        '''
        Send OK Response
        '''
        s.send_response(200)
        s.do_Response(response)
    def do_Response(s, response, status):
        ''' 
        Send Response and status
        '''
        s.send_response(status)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write(response.encode("utf-8"))
        s.end_headers()