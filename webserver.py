from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import mysql.connector
import cgi, cgitb
hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary']=bytes(pdict["boundary"],'utf=8')
        #content_len=int(self.headers.get('content-length'))
        #pdict['CONTENT-LENGTH']=content_len
        if ctype=='multipart/form-data':
            fields=cgi.parse_multipart(self.rfile,pdict)
            name=fields.get('fname')
            last=fields.get('lname')
            print(name,last)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            connection=mysql.connector.connect(host="localhost",user="root",password="",database="training")
            mycursor=connection.cursor()
            stmt="INSERT INTO `formdata`(`id`, `email`, `password`) VALUES ('','{}','{}')".format(name,last)
            try:
                mycursor.execute("CREATE TABLE IF NOT EXISTS formdata (id INT NOT NULL AUTO_INCREMENT , email VARCHAR(200) , password VARCHAR(200), PRIMARY KEY(id));")
                mycursor.execute(stmt)
                connection.commit()
                print("done")
            except:
                print("none")    
                connection.close()
            self.wfile.write(bytes( "Content-type:text/html/bc\r\n\r\n".encode()))
            self.wfile.write(bytes("<html>".encode()))
            self.wfile.write(bytes("<head>".encode()))
            self.wfile.write(bytes("<title>Hello - Saving data to database</title>".encode()))
            self.wfile.write(bytes("</head>".encode()))
            self.wfile.write(bytes("<body>".encode()))
            self.wfile.write(bytes("<h2>data saved:<br>name:{}<br>lastname:{}</h2>".format(name,last).encode()))
            self.wfile.write(bytes("</body>".encode()))
            self.wfile.write(bytes("</html>".encode()))
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