from flask import Response


class HomeController():
    def __init__(self, request):
        self.request = request

    def index(self):
        return Response(response="Home", status=200)