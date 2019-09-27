from locust import HttpLocust, TaskSet, task, exception
import Queue
import time

UID_START = 19070000

def generate_uid():
    mq = Queue.Queue()
    for index in range(2000):
        mq.put_nowait(UID_START+index)

    return mq


USER_CREDENTIALS = generate_uid()


class UserBehavior(object):

    def on_start(self):
        t = time.time();
        if not USER_CREDENTIALS.empty():
            self._uid = USER_CREDENTIALS.get_nowait()
            self._device_id = "a5dc83cc" + str(self._uid)

    def use(self):
        print self._uid , "--" , self._device_id
        raise exception.StopLocust


user = UserBehavior()
user.on_start()
user.use()