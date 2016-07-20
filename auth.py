import urllib2

from ntlm import HTTPNtlmAuthHandler


class Auth:
    def __init__(self, url, username, password):
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, username, password)
        self.ntlm = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
