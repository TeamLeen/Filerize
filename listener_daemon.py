import threading
from listen.filelistener import ListenForFiles

def listen_daemon():
    listen = ListenForFiles(r"D:\dev\hacknotts\23\Filerize\test_files")
    listen.run()

def func():
    print("Thread 2 start")

def main():
    daemon = threading.Thread(target=listen_daemon)
    func2 = threading.Thread(target=func)
    daemon.start()
    func2.start()



main()