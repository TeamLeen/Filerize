# import time module, Observer, FileSystemEventHandler
import asyncio
import logging
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import filetools.fstructs as fstructs
import filetools.ftools as ftools


class Handler(FileSystemEventHandler):

    event_buffer = []

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
            if os.path.exists(event.src_path):
                label = asyncio.run(ftools.label_file(path=event.src_path))
                # Don't move if not labelled 
                if label is not None:
                    ftools.move_single(
                        src=event.src_path, dst_root=label, filename=event.src_path.split("\\")[-1])


class ListenForFiles:

    def __init__(self, dir):
        self.observer = Observer()
        self.directory = dir

    def run(self):

        print("File Observor Daemon has started")

        event_handler = Handler()
        self.observer.schedule(
            event_handler, path=self.directory, recursive=True)
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
