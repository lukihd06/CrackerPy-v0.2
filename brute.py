#! /usr/bin/python
import itertools
import hashlib
import time

# all the type of caracter we can use.
lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
special = ['!','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']

possibilities = lowerCase+upperCase+special+number
password = "zzzz"
nbCaracter = 4


# method to encrypt in sha256 a string
def encryptString(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# compare generated password with the original password
def checkPass(attempt, myHash):
    passToCheck = "".join(attempt)
    hashToCheck = encryptString(passToCheck)
    if hashToCheck == myHash:
        return passToCheck
    return False

# method for generate cartesian product and compare it with checkPass() function
def crack(password, nbCaracter, possibilities):
    start = time.time()
    returnDict = {} 
    for attempt in itertools.product(possibilities, repeat=nbCaracter):
        solution = checkPass(attempt, password)
        print attempt
        if solution != False:
            realTime = time.time()-start
            result = 'Le mot de passe est "' + solution + '" .'
            minutes, seconds = divmod(int(realTime), 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            years, days = divmod(days, 365)
            timeSpent = 'Temps pour le trouver : {:d} ans, {:02d} jours, {:02d} heures, {:02d} minutes et {:02d} secondes'.format(years, days, hours, minutes, seconds)
            returnDict = {
                "password": result,
                "time": timeSpent
            }
            return returnDict         

# method for completing the next one, she's the same as crack() but is preset for the next function
def crackTest(password, nbCaracter, possibilities):
    start = time.time()
    for attempt in itertools.product(possibilities, repeat=nbCaracter):
        solution = checkPass(attempt, password)
        print attempt
        if solution != False:
            return time.time()-start  

# method use to know how many iteration per seconds the conputer can execute
def howManyIterationPerSeconds():
    operationTime = crackTest(encryptString("9999"), 4, possibilities)
    return len(possibilities)**nbCaracter/operationTime

# method use to show the theoric time it will need to crack the password
def timeToCrackTheoric(possibilities, nbCaracter, iterationPerSeconds):
    seconds = len(possibilities)**nbCaracter/iterationPerSeconds
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    res = 'Temps estime maximal pour trouver le mot de passe : {:d} ans, {:02d} jours, {:02d} heures, {:02d} minutes et {:02d} secondes '.format(years, days, hours, minutes, seconds)
    return res