import threading
from listener.filemonitor import ListenForFiles
import logging
import sys



def listen_daemon():
    listen = ListenForFiles(r"D:\dev\hacknotts\23\Filerize\test_files")
    listen.run()



def main():
    daemon = threading.Thread(target=listen_daemon)
    func2 = threading.Thread(target=func)
    daemon.start()
    func2.start()

main()