def checkBanana(peel):
    count = 0
    document = open(peel)
    read = document.read()
    words = read.split()
    for i in words:
        i = i.lower()
        if (i == "banana"):
            count = count + 1
    print(("There are ")+ str(count)+(" bananas in this text."))

checkBanana("bananafile.txt")
