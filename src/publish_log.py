from stream_log import generate_log_line
import logging
from google.cloud import pubsub_v1
import random
import time

PROJECT_ID = "streaming-data-piplines"
TOPIC = "userlogs"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID,TOPIC)


def publish(publisher,topic,msg):
    data =msg.encode('utf-8')
    return publisher.publish(topic_path,data=data)

def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(TOPIC, message_future.exception()))
    else:
        print(message_future.result())

if __name__ == '__main__':

    while True:
        line = generate_log_line()
        print(line)
        message_future = publish(publisher, topic_path, line)
        message_future.add_done_callback(callback)

        sleep_time = random.choice(range(1, 3, 1))
        time.sleep(sleep_time)