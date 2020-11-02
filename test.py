#!/usr/bin/python3
import os
import verification
import logging

#import logging
#logging.basicConfig(filename='/tmp/example.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')



#Hello. environ({'UNIQUE_ID': 'X3S3z2lUyMn4zHDRE-H4UQAAANU', 
#'HTTP_HOST': '10.1.1.27', 
#'HTTP_CONNECTION': 'keep-alive', 
#'HTTP_CACHE_CONTROL': 'max-age=0', 
#'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
#'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 OPR/71.0.3770.138', 
#'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
#'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 
#'HTTP_ACCEPT_LANGUAGE': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
#'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin', 
#'SERVER_SIGNATURE': '', 
#'SERVER_SOFTWARE': 'Apache/2.4.37 (Oracle Linux)', 
#'SERVER_NAME': '10.1.1.27', 
#'SERVER_ADDR': '10.1.1.27', 
#'SERVER_PORT': '80', 
#'REMOTE_ADDR': '10.1.1.95', 
#'DOCUMENT_ROOT': '/var/www/html', 
#'REQUEST_SCHEME': 'http', 
#'CONTEXT_PREFIX': '/cgi-bin/', 
#'CONTEXT_DOCUMENT_ROOT': '/var/www/cgi-bin/', 
#'SERVER_ADMIN': 'root@localhost', 
#'SCRIPT_FILENAME': '/var/www/cgi-bin/test.py', 
#'REMOTE_PORT': '64442', 
#'GATEWAY_INTERFACE': 'CGI/1.1', 
#'SERVER_PROTOCOL': 'HTTP/1.1', 
#'REQUEST_METHOD': 'GET', 
#'QUERY_STRING': 'param1=value1¶m2=value2', 
#'REQUEST_URI': '/cgi-bin/test.py?param1=value1¶m2=value2', 
#'SCRIPT_NAME': '/cgi-bin/test.py', 'LC_CTYPE': 'C.UTF-8'})

output = ''



print ("Content-type: text/html\n\n")
print
print
print ("<html><head>")
#print ('''<script language="javascript">
print ('''<script>
    function a()
    {document.getElementById('info').innerHTML = 'kod5';
    document.getElementById('info1').value = 'kod5';}
    function b()
    {document.getElementById('info').innerHTML = 'kod6';        
    document.getElementById('info1').value = 'kod6';
    var xhr = new XMLHttpRequest();
var url = "/cgi-bin/json_resp.py";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json.email + ", " + json.password);
    }
};
var host        = "qwqewre123host";
var login       = "qwqewre123login";
var pass        = "qwqewre123pass";
var preexecute  = "qwqewre123preexecute";


var data = JSON.stringify({"host": host,"login": login,"pass": pass,"preexecute": preexecute});
xhr.send(data);



    }  


    
</script>''')

print ("")
print ("")

print ("</head><body>")
print ("Hello.")
if os.environ['REQUEST_METHOD'] == 'GET':
    logging.info('GET')
    output = verification.process_GET()
if os.environ['REQUEST_METHOD'] == 'POST':
    logging.info('POST')
    output = verification.process_GET()
    #print(qq)
print (os.environ)
#print (output)

print ('<textarea id="info1" rows="10" cols="45" name="text"></textarea></p><div id="info"></div></body></html>')
