from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RPCServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_server(self):
        class RequestHandler(SimpleXMLRPCRequestHandler):
            rpc_paths = ('/rpc',)

        server = SimpleXMLRPCServer((host, port), requestHandler=RequestHandler)
        server.register_introspection_functions()
        server.register_function(receive_data, 'rpc_callback')
        server.serve_forever()

    def rpc_callback(ident, request):
        return 0

