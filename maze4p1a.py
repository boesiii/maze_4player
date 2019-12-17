import pygame
 
 
def draw(display_surf,image_surf):
   bx = 0
   by = 0
   for i in range(0,M*N):
       if maze[ bx + (by*M) ] == 1:
           display_surf.blit(image_surf,( bx * 44 , by * 44))
           blocks.append([bx*44,by*44])
 
       bx = bx + 1
       if bx > M-1:
           bx = 0
           by = by + 1
 
 
blocks = []

window_height = 616 # 14 rows
window_width = 792 # 18 columns
M = 18 # columns
N = 14 # rows
vel = 44
x = 0
y = 44
p2x = 748 
p2y = 528
player_width = 44
 
maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
         1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,
         1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,
         1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,
         1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,
         1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,
         1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,
         1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,
         1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,
         1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,
         1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,
         1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
 
               
pygame.init()
display_surf = pygame.display.set_mode((window_width,window_height), pygame.HWSURFACE)
pygame.display.set_caption('Pygame pythonspot.com example')
running = True
# image_surf = pygame.image.load("player44.png")
image_surf = pygame.image.load("player_me.png")
p2_surf = pygame.image.load("lyla_44.png")
block_surf = pygame.image.load("block44.png")
 
display_surf.fill((0,0,0))
display_surf.blit(image_surf,(x,y))
display_surf.blit(p2_surf,(p2x,p2y))
draw(display_surf, block_surf)
# print (blocks)
pygame.display.flip()
 
 
while running:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
 
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            running = False  # Ends the game loop
           
    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT] and x > vel and [x-vel,y] not in blocks:
        x -= vel
 
    if keys[pygame.K_RIGHT] and x < window_width - vel - player_width and [x+vel,y] not in blocks:
        x += vel
 
    if keys[pygame.K_UP] and y > vel and [x,y-vel] not in blocks:
        y -= vel
 
    if keys[pygame.K_DOWN] and y < window_height - vel - player_width and [x,y+vel] not in blocks:
        y += vel
        
    # player 2    
    if keys[pygame.K_a] and p2x > vel and [p2x-vel,p2y] not in blocks:
        p2x -= vel
 
    if keys[pygame.K_d] and p2x < window_width - vel - player_width and [p2x+vel,p2y] not in blocks:
        p2x += vel
 
    if keys[pygame.K_w] and p2y > vel and [p2x,p2y-vel] not in blocks:
        p2y -= vel
 
    if keys[pygame.K_s] and p2y < window_height - vel - player_width and [p2x,p2y+vel] not in blocks:
        p2y += vel
       
    # pygame.draw.rect(win, (255,0,0), (x, y, width, height))  
    display_surf.fill((0,0,0))
    draw(display_surf, block_surf)
    display_surf.blit(image_surf,(x,y))
    display_surf.blit(p2_surf,(p2x,p2y))
    pygame.display.update()
   
 
pygame.quit()