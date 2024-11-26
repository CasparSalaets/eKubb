import os
import threading
def run_script(script_name):
    os.system(f'python {script_name}')

# Create two threads
thread1 = threading.Thread(target=run_script, args=('YOLO_detect.py',))
thread2 = threading.Thread(target=run_script, args=('ui.py',))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
