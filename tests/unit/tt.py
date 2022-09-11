
from threading import Thread
from time import sleep
import os, sys

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..'))
server_path = os.path.join(ROOT_DIR, 'server')
server_file = server_path + '/controller.py'
def server():
    exec(open(server_file).read())
    print("r")
      
if __name__ == '__main__':
    # thread = Thread(target=server)
    # thread.start()
    server()
    # sleep(3)
