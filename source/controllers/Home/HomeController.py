
class HomeController():
    def __init__(self, request):
        self.request = request

    def index(self):
        print(self.request)
        return {}