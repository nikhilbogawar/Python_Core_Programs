#   Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.
def connect(host, port=3306, protocol='TCP'):
    print(f"Connecting to {host} on port {port} using {protocol} protocol.")
connect('localhost')
connect('localhost', 8080, 'UDP')