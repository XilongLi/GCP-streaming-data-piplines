from src.stream_log import generate_log_line
import random
import time
import logging

if __name__ == '__main__':
    while True:
        print (generate_log_line())
        sleep_time = random.choice(range(1, 3, 1))
        time.sleep(sleep_time)