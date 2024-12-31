from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np
import random
import time

winWidth, winHeight= 700, 800
Path=[(-66.66666666666666, -280), (0, -280), (66.66666666666666, -280), (-66.66666666666666, -240), (0, -240), (66.66666666666666, -240), (-66.66666666666666, -200), (0, -200), (66.66666666666666, -200), (-66.66666666666666, -160), (0, -160), (66.66666666666666, -160), (-66.66666666666666, -120), (0, -120), (66.66666666666666, -120), (-66.66666666666666, 120), (0, 120), (66.66666666666666, 120), (-66.66666666666666, 160), (0, 160), (66.66666666666666, 160), (-66.66666666666666, 200), (0, 200), (66.66666666666666, 200), (-66.66666666666666, 240), (0, 240), (66.66666666666666, 240), (-66.66666666666666, 280), (0, 280), (66.66666666666666, 280), (-280, -66.66666666666666), (-280, 0), (-280, 66.66666666666666), (-240, -66.66666666666666), (-240, 0), (-240, 66.66666666666666), (-200, -66.66666666666666), (-200, 0), (-200, 66.66666666666666), (-160, -66.66666666666666), (-160, 0), (-160, 66.66666666666666), (-120, -66.66666666666666), (-120, 0), (-120, 66.66666666666666), (120, -66.66666666666666), (120, 0), (120, 66.66666666666666), (160, -66.66666666666666), (160, 0), (160, 66.66666666666666), (200, -66.66666666666666), (200, 0), (200, 66.66666666666666), (240, -66.66666666666666), (240, 0), (240, 66.66666666666666), (280, -66.66666666666666), (280, 0), (280, 66.66666666666666)]
player1_Start=[-66.66666666666666,-280]
player2_Start=[66.66666666666666,280]
player1_Path=[(-66.66666666666666, -280), (-66.66666666666666, -240), (-66.66666666666666, -200), (-66.66666666666666, -160), (-66.66666666666666, -120), (-120, -66.66666666666666), (-160, -66.66666666666666), (-200, -66.66666666666666), (-240, -66.66666666666666), (-280, -66.66666666666666), (-280, 0), (-280, 66.66666666666666), (-240, 66.66666666666666), (-200, 66.66666666666666), (-160, 66.66666666666666), (-120, 66.66666666666666), (-66.66666666666666, 120), (-66.66666666666666, 160), (-66.66666666666666, 200), (-66.66666666666666, 240), (-66.66666666666666, 280), (0, 280), (66.66666666666666, 280), (66.66666666666666, 240), (66.66666666666666, 200), (66.66666666666666, 160), (66.66666666666666, 120), (120, 66.66666666666666), (160, 66.66666666666666), (200, 66.66666666666666), (240, 66.66666666666666), (280, 66.66666666666666), (280, 0), (280, -66.66666666666666), (240, -66.66666666666666), (200, -66.66666666666666), (160, -66.66666666666666), (120, -66.66666666666666), (66.66666666666666, -120), (66.66666666666666, -160), (66.66666666666666, -200), (66.66666666666666, -240), (66.66666666666666, -280), (0, -280), (0, -240), (0, -200), (0, -160), (0, -120), (0, 0)]
player2_Path=[(66.66666666666666, 280), (66.66666666666666, 240), (66.66666666666666, 200), (66.66666666666666, 160), (66.66666666666666, 120), (120, 66.66666666666666), (160, 66.66666666666666), (200, 66.66666666666666), (240, 66.66666666666666), (280, 66.66666666666666), (280, 0), (280, -66.66666666666666), (240, -66.66666666666666), (200, -66.66666666666666), (160, -66.66666666666666), (120, -66.66666666666666), (66.66666666666666, -120), (66.66666666666666, -160), (66.66666666666666, -200), (66.66666666666666, -240), (66.66666666666666, -280), (0, -280), (-66.66666666666666, -280), (-66.66666666666666, -240), (-66.66666666666666, -200), (-66.66666666666666, -160), (-66.66666666666666, -120), (-120, -66.66666666666666), (-160, -66.66666666666666), (-200, -66.66666666666666), (-240, -66.66666666666666), (-280, -66.66666666666666), (-280, 0), (-280, 66.66666666666666), (-240, 66.66666666666666), (-200, 66.66666666666666), (-160, 66.66666666666666), (-120, 66.66666666666666), (-66.66666666666666, 120), (-66.66666666666666, 160), (-66.66666666666666, 200), (-66.66666666666666, 240), (-66.66666666666666, 280), (0, 280), (0, 240), (0, 200), (0, 160), (0, 120), (0, 0)]
Dice=0
Player1_pawns=[False,False,False,False]
Player2_pawns=[False,False,False,False]
player1_pawn_rest=[(-230, -230),(-180,-230),(-230,-180),(-180,-180)]
player1_pawn_path=[player1_Start,player1_Start,player1_Start,player1_Start]
player2_pawn_rest=[(230, 230),(180,230),(230,180),(180,180)]
player2_pawn_path=[player2_Start,player2_Start,player2_Start,player2_Start]
turn= "Player 1"
placed_pawn=False
consecutive_sixes=0
Move=0

