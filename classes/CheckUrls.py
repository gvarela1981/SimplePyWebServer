import json

class CheckUrls():
    def checkUrl(s):    
        checkUrl= s.path[0:].split('/')
        # if url is domain.com/
        if(checkUrl[1] == ''):
            return "root"
        # if url is domain.com/something
        else:
            acceptedValues = [
                                'catalog.xlsx',
                                'catalog.csv'
                            ]

            # Ignore first '/' from request string is useless
            requestesHeader = s.path[1:].split('/')
            dict_s = dict(s.headers)
            if str(requestesHeader[0]) in acceptedValues:
                json_response = json.dumps({'status':'Test OK'})
                return "accepted_value"
            else:
                return "unsupported_value"