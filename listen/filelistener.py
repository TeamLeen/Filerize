# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)

class ListenForFiles:
  
    def __init__(self):
        self.observer = Observer()
        self.directory = None
    
    def set_directory(self, dir):
        self.directory = dir
  
    def run(self):
        print("running")
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()

              
  
# if __name__ == '__main__':
#     watch = ListenFile()
#     watch.run()