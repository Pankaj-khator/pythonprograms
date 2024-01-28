orizinal = open('donket.txt')
textorizinal = orizinal.read()
orizinal.close()

newfile = open('copiedtext','w' )
newfile.write(textorizinal)
newfile.close()