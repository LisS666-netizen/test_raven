

class Base:


    DOMAIN_URL = None
    API_REQUESTS = None

    headers = []

    def __init__(self, domain, req=None):
        self.DOMAIN_URL = domain
        self.API_REQUESTS = req

    def get(self):
        pass