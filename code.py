import socket
import time

HOST = '127.0.0.1'
PORT = 8888

def send_pin(pin):
    body = f"pin={pin}"
    request = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())

        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data

    return response.decode()
