def game ():
 return 283


score = game()

filescore = open('highscore.txt')
fileread = filescore.read()
filescore.close()

filescore = open('highscore.txt','w')
if fileread=='':
    filescore.write(str(score))
elif score > int(fileread):
      filescore.write(str(score))

filescore.close()