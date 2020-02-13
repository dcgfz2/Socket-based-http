# Socket-based-http
Python socket implementation of http server/client 

Server should run without input but path of files to be hosted are relative to the directory the script is in. By default it host on port 1400 but this is easly adjustable
*For best results put http files in the same directory as script*

Client needs 3 inputs to function, the cmd should look as follows:
> ./client_browser.py <server ip/domain> <port> <filename>
