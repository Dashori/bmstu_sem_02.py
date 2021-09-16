import pygame as p

sc = p.display.set_mode((800, 600))
sc.fill("white")

##мышь которая бежит вправо 
mouse_surf = p.image.load('mouse.jpg').convert()
mouse = p.transform.scale(mouse_surf, (mouse_surf.get_width() // 4,mouse_surf.get_height() // 4)) 
mouse_rect = sc.get_rect(center=(100, 600))

##мышь которая бежит влево
mouse_2_surf = p.image.load('mouse_2.jpg').convert()
mouse_2 = p.transform.scale(mouse_2_surf, (mouse_2_surf.get_width() // 4,mouse_2_surf.get_height() // 4)) 
mouse_2_rect = sc.get_rect(center=(700, 600))

##общая для всех сыров картинка
cheese_surf = p.image.load('maasdam.jpg').convert()
cheese = p.transform.scale(cheese_surf, (cheese_surf.get_width() // 22, cheese_surf.get_height() // 22))

ang=0
x=0
cheese_8 = p.transform.rotate(cheese, ang)
cheese_8_rect = cheese_8.get_rect(center=(x, 360))

##мышеловка
mousetrap_surf=p.image.load('mousetrap.jpg').convert()
mousetrap = p.transform.scale(mousetrap_surf, (mousetrap_surf.get_width() // 3, mousetrap_surf.get_height() // 3))
mousetrap_rect=mousetrap.get_rect(center=(750,400))

sc.blit(mousetrap, mousetrap_rect)
p.display.update()


run=True

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    ##отрисовка сыров  
    ang+=8
    cheese_1 = p.transform.rotate(cheese, ang)
    cheese_rect = cheese_1.get_rect(center=(50, 200))
    sc.blit(cheese_1, cheese_rect)    
    p.display.update()
    

    cheese_2 = p.transform.rotate(cheese, ang)
    cheese_rect_2 = cheese_2.get_rect(center=(150, 100))
    sc.blit(cheese_2, cheese_rect_2)
    p.display.update()

    cheese_3 = p.transform.rotate(cheese, ang)
    cheese_rect_3 = cheese_3.get_rect(center=(280, 220))
    sc.blit(cheese_3, cheese_rect_3)
    p.display.update()

    cheese_4 = p.transform.rotate(cheese, ang+3)
    cheese_rect_4 = cheese_4.get_rect(center=(380, 100))
    sc.blit(cheese_4, cheese_rect_4)
    p.display.update()

    cheese_5 = p.transform.rotate(cheese, ang)
    cheese_rect_5 = cheese_5.get_rect(center=(500, 220))
    sc.blit(cheese_5, cheese_rect_5)
    p.display.update()

    cheese_6 = p.transform.rotate(cheese, ang)
    cheese_rect_6 = cheese_6.get_rect(center=(650, 100))
    sc.blit(cheese_6, cheese_rect_6)
    p.display.update()

    cheese_7 = p.transform.rotate(cheese, ang)
    cheese_rect_7 = cheese_7.get_rect(center=(760, 220))
    sc.blit(cheese_7, cheese_rect_7)
    p.display.update()
    
    
    
    ##бег мышки
    
    if mouse_rect.x + 200 < mousetrap_rect.x:
        

        x+=2
        if cheese_8_rect.x + 120 < mousetrap_rect.x:
            cheese_8 = p.transform.rotate(cheese, ang)
            cheese_8_rect = cheese_8.get_rect(center=(x, 380))
        else:
            p.draw.polygon(sc,"white",[[cheese_8_rect.x,mouse_2_rect.y],[cheese_8_rect.x+100,mouse_2_rect.y],
                                 [cheese_8_rect.x+100,mouse_2_rect.y+200],[cheese_8_rect.x,mouse_2_rect.y+200]])

        sc.blit(cheese_8, cheese_8_rect)

        sc.blit(mouse, mouse_rect)
        mouse_rect.x += 2
        p.draw.polygon(sc,"white",[[mouse_rect.x-2,mouse_rect.y],[mouse_rect.x-10,mouse_rect.y+150],[mouse_rect.x-10,mouse_rect.y+100]])
        
        p.display.update()
        p.time.delay(10)
        
    else:
        sc.blit(mouse_2, mouse_2_rect)
        mouse_2_rect.x -= 2
        p.draw.polygon(sc,"white",[[mouse_2_rect.x+200,mouse_2_rect.y+150],[mouse_2_rect.x+330,mouse_2_rect.y+150],
                                 [mouse_2_rect.x+330,mouse_2_rect.y-20],[mouse_2_rect.x+200,mouse_2_rect.y-20]])
        p.display.update()
        p.time.delay(10)


p.quit()










