from locust import TaskSet, task


def index(l):
    l.client.get("/")

def stats(l):
    l.client.get("/stats/requests")


class UserTasks(TaskSet):
    # one can specify tasks like this
    tasks = [index, stats]
    
    # but it might be convenient to use the @task decorator
    @task
    def page404(self):
        self.client.get("/does_not_exist")

