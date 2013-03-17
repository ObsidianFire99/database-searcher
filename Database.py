print "-+"*960
global dbchoice
dbchoice = "null"
import resources
global databaselist
databaselist = []
global searchlist
searchlist = []
global searchreturn
searchreturn = []
global files
files = []
global titles
titles = []

def sreturn(tx, count, query):
   print "-+"*20
   print count, tx, query
   for item in searchreturn:
        if not item[0] == "~":
            print ""
        print item
   print "-+"*20
   print ""
   start()

def normsearch(query):
   global searchreturn
   if dbchoice == "null":
      print "You need to choose a Database."
      start()
   searchreturn = []
   count = 0
   startsearch = False
   for item in searchlist:
        if item == query:
            for newitem in searchlist:
                if not newitem[0] == "~" and startsearch == True:
                    break
                if newitem == query:
                    startsearch = True
                if startsearch == True:
                    searchreturn.append(newitem)
            count = count + 1
   sreturn("Matches For: ", count, query)

def critsearch(query):
   global searchreturn
   if dbchoice == "null":
      print "You need to choose a Database."
      start()
   searchreturn = []
   founditem = []
   currentiteml = []
   count = 0
   startsearch = False
   found = False
   for item in searchlist:
       if not item[0] == "~":
           if found == True:
               for i in currentiteml:
                   searchreturn.append(i)
               found = False
           currentiteml = []
       if item == query:
           found = True
           count = count + 1
       currentiteml.append(item)
   sreturn("Items with Criteria: ", count, query)


def search():
   query = raw_input("Enter your search query: ")
   if query[0] == "~":
       critsearch(query)
   else:
       normsearch(query)

def getdb(xlist):
    global searchlist
    global dbchoice
    searchlist = []
    count = 0
    while True:
        if count == len(xlist):
            break
        dbchoice = files[xlist[count] - 1]
        try:
            infile = open(dbchoice, "r")
        except(IOError):
            print "The path to your database is broken."
            start()
        for line in infile:
            if not line[0] == "-":
                searchlist.append(line.strip("\n"))
        count = count + 1
    infile.close()
    start()

def choosedb():
    global titles
    global files
    titles = []
    files = []
    c = 1
    lastlinefile = True
    lastlinetitle = False
    infile = open("Config.txt", "r")
    for line in infile:
        line = line.strip()
        if not line[0] == "-":
            if line[0] == "#":
                if lastlinefile == False:
                    print "Your Config File has either an extra title or is missing a path."
                    lastlinetitle = False
                    lastlinefile = True
                elif lastlinefile == True:
                    titles.append(line.strip("#"))
                    lastlinetitle = True
                    lastlinefile = False
            else:
                if lastlinetitle == True:
                    files.append(line.strip("\n"))
                    lastlinetitle = False
                    lastlinefile = True
                elif lastlinetitle == False:
                    titles.append("Untitled Database")
                    files.append(line.strip())
                    lastlinefile = True
    itemnum = 1
    for item in titles:
        print str(itemnum) + ". " + item + " - " + str(files[itemnum - 1])
        itemnum = itemnum + 1
    print ""
    print "Choose a database. To choose multiple databases type all of it's numbers"
    print "with no space (e.g. 13 to choose databases 1 and 3)."
    print "Type 0 to load all Databases"
    choice = input("Enter The Number(s) of your chosen Database: ")
    print "-+"*20
    runc = 1
    choicelist = []
    if choice == 0:
        while not runc > len(files):
            choicelist.append(runc)
            runc = runc + 1
    else:
        choicelist = list(resources.splitdig(choice))
    getdb(choicelist)

def start():
    cont = raw_input("(S)earch or (C)hoose a Database: ")
    if cont == "S":
        search()
    elif cont == "C":
        choosedb()
    else:
        start()
start()
