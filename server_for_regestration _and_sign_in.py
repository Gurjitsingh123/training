from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import hashlib
import mysql.connector
import cgi, cgitb
hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary']=bytes(pdict["boundary"],'utf=8')
        content_len=int(self.headers.get('content-length'))
        pdict['CONTENT-LENGTH']=content_len
        if self.path=='/signup':
            if ctype=='multipart/form-data':
                fields=cgi.parse_multipart(self.rfile,pdict)
                email=fields.get('email')
                password1=fields.get('password')
                password2=hashlib.md5(password1[0].encode())
                password=password2.hexdigest()
                self.send_response(301)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="training")
                mycursor=connection.cursor()
                stmt="INSERT INTO `reg`(`id`, `password`) VALUES ('{}','{}')".format(email[0],password)
                try:
                    mycursor.execute("CREATE TABLE IF NOT EXISTS reg (id  VARCHAR(200) , password VARCHAR(200), PRIMARY KEY(id));")
                    mycursor.execute(stmt)
                    connection.commit()
                    self.wfile.write(bytes( "Content-type:text/html/\r\n\r\n".encode()))
                    self.wfile.write(bytes("<html>".encode()))
                    self.wfile.write(bytes("<head>".encode()))
                    self.wfile.write(bytes("<title>Hello - Saving data to database</title>".encode()))
                    self.wfile.write(bytes("</head>".encode()))
                    self.wfile.write(bytes("<body>".encode()))
                    self.wfile.write(bytes("<h2>data saved:<br>name:{}<br>lastname:{}</h2>".format(email,password).encode()))
                    self.wfile.write(bytes("</body>".encode()))
                    self.wfile.write(bytes("</html>".encode()))
                except:
                    print("data is not saved")    
                    connection.close()
        if self.path=='/signin':
            if ctype=='multipart/form-data':
                fields=cgi.parse_multipart(self.rfile,pdict)
                email=fields.get('email')
                password1=fields.get('password')
                password2=hashlib.md5(password1[0].encode())
                password=password2.hexdigest()
                self.send_response(301)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="training")
                mycursor=connection.cursor()
                try:
                    stmt="SELECT password FROM `reg` WHERE id='{}'".format(email[0])
                    mycursor.execute(stmt)
                    for i in mycursor:
                        pass
                    data=i[0]
                    connection.commit()
                    if data[0]==password[0]:
                        #self.Set-Cookie:UserID = 
                        #self.Set-Cookie:Password = 
                       # self.Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT";
                        #self.Set-Cookie:Domain = 
                       # self.Set-Cookie:Path = /
                        #self.wfile.write(bytes( "".encode()))
                        self.wfile.write(bytes("<html>".encode()))
                        self.wfile.write(bytes("<head>".encode()))
                        self.wfile.write(bytes("<title>signing_in</title>".encode()))
                        self.wfile.write(bytes("</head>".encode()))
                        self.wfile.write(bytes("<body>".encode()))
                        self.wfile.write(bytes("<h2>sign in sucessfull</h2>".encode()))
                        self.wfile.write(bytes("</body>".encode()))
                        self.wfile.write(bytes("</html>".encode()))
                    else:
                        writing=''
                        writing+='<html> <head><title>signing_in</title><body>password incorrect</body></head></html>'
                        self.wfile.write(bytes(writing.encode()))              
                except:
                    print("data is not aprropriate")    
                    connection.close()
   
    def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.wfile.write(bytes( "Content-type:text/html/bc\r\n\r\n".encode()))
            self.wfile.write(bytes("<html>".encode()))
            self.wfile.write(bytes("<head>".encode()))
            self.wfile.write(bytes("<title>Hello - Second CGI Program</title>".encode()))
            self.wfile.write(bytes("</head>".encode()))
            self.wfile.write(bytes("<body>".encode()))
            self.wfile.write(bytes("<h2>Hello {}</h2>".format(self.path).encode()))
            self.wfile.write(bytes("</body>".encode()))
            self.wfile.write(bytes("</html>".encode()))
          

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")