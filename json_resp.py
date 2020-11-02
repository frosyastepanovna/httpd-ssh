#!/usr/bin/python3
import base64
import os
import logging
from cgi import parse_qs, escape


logging.basicConfig(filename='/tmp/example.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

logging.debug(os.environ['QUERY_STRING']);



#
#message = "Python is fun"
#message_bytes = message.encode('ascii')
#base64_bytes = base64.b64encode(message_bytes)
#base64_message = base64_bytes.decode('ascii')

#print(base64_message)


print ("Content-type: application/json\n\n")
print
print
#print ("<html><head>")
#print ("</head><body>")
temp = os.environ['REQUEST_SCHEME']
#message_bytes = temp.encode('ascii')
#base64_bytes = base64.b64encode(message_bytes)

#'QUERY_STRING': 'param1=value1¶m2=value2',

#str(int(os.environ['SERVER_PORT']))
#str(os.environ['SERVER_PORT'])

data = '''{
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "'''+str(int(os.environ['CONTENT_LENGTH']))+'''"
    }
}'''

print(data)





#print ('</body></html>')
