def setup():
    size(1154,540)
    
x = 0   

def draw():
    global x

    noStroke()
    
    if x >= 1154:
        x = 0

    background(72,61,139)
    x += 4

    fill(240,248,255)
    ellipse(100,100,200,200)
    
    fill(72,61,139)
    ellipse(150,130,150,150)
    
    fill(50,205,50)
    rect(0,350,1154,240)
    
    stroke(1)
    fill(205,133,63)
    rect(780,100,280,350)
    
    fill(255,255,102)
    rect(820,150,75,75)
    rect(940,150,75,75)
    rect(820,250,75,75)
    
    fill(222,184,135)
    rect(940,250,75,175)
    triangle(730,100,1110,100,920,10)
    
    fill(0)
    rect(820,185,75,10)
    rect(850,150,10,75)
    rect(820,285,75,10)
    rect(850,250,10,75)
    rect(940,185,75,10)
    rect(970,150,10,75)
    
    fill(205,133,63)
    ellipse(955,340,15,15)
    
    noStroke()
    fill(255)
    ellipse(x,100,100,100)
    rect(x - 50,100,100,50)
    ellipse(x-34,150,33,40)
    ellipse(x ,150,33,40)
    ellipse(x +34,150,33,40)
    fill(0)
    ellipse(x-25,100,35,35)
    ellipse(x+25,100,35,35)
    
    fill(255)
    ellipse(x-100,275,100,100)
    rect(x - 150,275,100,50)
    ellipse(x-134,325,33,40)
    ellipse(x -100,325,33,40)
    ellipse(x -66,325,33,40)
    
    fill(0)
    ellipse(x-125,275,35,35)
    ellipse(x-75,275,35,35)
    
    fill(85,107,47)
    rect(855,370,10,25)
        
    fill(255,165,0)
    stroke(1)
    ellipse(860,400,75,35)
    ellipse(860,400,60,35)
    ellipse(860,400,35,35)
    
    noStroke()
    fill(85,107,47)
    rect(835,420,10,25)
        
    fill(255,165,0)
    stroke(1)
    ellipse(840,450,75,35)
    ellipse(840,450,60,35)
    ellipse(840,450,35,35)
    
    noStroke()
    fill(105)
    ellipse(150,430,50,50)
    rect(125,430,50,50)
    
    ellipse(250,400,50,50)
    rect(225,400,50,50)
    
    ellipse(370,460,50,50)
    rect(345,460,50,50)
    
    ellipse(450,412,50,50)
    rect(425,412,50,50)
    
    ellipse(570,445,50,50)
    rect(545,445,50,50)
    
    ellipse(680,380,50,50)
    rect(655,380,50,50)
