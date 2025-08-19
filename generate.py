import os
import sys
import signal
import requests
from io import BytesIO

def download_list(url, filename, method='GET', data=None):
    try:
      
        headers = {'Content-Type': 'application/x-www-form-urlencoded'} if data else {}
        response = requests.request(method, url, headers=headers, data=data)

       
        if response.status_code != 200:
            print(f"Error downloading {filename}: {response.text}")
            return

        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} successfully!")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

def signal_handler(sig, frame):
    print("\nTerminating download process...")
    sys.exit(0)

def main():

    signal.signal(signal.SIGINT, signal_handler)  
    signal.signal(signal.SIGTERM, signal_handler) 


    download_list(
        "https://raw.githubusercontent.com/monperrus/crawler-user-agents/master/crawler-user-agents.json", 
        "crawler-user-agents.json", 
        method='GET'
    )

    download_list(
        "https://user-agents.net/download", 
        "user-agents-bots.txt", 
        method='POST', 
        data="crawler=true&download=txt"
    )

if __name__ == "__main__":
    main()
