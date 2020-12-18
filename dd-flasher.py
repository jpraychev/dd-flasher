#!/usr/bin/python3

import sys
import time
import signal
from subprocess import Popen, PIPE

dd = Popen(['dd'] + sys.argv[1:], stderr=PIPE)
while dd.poll() is None:
    time.sleep(.3)
    dd.send_signal(signal.SIGUSR1)
    while True:
        lines = dd.stderr.readline()
        if b'bytes' in lines:
            print(lines.decode('utf-8').strip(), end = '\r')
            break
        
print(dd.stderr.read())
