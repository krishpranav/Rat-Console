#!/usr/bin/env/python3

class SCREENSHOT:

    SC_DATA = b""

    
    def __init__(self):
        self.generate()
    

    def generate(self):
        obj = io.BytesIO()
        im = pyscreenshot.grab()
        im.save(obj, format="PNG")
        self.SC_DATA = obj.getvalue()