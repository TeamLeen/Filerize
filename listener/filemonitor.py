# import time module, Observer, FileSystemEventHandler
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
  
        # elif event.event_type == 'created':
        #     # Event is created, you can process it now
        #     logging.info("Watchdog received created event - % s." % event.src_path)
        # elif event.event_type == 'modified':
        #     # Event is modified, you can process it now
        #     logging.info("Watchdog received modified event - % s." % event.src_path)

        if event.event_type == 'created' or event.event_type == 'modified':
            print(event.src_path)

class ListenForFiles:
  
    def __init__(self, dir):
        self.observer = Observer()
        self.directory = dir
  
    def run(self):
        
        logging.info("FileMonitor Daemon has started")

        event_handler = Handler()
        self.observer.schedule(event_handler, path=self.directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()

              
  
if __name__ == '__main__':
    watch = ListenForFiles(".\\")
    watch.run()