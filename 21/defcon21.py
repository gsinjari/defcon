#!/usr/bin/python
# By Govand Sinjari, 2013-07-19, San Diego CA,
# Created for Defcon 21 puzzle contest
# Contact: gsinjari [at] gmail.com
# Filename: defcon21.py, input file name: contest.txt
# Run: python defcon21.py
# license           : MIT
# py version        : 2.7

defcon =[ ["L","B","H","U","N","I","S","R","Q","B","A","R","I","R","C","E","L","J","R","Y","Y"] , ["F","B","S","N","E","S","C","A","V","E","N","G","E","R","H","U","N","T","A","D","B"],["J","E","X","P","L","O","I","T","H","A","C","K","A","T","H","O","N","S","I","B","E"], ["G","U","L","R","C","E","S","V","C","M","R","C","U","R","E","R","V","M","F","L","H"],["B","H","E","I","P","D","N","Y","H","E","K","R","P","U","R","V","A","F","G","Y","A"],["U","R","A","R","P","J","E","U","B","M","J","I","F","G","B","R","S","U","R","G","C"], ["N","G","P","X","W","M","R","F","E","R","M","O","E","W","Y","R","B","O","A","C","K"], ["N","E","N","Q","A","L","O","I","E","P","K","K","R","P","K","K","T","L","H","T","E"], ["K","H","I","I","L","V","F","C","M","H","V","W","T","P","X","S","F","R","A","Z","R"], ["E","O","C","Y","L","Y","K","Y","D","S","T","N","O","M","T","E","T","M","C","M","J"], ["G","L","B","J","O","O","R","P","F","N","E","T","M","R","H","E","P","F","K","Z","E"], ["D","O","I","U","F","A","O","X","A","C","A","S","O","T","P","E","N","P","F","X","O"], ["A","N","C","H","S","P","W","C","K","A","B","H","E","P","R","G","C","K","O","H","P"], ["I","A","Z","C","H","I","T","N","E","E","S","R","S","E","S","A","B","V","R","E","A"], ["N","J","A","W","E","L","E","Z","W","G","U","C","V","A","D","B","B","T","T","A","R"], ["X","L","A","X","E","T","N","Z","O","T","A","I","M","X","R","K","B","B","R","H","D"], ["B","C","I","F","P","I","Y","X","P","Q","D","R","G","L","B","C","M","L","E","B","Y"], ["R","N","S","C","H","E","M","A","V","E","R","S","E","C","H","A","M","P","S","G","F"], ["G","S","T","R","H","B","C","C","N","Z","F","Z","A","V","F","L","X","M","S","A","F"], ["D","X","M","G","R","J","L","T","U","F","P","R","N","G","E","B","F","J","M","K","W"], ["C","T","J","Q","W","D","E","X","E","J","H","E","D","W","M","B","K","K","K","K","K"] ]

