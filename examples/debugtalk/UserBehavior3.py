from locust import HttpLocust, TaskSet, task
import queue
'''
    所有并发虚拟用户共享同一份测试数据，并且保证虚拟用户使用的数据不重复。
    例如，模拟3用户并发注册账号，总共有9个账号，要求注册账号不重复，注册完毕后结束测试
'''


class UserBehavior(TaskSet):


    @task
    def test_register(self):
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            exit(0)

        payload={
            'username':data['username'],
            'passwd':data['passwd']
        }

        self.client.post('/register', data=payload)


class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://127.0.0.1:8089"

    user_data_queue = queue.Queue()
    for index in range(100):
        data = {
            'username':'test%04d' % index,
            'passwd' : 'passwd%04d' %index,
            'email' : 'email%04d' % index
        }
        user_data_queue.put_nowait(data)

    min_wait = 2000
    max_wait = 5000
    task_set = UserBehavior