PLAYER1_GOAL = [(0, 0)] * 4 
PLAYER2_GOAL = [(0, 0)] * 4  


player1_goal_count = 0
player2_goal_count = 0


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18, color=(1.0, 1.0, 1.0)):
    glColor3f(*color)  # Set text color
    glRasterPos2i(x, y)  # Set position
    for char in text:
        glutBitmapCharacter(font, ord(char))  # Draw each character


#Midpoint Line drawing Algorithma
def find_zone(x0, y0, x1, y1):
    #Determine the zone for the line based on its slope
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) > abs(dy):  # Horizontal dominant
        if dx >= 0 and dy >= 0:
            return 0  # Zone 0
        elif dx <= 0 and dy >= 0:
            return 3  # Zone 3
        elif dx <= 0 and dy <= 0:
            return 4  # Zone 4
        elif dx >= 0 and dy <= 0:
            return 7  # Zone 7
    else:  # Vertical dominant
        if dx >= 0 and dy >= 0:
            return 1  # Zone 1
        elif dx <= 0 and dy >= 0:
            return 2  # Zone 2
        elif dx <= 0 and dy <= 0:
            return 5  # Zone 5
        elif dx >= 0 and dy <= 0:
            return 6  # Zone 6

def to_zone_0(x, y, zone):
    #Transform (x, y) to Zone 0
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def from_zone_0(x, y, zone):
    #Transform (x, y) from Zone 0 back to the original zone
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def midpoint_line(x0, y0, x1, y1):
    points = []
    zone = find_zone(x0, y0, x1, y1)
    # Transform points to Zone 0
    x0, y0 = to_zone_0(x0, y0, zone)
    x1, y1 = to_zone_0(x1, y1, zone)

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dy - dx
    x, y = x0, y0

    while x <= x1:
        # Transform point back to the original zone
        points.append(from_zone_0(x, y, zone))
        x += 1
        if d < 0:
            d += 2 * dy
        else:
            y += 1
            d += 2 * (dy - dx)
    
    return points

#Midpoint Circle drawing Algorithm
def midpoint_circle(cx, cy, r):
    points = []
    x = 0
    y = r
    d = 1 - r  

    # Add the initial points of the first octant
    points+=generate_symmetric_points(cx, cy, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        points+=generate_symmetric_points(cx, cy, x, y)
    
    return points

def generate_symmetric_points(cx, cy, x, y):
    return [
        (cx + x, cy + y),  # Octant 1
        (cx - x, cy + y),  # Octant 2
        (cx + x, cy - y),  # Octant 7
        (cx - x, cy - y),  # Octant 8
        (cx + y, cy + x),  # Octant 3
        (cx - y, cy + x),  # Octant 4
        (cx + y, cy - x),  # Octant 6
        (cx - y, cy - x),  # Octant 5
    ]


# Function to draw a pixel at (x, y)
def draw_pixel(x, y, color=(1.0, 1.0, 1.0)):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw a line using Midpoint Line Drawing Algorithm
def draw_line(x0, y0, x1, y1, color=(1.0, 1.0, 1.0)):
    points = midpoint_line(x0, y0, x1, y1)
    for point in points:
        draw_pixel(point[0], point[1], color)

# Function to draw a circle using Midpoint Circle Drawing Algorithm
def draw_circle(cx, cy, r, color=(1.0, 1.0, 1.0)):
    points = midpoint_circle(cx, cy, r)
    for point in points:
        draw_pixel(point[0], point[1], color)


def fill_circle(cx, cy, r, color=(1.0, 1.0, 1.0)):
    # while r>0:
    #     draw_circle(cx, cy, r, color)
    #     r-=1

    glColor3f(*color)  # Set the fill color
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)  # Center of the circle
    num_segments = 100  # Number of segments for smoother circle
    
    # Generate circle points
    for i in range(num_segments + 1):  # Extra segment to close the circle
        angle = 2.0 * 3.1415926 * i / num_segments  # Angle in radians
        x = cx + (r * math.cos(angle))
        y = cy + (r * math.sin(angle))
        glVertex2f(x, y)
    glEnd()