filex = open('contest.txt','r')
for contest in filex:
  wordx=list(contest.upper())
  
  for x in range(0,21):
        for y in range(0,21):
                if defcon[x][y] == wordx[0]: 
                           
                    if y < 17 and defcon[x][y+1] == wordx[1]:
                        if defcon[x][y+2] == wordx[2]:
                            if defcon[x][y+3] == wordx[3]:
                                if defcon[x][y+4] == wordx[4]:
                                    print (contest.upper()+"right ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x) + "][" + str(y+1) + "]= "+ defcon[x][y+1] + "  ["+str(x) + "][" + str(y+2) + "]= "+ defcon[x][y+2]+ "  ["+str(x) + "][" + str(y+3) + "]= "+ defcon[x][y+3] + "  ["+str(x) + "][" + str(y+4) + "]= "+ defcon[x][y+4])

                    if x < 17 and defcon[x+1][y] == wordx[1]:
                        if defcon[x+2][y] == wordx[2]:
                            if defcon[x+3][y] == wordx[3]:
                                if defcon[x+4][y] == wordx[4]:     
                                    print (contest.upper()+"down ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x+1) + "][" + str(y) + "]= "+ defcon[x+1][y] + "  ["+str(x+2) + "][" + str(y) + "]= "+ defcon[x+2][y] + "  ["+str(x+3) + "][" + str(y) + "]= "+ defcon[x+3][y] + "  ["+str(x+4) + "][" + str(y) + "]= "+ defcon[x+4][y])

                    if y > 3 and defcon[x][y-1] == wordx[1]:
                        if defcon[x][y-2] == wordx[2]:
                            if defcon[x][y-3] == wordx[3]:
                                if defcon[x][y-4] == wordx[4]:
                                    print (contest.upper()+"<-- ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x) + "][" + str(y-1) + "]= "+ defcon[x][y-1] + "  ["+str(x) + "][" + str(y-2) + "]= "+ defcon[x][y-2] + "  ["+str(x) + "][" + str(y-3) + "]= "+ defcon[x][y-3] + "  ["+str(x) + "][" + str(y-4) + "]= "+ defcon[x][y-4])

                    if defcon[x-1][y] == wordx[1]:
                        if defcon[x-2][y] == wordx[2]:
                            if defcon[x-3][y] == wordx[3]:
                                if defcon[x-4][y] == wordx[4]:
                                    print (contest.upper()+"up ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x-1) + "][" + str(y) + "]= "+ defcon[x-1][y] + "  ["+str(x-2) + "][" + str(y) + "]= "+ defcon[x-2][y] + "  ["+str(x-3) + "][" + str(y) + "]= "+ defcon[x-3][y] + "  ["+str(x-4) + "][" + str(y) + "]= "+ defcon[x-4][y])
 
 
                    if x < 17 and y < 17 and defcon[x+1][y+1] == wordx[1]:
                        if defcon[x+2][y+2] == wordx[2]:
                            if defcon[x+3][y+3] == wordx[3]:
                                if defcon[x+4][y+4] == wordx[4]:
                                    print (contest.upper()+"\ right-down ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x+1) + "][" + str(y+1) + "]= "+ defcon[x+1][y+1] + "  ["+str(x+2) + "][" + str(y+2) + "]= "+ defcon[x+2][y+2] + "  ["+str(x+3) + "][" + str(y+3) + "]= "+ defcon[x+3][y+3]+ "  ["+str(x+4) + "][" + str(y+4) + "]= "+ defcon[x+4][y+4])
                        
                    if defcon[x-1][y-1] == wordx[1]:
                        if defcon[x-2][y-2] == wordx[2]:
                            if defcon[x-3][y-3] == wordx[3]:
                                if defcon[x-4][y-4] == wordx[4]:
                                    print (contest.upper()+"\ up-left["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x-1) + "][" + str(y-1) + "]= "+ defcon[x-1][y-1] + "  ["+str(x-2) + "][" + str(y-2) + "]= "+ defcon[x-2][y-2] + "  ["+str(x-3) + "][" + str(y-3) + "]= "+ defcon[x-3][y-3] + "  ["+str(x-4) + "][" + str(y-4) + "]= "+ defcon[x-4][y-4])
                        
                    if x < 17 and defcon[x+1][y-1] == wordx[1]:
                          if defcon[x+2][y-2] == wordx[2]:
                            if defcon[x+3][y-3] == wordx[3]:
                                if defcon[x+4][y-4] == wordx[4]:
                                    print (contest.upper()+"/ down-left ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x+1) + "][" + str(y-1) + "]= "+ defcon[x+1][y-1] + "  ["+str(x+2) + "][" + str(y-2) + "]= "+ defcon[x+2][y-2] + "  ["+str(x+3) + "][" + str(y-3) + "]= "+ defcon[x+3][y-3] + "  ["+str(x+4) + "][" + str(y-4) + "]= "+ defcon[x+4][y-4])

                    if y < 17 and defcon[x-1][y+1] == wordx[1]:
                        if defcon[x-2][y+2] == wordx[2]:
                            if defcon[x-3][y+3] == wordx[3]:
                                if defcon[x-4][y+4] == wordx[4]:
                                    print (contest.upper()+ "/ up-right ["+str(x) + "][" + str(y) + "]= "+ defcon[x][y] + "  ["+str(x-1) + "][" + str(y+1) + "]= "+ defcon[x-1][y+1] + "  ["+str(x-2) + "][" + str(y+2) + "]= "+ defcon[x-2][y+2] + "  ["+str(x-3) + "][" + str(y+3) + "]= "+ defcon[x-3][y+3] + "  ["+str(x-4) + "][" + str(y+4) + "]= "+ defcon[x-4][y+4])

  print ""