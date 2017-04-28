import re
cLang = "english"
#cLang = "spanish"
toStrip = cLang+"1.txt"
with open(toStrip, "r") as f:
    for line in f:
    	line = re.sub('[0-9.!@\-#$?<>{\}\[\]%^&*()/,\'";:]', '', line)
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            print cleanedLine