def draw_court(cx,cy,d,color):
    draw_line(cx-d, cy-d, cx+d, cy-d, color)
    draw_line(cx-d, cy-d, cx-d, cy+d, color)
    draw_line(cx-d, cy+d, cx+d, cy+d, color)
    draw_line(cx+d, cy-d, cx+d, cy+d, color)

def draw_goal(cx,cy,d,color):
    fill_Triangle(cx+d, cy-d, cx+d, cy+d, color[4])
    fill_Triangle(cx-d, cy+d, cx+d, cy+d, color[2])
    fill_Triangle(cx-d, cy-d, cx-d, cy+d, color[3])
    fill_Triangle(cx-d, cy-d, cx+d, cy-d, color[1])

    draw_line(cx-d, cy-d, cx+d, cy-d, color[0])
    draw_line(cx-d, cy-d, cx-d, cy+d, color[0])
    draw_line(cx-d, cy+d, cx+d, cy+d, color[0])
    draw_line(cx+d, cy-d, cx+d, cy+d, color[0])

    draw_line(cx-d, cy-d, cx+d, cy+d, color[0])
    draw_line(cx-d, cy+d, cx+d, cy-d, color[0])


def fill_Triangle(x0, y0, x1, y1, color):
    if (x0 and x1)>0 and x0==x1:
        while x0>0:
            draw_line(x0, y0, x1, y1, color)
            x0-=1
            x1-=1
            y0+=1
            y1-=1
    elif (y0 and y1)>0 and y0==y1:
        while y0>0:
            draw_line(x0, y0, x1, y1, color)
            x0+=1
            x1-=1
            y0-=1
            y1-=1
    elif (y0 and y1)<0 and y0==y1:
        while y0<0:
            draw_line(x0, y0, x1, y1, color)
            x0+=1
            x1-=1
            y0+=1
            y1+=1

    elif (x0 and x1)<0 and x0==x1:
        while x0<0:
            draw_line(x0, y0, x1, y1, color)
            x0+=1
            x1+=1
            y0+=1
            y1-=1



def draw_path_blocks(cx,cy,d1,d2,color):
    draw_line(cx-d1, cy-d2, cx+d1, cy-d2, color)
    draw_line(cx-d1, cy-d2, cx-d1, cy+d2, color)
    draw_line(cx-d1, cy+d2, cx+d1, cy+d2, color)
    draw_line(cx+d1, cy-d2, cx+d1, cy+d2, color)


def draw_path(color):
    global Path
    k=[-66.66666666666666,66.66666666666666,0]
    #Player 1
    for i in range(-280,-80,40):
        for j in k:
            if math.floor(j)==0:
                draw_path_blocks(j,i,(200/3)/2,(200/5)/2,color[1])
            else:
                draw_path_blocks(j,i,(200/3)/2,(200/5)/2,color[0])
            

    #Player 2
    for i in range(120,320,40):
        for j in k:
            if math.floor(j)==0:
                draw_path_blocks(j,i,(200/3)/2,(200/5)/2,color[2])
            else:
                draw_path_blocks(j,i,(200/3)/2,(200/5)/2,color[0])
            

    #Player 3
    for i in range(-280,-80,40):
        for j in k:
            if math.floor(j)==0:
                draw_path_blocks(i,j,(200/5)/2,(200/3)/2,color[3])
            else:
                draw_path_blocks(i,j,(200/5)/2,(200/3)/2,color[0])
            

    #Player 4
    for i in range(120,320,40):
        for j in k:
            if math.floor(j)==0:
                draw_path_blocks(i,j,(200/5)/2,(200/3)/2,color[4])
            else:
                draw_path_blocks(i,j,(200/5)/2,(200/3)/2,color[0])
            

   


