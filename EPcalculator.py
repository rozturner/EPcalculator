# Each Way/Extra Place calculator
# Created by Roz Turner, 2022
# IO formula = (EP profit/QL) + 1

def backdata():
    global stake
    stake = float(input("Enter E/W back stake: "))
    global backodds 
    backodds = float(input("Enter back odds: "))
    global bplaces 
    bplaces = float(input("Enter bookie places: "))
    global bplaceodds 
    bplaceodds = float(input("Enter place payout (e.g. 1/5): 1 / "))
    
   

def laydata():
    global winlay 
    winlay = float(input("Enter win lay odds: "))
    global placelay 
    placelay = float(input("Enter place lay odds: "))
    
def backplacecalc():
    p1 = 1/bplaceodds
    p2 = 1-p1
    p3 = backodds*p2
    global calcpodds
    calcpodds = round(backodds-p3, 2)+1
    return calcpodds
    
      
def winlaystake(x, y, z):
    global wlstake 
    wlstake = round((x/y)*z,2)
    return wlstake
    
def placelaystake(x, y, z):
    global plstake 
    plstake = round((x/y)*z, 2)
    return plstake

def pliability():
    global pliab 
    pliab = round((plstake*placelay)-plstake, 2)
    return pliab
    
def wliability():
    global wliab 
    wliab = round((wlstake*winlay)-wlstake, 2)
    return wliab

def liability():
    global liab 
    liab = wliab+pliab
    

def placewin(x, y):  #bookie
    global pwin
    pwin = round((x*y)-x, 2)
    

def backwin(x, y):  #bookie
    global bwin 
    bwin = round((x*y)-x,2)+pwin
    
    
def laywin():
    global lwin
    lwin = wlstake
    
def layplacewin():
    global lpwin
    lpwin = plstake    


#Calculate various QLs based on outcomes    
def firstplace():
    global ql_1 
    ql_1 = round(bwin-liab, 2)
    

def placemarket():
    global ql_2 
    ql_2 = round(((lwin+pwin)-pliab)-stake, 2)
    
    
def ep_hit():
    global hit
    hit = (pwin+lwin+lpwin)
    
def loser():
    global ql_3 
    ql_3 = round((wlstake+plstake)-(stake*2), 2)
    
def ep_profit():
    global eprof 
    eprof = round(hit-stake, 2)
    
def avgql():
    global aql
    aql = (ql_1+ql_2+ql_3)/3
    
    
def calculateIO():
    global io 
    io = round(0-(eprof // aql), 2)+1
    

print(" ")
print("Welcome to the offline Extra Place (EP) Calculator!")
print(" ")
print("Enter the values as prompted to calculate your lay stakes, QL, EP profit, and IO.")    
print(" ")
print("Thanks to Profit Accumulator (https://www.profitaccumulator.co.uk) for the formula!")
print(" ")

while True:
    #Get input
    backdata()
    laydata()

    #Run the calculations
    backplacecalc()
    winlaystake(backodds, winlay, stake)
    print("Calculated place odds: ", calcpodds)
    placelaystake(calcpodds, placelay, stake)
    
    wliability()
    pliability()
    liability()
    placewin(stake, calcpodds)
    backwin(stake, backodds) 
    laywin()
    layplacewin()
    firstplace()
    placemarket()
    ep_hit()
    loser()
    avgql()
    ep_profit()
    calculateIO()

    #Show lay bet details
    print(" ")
    print("******************************************************************************")
    print(" ")
    print("Lay bet details:")
    print(" ")
    print("Win lay stake: £", wlstake)
    print("Place lay stake: £", plstake)
    print("Liability: £", liab)
    print(" ")

    #Show profit details
    print("******************************************************************************")
    print(" ")
    print("If your EP hits, you will make a profit of £",eprof,".")
    print(" ")
    print("Qualifying loss outcomes: ")
    print(" ")
    print("1st place: £", ql_1)
    print("Within place market: £", ql_2)
    print("Outside all places: £", ql_3)
    print("Expected QL (average of all): £", round(aql, 2))
    print(" ")
    print("ql_1 = £",ql_1,",","ql_2 = £",ql_2,",","ql_3 = £",ql_3)
    print("Implied Odds (IO): ", io)
    print(" ")
    print(" ")
    again = input("New calculation? (y/n): ")
    if again == "y":
        continue
    else:
        print(" ")
        print("Good luck smashing the bookies!")
        break