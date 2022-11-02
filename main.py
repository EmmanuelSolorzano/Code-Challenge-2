def graficar(p1x, p1y, p2x, p2y):
    if p1x < p2x and p1y < p2y:
        aux = p1x
        p1x = p2x
        p2x = aux    
        aux = p1y
        p1y = p2y
        p2y = aux
        
    dx = p2x - p1x
    dy = p2y - p1y
    
    if dx >= dy:
        supLimit = abs(dx)
    else:
        supLimit = abs(dy)

    x = p1x
    y = p1y
    point(x,y)
    dx = (dx / supLimit)
    dy = (dy / supLimit)
    
    for i in range(supLimit):
        x += dx
        y += dy
        point(x,y)

size(400,400)
graficar(1,2,100,20)
graficar(10,200,50,10)
graficar(300,300,10,10)
graficar(200,300,250,50)
graficar(350,350,100,300)