# Function to draw the Ludo board
def draw_board():
    glClear(GL_COLOR_BUFFER_BIT)

   
    player1_color = (1, 0.0, 0.0)  # Red
    player3_color = (0.0, 1, 0.0)  # Blue
    player2_color = (0.0, 0.0, 1)  # Green
    player4_color = (0.996078431372549, 0.8352941176470589, 0.0)  # Yellow
    path_color = (0.0, 1.0, 0.0)     # Green

    # Draw the main board outline
    draw_line(-300, -300, 300, -300, color=(1, 1, 1))
    draw_line(300, -300, 300, 300, color=(1, 1, 1))
    draw_line(300, 300, -300, 300, color=(1, 1, 1))
    draw_line(-300, 300, -300, -300, color=(1, 1, 1))

    #Court
    draw_court(-200,-200,100,player1_color)
    fill_circle(-200,-200, 100, color=(0.5, 0.0, 0.0))
    draw_circle(-200,-200, 100, color=player1_color)  
    

    draw_court(200,200,100,player2_color)
    fill_circle(200,200,100, color=(0.0, 0.0, 0.5))
    draw_circle(200,200,100, color=player2_color)    
    

    draw_court(-200,200,100,player3_color)
    fill_circle(-200,200,100, color=(0.0, 0.5, 0.0))
    draw_circle(-200,200,100, color=player3_color)    
    

    draw_court(200,-200,100,player4_color)
    fill_circle(200,-200,100, color=(0.5, 0.5, 0.0))
    draw_circle(200,-200,100, color=player4_color)    
    

    draw_goal(0,0,100,[(1, 1, 1), (0.5, 0.0, 0.0), (0.0, 0.0, 0.5), (0.0, 0.5, 0.0), (0.5, 0.5, 0.0)])

    draw_path([(1, 1, 1), (0.5, 0.0, 0.0), (0.0, 0.0, 0.5), (0.0, 0.5, 0.0), (0.5, 0.5, 0.0)])
    

    
    # Draw home areas for both players


    # draw_text(-180, -180, "Player 1", color=player1_color)
    # draw_text(120, 180, "Player 2", color=player2_color)



def draw_ludo_pawn(cx, cy, player=1, base_radius=15, head_radius=10):
    """
    Draws a Ludo pawn at the specified position with colors based on the player.
    :param cx: Center x-coordinate of the pawn
    :param cy: Center y-coordinate of the pawn
    :param player: Player ID (1 or 2)
    :param base_radius: Radius of the base circle
    :param head_radius: Radius of the head circle
    """
    # Define player colors
    if player == 1:
        color_base = (1.0, 0.0, 0.0)  # Red for Player 1
        color_head = (0.8, 0.4, 0.4)  # Lighter red for Player 1
    elif player == 2:
        color_base = (0.0, 0.0, 1.0)  # Blue for Player 2
        color_head = (0.4, 0.4, 0.8)  # Lighter blue for Player 2
    else:
        color_base = (0.5, 0.5, 0.5)  # Default gray
        color_head = (0.7, 0.7, 0.7)  # Default lighter gray

    # Draw the base circle
    fill_circle(cx, cy, base_radius, color=color_base)

  

    # Draw the head circle
    head_center_y = cy + base_radius / 3 + head_radius  # Position the head above the base
    fill_circle(cx, head_center_y, head_radius, color=color_head)
    

def Player1_pawn():
    global player1_pawn_rest, player1_pawn_path, Player1_pawns
    for i in range(4):
        if Player1_pawns[i]:
            draw_ludo_pawn(player1_pawn_path[i][0],player1_pawn_path[i][1],1)
        else:
            draw_ludo_pawn(player1_pawn_rest[i][0],player1_pawn_rest[i][1],1)
        

def Player2_pawn():
    global player2_pawn_rest, player2_pawn_path, Player2_pawns
    for i in range(4):
        if Player2_pawns[i]:
            
            draw_ludo_pawn(player2_pawn_path[i][0],player2_pawn_path[i][1],2)
        else:
            
            draw_ludo_pawn(player2_pawn_rest[i][0],player2_pawn_rest[i][1],2)



def axis():
    glColor3f(1, 1, 1)
    glPointSize(2)                
    x0, y0 = 0, -winHeight/2
    x1, y1 = 0, winHeight/2
    points1 = midpoint_line(x0, y0, x1, y1)

    x0, y0 = winWidth/2, 0
    x1, y1 = -winWidth/2, 0
    points2 = midpoint_line(x0, y0, x1, y1)

    glBegin(GL_POINTS)
    for x, y in points1:
        glVertex2f(x , y)  
    for x, y in points2:
        glVertex2f(x , y)  
    glEnd()




