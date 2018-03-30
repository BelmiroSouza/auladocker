import logging
import http.server
import socketserver
import getpass

class MyHTTPHandle(http.server.SimpleHTTPRequestHandle):
    def log_message(self, format, *args):
        logging.info("%s-- [%s] %s\n"% (
            self.client_adress[0],
            self.log_date_time_string(),
            format%args
        ))
logging.basicConfig(
    filename='/log/http-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandle())
logging.info('Inicializando .....')
PORT = 8000

httpd = socketserver.TCPServer(("", PORT), MyHTTPHandler)
logging.info('escutando a porta: %s', PORT)
logging.info('usuario: %s', getPass().getuser())
hhtpd.serve_forever()

