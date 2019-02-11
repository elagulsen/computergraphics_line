from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 - x0) != 0:
        m = (y1 - y0)/(x1 - x0)
    else:
        m = 17 #arbitrary positive number > 1 - slope is actually undefined.
    if (m > 0 and x0 > x1) or (m < 0 and x0 < x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x,y = x0, y0
    a = y1 - y0
    b = x0 - x1
        
    if m <= 1 and m >= 0: #octants one, five
        d = (2*a) + b
        while x <= x1:
            plot(screen, color, x,y)
            if d > 0:
                y += 1
                d += 2*b
            x += 1
            d += 2*a
    elif m > 1: #octants two, six
        d = a+ 2*b
        while y <= y1:
            plot(screen, color, x,y)
            if d < 0:
                x += 1
                d += 2*a
            y += 1
            d += 2*b
    elif m >= -1 and m < 0: #octants four, eight
        d = (2*a) + b
        while x >= x1:
            plot(screen, color, x,y)
            if d > 0:
                y += 1
                d -= 2*b
            x -= 1
            d += 2*a
    elif m < -1: #octants three, seven
        d = a+ 2*b
        while y <= y1:
            plot(screen, color, x,y)
            if d < 0:
                x -= 1
                d += 2*a
            y += 1
            d -= 2*b
    
