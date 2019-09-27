from locust import HttpLocust, TaskSet, task
from lxml import etree
'''
    从response中获取参数
'''

def index(l):
    l.client.get("/")

def stats(l):
    l.client.get("/stats/requests")

class UserBehavior(TaskSet):

    @staticmethod
    def get_session(html):
        tree = etree.HTML(html)
        return tree.xpath("//div[@class='btnbox']/input[@name='session']/@value")[0]

    @task(10)
    def test_log(self):
        html = self.client.get("/login").text
        username = 'test'
        passwd = 'passwd'
        session = self.get_session(html)
        payload={
            'username':username,
            'passwd':passwd,
            'session':session
        }

        self.client.post('/login', data=payload)


class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000
    task_set = UserBehavior