#Mouse Handler
def convert_coordinate(x, y):
    global winWidth, winHeight
    a = x - (winWidth / 2)
    b = (winHeight / 2) - y
    return a, b



def handle_pawn_click(x, y, pawn_path, full_path, player_goal_count, opponent_pawn_path):
    """
    Handles clicking a pawn and moving it along the path.
    Returns True if the move was successful, False otherwise.
    """
    global player1_goal_count, player2_goal_count

    for i in range(4):
        pawn_x, pawn_y = pawn_path[i]

        if pawn_x - 15 <= x <= pawn_x + 15 and pawn_y - 15 <= y <= pawn_y + 15:
            new_position_index = full_path.index((pawn_x, pawn_y)) + Move

            if pawn_path[i] == (0, 0):
                print("This pawn has already reached the goal. Select another pawn.")
                return False

            if new_position_index >= len(full_path):
                if new_position_index == len(full_path):
                    print(f"{turn} pawn reached the goal!")
                    pawn_path[i] = (0, 0)
                    player_goal_count += 1
                    check_winner()
                    return True
                else:
                    print("Move exceeds the path. Invalid move.")
                    return False

            print(f"{turn} pawn selected.")
            new_position = full_path[new_position_index]
            pawn_path[i] = new_position

            # Handle kill logic
            kill=check_for_kill(new_position, opponent_pawn_path)
            if kill[0]=="Kill":
                # Kill opponent's pawn
                reset_opponent_pawn(opponent_pawn_path, turn, kill[1])
                print(f"{turn} killed an opponent's pawn!")
                return True

            if pawn_path[i] == (0, 0):
                print(f"{turn} pawn reached the goal!")
                player_goal_count += 1
                check_winner()
            return True

    print(f"Invalid pawn selection for {turn}.")
    return False

def check_for_kill(position, opponent_pawn_path):
    """
    Check if the player's pawn has landed on the opponent's pawn and kill it.
    """
    for opponent_pawn in opponent_pawn_path:
        if position == opponent_pawn:
            return ["Kill", opponent_pawn_path.index(opponent_pawn)]
    return "No kill"

def reset_opponent_pawn(opponent_pawn_path, player, position):
    """
    Resets the opponent's pawn back to their specific rest position.
    """
    if player == "Player 1":
        # Reset Player 2's pawn to rest positions
        opponent_pawn_rest = [(230, 230), (180, 230), (230, 180), (180, 180)]
        opponent_pawn_path[position] = opponent_pawn_rest[position]
    else:
        # Reset Player 1's pawn to rest positions
        opponent_pawn_rest = [(-230, -230), (-180, -230), (-230, -180), (-180, -180)]
        opponent_pawn_path[position] = opponent_pawn_rest[position]


def check_winner():
    """
    Check if any player has won the game.
    """
    global player1_goal_count, player2_goal_count

    if player1_goal_count == 4:
        print("Player 1 has won the game!")
        game_over("Player 1")
    elif player2_goal_count == 4:
        print("Player 2 has won the game!")
        game_over("Player 2")

def game_over(winner):
    """
    Ends the game and displays the winner.
    """
    print(f"Congratulations {winner}! The game is over.")
    


def mouseClick(button, state, x, y):
    global turn, Move, placed_pawn, player1_pawn_path, player2_pawn_path

    x, y = convert_coordinate(x, y)

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if Move == 0:  
            print(f"{turn} has no moves left. Roll the dice first.")
            return

        if turn == "Player 1":
            if handle_pawn_click(x, y, player1_pawn_path, player1_Path, player1_goal_count, player2_pawn_path):
                Move = 0
                turn = "Player 2" if Dice != 6 else "Player 1"
                placed_pawn = False
        else:  
            if handle_pawn_click(x, y, player2_pawn_path, player2_Path, player2_goal_count, player1_pawn_path):
                Move = 0
                turn = "Player 1" if Dice != 6 else "Player 2"
                placed_pawn = False

        glutPostRedisplay()


