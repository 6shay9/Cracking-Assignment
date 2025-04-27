The goal of this project was to automate the process of discovering the correct PIN code required to access a local server running on 127.0.0.1 (localhost) via port 8888. The server expected a POST request containing a magicNumber parameter. A correct PIN submission would return a success message.

The challenge was to programmatically try all possible 3-digit PINs (000 to 999) and stop when the correct PIN was found, while handling server responses appropriately, including any rate-limiting instructions like "slow down."

First, I needed to understand the flow of the HTTP request and the expected server behavior:

Send an HTTP POST request to /verify with form data containing a PIN.

Interpret the server’s response to determine if the submitted PIN was correct.

Adjust the speed of requests if the server asked to slow down.
I chose to use Python’s built-in socket module to manually handle the TCP connection and HTTP communication.

I defined the host (127.0.0.1) and port (8888) variables.

I decided to use a with statement when working with sockets to ensure proper resource management (the socket closes automatically).
Each request had to include:

A request line (POST /verify HTTP/1.1).

Headers including Host, Content-Type, Content-Length, and Connection: close.

A properly formatted body: magicNumber=XXX, where XXX was the current 3-digit PIN.
A loop (for pin_number in range(1000)) was created to systematically try every PIN from 000 to 999:

Each number was formatted to always be 3 digits long (e.g., 001, 045).

The loop attempted sending each PIN via a fresh socket connection to avoid any leftover connection issues.
After sending a request:

The program read all server responses in chunks of up to 4096 bytes until no more data was received.

The entire response was decoded to a string while ignoring any decoding errors.

The program then checked:

If the response contained success indicators like "congratulations", "access granted", or "welcome", it meant the correct PIN was found, and the program printed it and terminated the loop.

If the response included "slow down", it increased the delay between attempts by 0.5 seconds to respect the server’s pacing request.

Otherwise, it continued trying the next PIN.

https://drive.google.com/drive/folders/1qWpHEz7RlpfPj9feFefbuStzzh7nTK6f?usp=drive_link = link of the drive
