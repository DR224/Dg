import random
import sys
import time
def mengetik(s):
     for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.7)

mengetik('cuma belajar terus lah berjuang <user DR224 \n Terima kasih .')