def draw_dice(dice):
    for i in range(40,-1,-1):
        draw_court(0,0,i,(0,0,0))

    if dice==1:
        fill_circle(0,0,10)
    elif dice==2:
        fill_circle(-20,20,10)
        fill_circle(20,-20,10)
    elif dice==3:
        fill_circle(-20,20,10)
        fill_circle(0,0,10)
        fill_circle(20,-20,10)
    elif dice==4:
        fill_circle(-20,20,10)
        fill_circle(20,20,10)
        fill_circle(-20,-20,10)
        fill_circle(20,-20,10)
    elif dice==5:
        fill_circle(-20,20,10)
        fill_circle(20,20,10)
        fill_circle(-20,-20,10)
        fill_circle(20,-20,10)
        fill_circle(0,0,10)
    elif dice==6:
        fill_circle(-20,20,10)
        fill_circle(20,20,10)
        fill_circle(-20,-20,10)
        fill_circle(20,-20,10)
        fill_circle(-20,0,10)
        fill_circle(20,0,10)
    else:
        pass

#Keyboard Handlerr
def KeyClick(key, x, y):
    global Dice, placed_pawn, turn, consecutive_sixes, Move, Player1_pawns, Player2_pawns

    if key == b' ':  # Roll the dice
        Dice = random.randint(1, 6)
        print(f"{turn} rolled: {Dice}")
        if Move>0 :
            print("You have to move the pawn first")
            return
        # Dice animation
        animation_duration = 1.0
        start_time = time.time()
        angle = 0
        while time.time() - start_time < animation_duration:
            glPushMatrix()
            glRotatef(angle, 0, 0, 1)
            draw_dice(Dice)
            glPopMatrix()

            angle += 10
            if angle >= 360:
                angle = 0

            glutSwapBuffers()
            time.sleep(0.05)

        # Draw final dice face
        glPushMatrix()
        glTranslatef(0, 0, 0)
        draw_dice(Dice)
        glPopMatrix()
        glutPostRedisplay()

        # Handle a roll of 6
        if Dice == 6:
            consecutive_sixes += 1
            if consecutive_sixes >= 3:  # After three consecutive 6s, switch turn
                print(f"{turn} rolled 6 three times. Switching turn.")
                turn = "Player 2" if turn == "Player 1" else "Player 1"
                consecutive_sixes = 0
                Move = 0
                placed_pawn = False
                return

            print(f"{turn} rolled a 6! Can roll again or place a pawn.")
            Move += Dice
            placed_pawn = True  # Allow placing a pawn

        else:  # If no 6 is rolled
            if not any(Player1_pawns if turn == "Player 1" else Player2_pawns):  # No pawns placed
                print("No pawn placed. Cannot roll the dice unless you roll a 6.")
                turn = "Player 2" if turn == "Player 1" else "Player 1"  # Switch turn
                consecutive_sixes = 0
                return

            Move += Dice
            consecutive_sixes = 0
            print(f"{turn} can move {Dice} steps.")

        glutPostRedisplay()

    elif key == b'r':  # Place a pawn
        if Move >= 6:  # Only allow placement if enough moves available
            if turn == "Player 1":
                for i in range(4):
                    if not Player1_pawns[i]:
                        Player1_pawns[i] = True
                        print(f"Player 1 placed pawn {i + 1}.")
                        break
                else:
                    print("Player 1 has no more pawns to place.")
                    return
            else:
                for i in range(4):
                    if not Player2_pawns[i]:
                        Player2_pawns[i] = True
                        print(f"Player 2 placed pawn {i + 1}.")
                        break
                else:
                    print("Player 2 has no more pawns to place.")
                    return

            Move -= 6  # Deduct move for placing a pawn
            if Move == 0:  # End turn if no moves left
                placed_pawn = False
                turn = "Player 2" if turn == "Player 1" else "Player 1"

        else:
            print("Cannot place a pawn without rolling a 6.")

        glutPostRedisplay()


        



def animate():
        
        glutPostRedisplay() 

    
# Display function to render the line
def display():
    global player1_Start, player2_Start, Dice
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_board()
    draw_dice(Dice)
    Player1_pawn()
    Player2_pawn()
   
    # draw_line(player1_Start[0], player1_Start[1], player2_Start[0], player2_Start[1], color=(1, 0, 0))
    # axis()
    glFlush()  # Render now

# Main function to initialize OpenGL and create a window

def iterate():
    glViewport(0, 0, winWidth, winHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-winWidth/2, winWidth/2, -winHeight/2, winHeight/2, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(winWidth, winHeight) 
glutInitWindowPosition(600, 150)
wind = glutCreateWindow(b"Game Box") #window name

# Register the display callback
glutDisplayFunc(display)
glutMouseFunc(mouseClick)
glutKeyboardFunc(KeyClick)
# glutIdleFunc(animate)

# Start the main loop
glutMainLoop()

