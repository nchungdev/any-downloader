class FUserInfo:
    def __init__(self, app_key, user_agent, mail, password, ssid, token):
        self.app_key = app_key
        self.user_agent = user_agent
        self.mail = mail
        self.password = password
        self.ssid = ssid
        self.token = token

    @classmethod
    def from_dict(cls, adict):
        room = FUserInfo(
            app_key=adict['app_key'],
            user_agent=adict['user_agent'],
            mail=adict['mail'],
            password=adict['password'],
            ssid=adict['ssid'],
            token=adict['token']
        )

        return room

    def to_dict(self):
        return {
            'app_key': self.app_key,
            'user_agent': self.user_agent,
            'mail': self.mail,
            'password': self.password,
            'ssid': self.ssid,
            'token': self.token
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
