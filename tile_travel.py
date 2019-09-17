# 1  make variables for the directions and x, y coordinates
# 2  find out out which direction he can take
# 3  ask which for direction input
# 4  move the player
# 5  if the player is on tile 3, 1 the player wins 
# 6  else continue

#TODO:
# Make variables for south, north, east, west, x and y
NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"
X = 1
Y = 1
#TODO:
#Make a function that return the options available
def move_options(x,y):
    n_bool, s_bool, e_bool, w_bool = True, True, True, True
    option_count = 4
    if(x == 1 or (y==1) or (x==3 and y==2)):
        w_bool = False
        option_count -= 1
    if(x == 3 or (y==1) or (x==2 and y==2)):
        e_bool = False
        option_count -= 1
    if(y==3 or (x==2 and y==2)):
        n_bool = False
        option_count -= 1
    if(y==1 or (x==2 and y==3)):
        s_bool = False
        option_count -= 1
    return n_bool, e_bool, s_bool, w_bool, option_count
        

def print_options(n,e,s,w, count):
    print("You can travel: ",end="")
    if(n and count != 1):
        print("(N)orth", end=" or ")
        count -= 1
    elif (n and count == 1):
        print("(N)orth.")
        return None

    if(e and count != 1):
        print("(E)ast", end=" or ")
        count -= 1
    elif (e and count == 1):
        print("(E)ast.")
        return None

    if(s and count != 1):
        print("(S)outh", end=" or ")
        count -= 1
    elif (s and count == 1):
        print("(S)outh.")
        return None

    if(w and count != 1):
        print("(W)est", end=" or ")
        count -= 1
    elif (w and count == 1):
        print("(W)est.")
        return None

#TODO:
# Make a function that moves the player
def move_player(x, y, move):
    if move == NORTH:
        y +=1
    elif move == SOUTH:
        y -= 1
    elif move == WEST:
        x -= 1
    elif move == EAST:
        x += 1
    return x, y

#TODO:
# Ask for input and save it
while True:
    n,e,s,w,count = move_options(X,Y)
    print_options(n,e,s,w,count)
    while True:
        input_str = input("Direction: ").lower()
        if((input_str == NORTH and n) or (input_str == EAST and e) or (input_str == SOUTH and s) or (input_str == WEST and w)):
            break
        else:
            print("Not a valid direction!")
            continue
    X,Y = move_player(X,Y,input_str)
    if X == 3 and Y == 1:
        print("Victory!")
        break


#TODO:
#Check if the player is in a winning position