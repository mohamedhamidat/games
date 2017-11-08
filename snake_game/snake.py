class Snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.total = 0
        self.tail = []
        self.width = 30
        self.green =  (0, 200, 0)

    def can_eat(self, food):
        if self.x == food[0] and self.y == food[1]:
             self.total += 1
             self.tail.append(food)
             return True
        return False

    def change_direction(self, x , y):
        self.xspeed = x
        self.yspeed = y
    
    def update(self, scale):
        for i in range(len(self.tail) -1):
            self.tail[i] = self.tail[i+1]

        if self.total >=1 : 
            self.tail[self.total -1] = [self.x , self.y]
        
        self.x += self.xspeed * scale
        self.y += self.yspeed * scale
    
    def draw(self, pygame, game_display,):
        for i in range(len(self.tail)):
            self.rect(pygame, game_display, self.tail[i][0], self.tail[i][1], self.width, self.width, self.green)
        
        self.rect(pygame, game_display,self.x, self.y, self.width, self.width, self.green)
    
    def rect(self, pygame, game_display, thingX, thingY, thingW, thingH, color):
        """draw random things (car or anything)""" 
        pygame.draw.rect(game_display, color, [thingX, thingY, thingW, thingH])
    
    def is_dead(self):
        """
        check if new position of snake already exists in tail snake
        """
        if [self.x, self.y] in self.tail: 
            return True
        return False
        