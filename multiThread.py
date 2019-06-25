import threading
import itertools

threads = []
possibilities = ['0','1','2','3','4','5','6','7','8','9']
nbCaracter = 4
password = 1234


def checkPass(attempt, password):
    passToCheck = "".join(attempt)
    if passToCheck == passToCheck:
        return passToCheck
    return False

def testFunction(possibilities, nbCaracter, password, nbThread):
    i = 0
    x = 0
    listAttempt = []
    y = len(possibilities)**nbCaracter
    for attempt in itertools.product(possibilities, repeat=nbCaracter):
        listAttempt.append(attempt)
    while i < y:
        thread = threading.Thread(target = checkPass, args = (listAttempt[i], password))
        thread.start()
        res = thread.join()
        i += 2
        print thread
testFunction(possibilities, nbCaracter, password, 1)