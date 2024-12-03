import os
import threading
def run_script(script_name):
    os.system(f'python {script_name}')


# twee threads maken
thread1 = threading.Thread(target=run_script, args=('YOLO_detect.py',))
thread2 = threading.Thread(target=run_script, args=('ui.py',))

# beide threads starten
thread1.start()
thread2.start()

# beide threads samenvoegen
thread1.join()
thread2.join()
