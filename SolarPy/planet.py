import pygame
import math

class Planet():
    # Constantes que serão utilizadas
    AU = 149.6e6 * 1000 # Unidade astronomica (distancia da terra ao sol), em metros
    G = 6.67428e-11 # Constante gravitacional
    SCALE = 230/AU #1AU = 100 pixels
    TIMESTEP = 3600 * 24 # 1 dia em segundos. Essa vai ser a velocidade da atualização da simulção


    def __init__(self, name, x, y, radius, color, mass, win):
        self.x = x # Posição x na tela
        self.y = y # Posição y na tela
        self.radius = radius # Raio do planeta
        self.color = color   # Cor do planeta
        self.mass = mass     # Massa do planeta
        self.name = name     # Nome do Planeta
        self.win = win       # Tela (Screen)

        self.orbit = [] 
        self.sun = False # Se for o sol, não queremos desenhar sua orbita
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win, dimensions):

        WIDTH1, HEIGHT1 = dimensions

        x = self.x * self.SCALE + WIDTH1/2
        y = self.y * self.SCALE + HEIGHT1/2

        fonte = pygame.font.get_default_font()
        fontesys = pygame.font.SysFont(fonte, 50) 
        txttela = fontesys.render(f"{self.name}", 1, (255,0,255))
        

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH1/2
                y = y * self.SCALE + HEIGHT1/2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, (updated_points), 2)
         
        pygame.draw.circle(win, self.color, (x,y), self.radius)
        win.blit(txttela,(x, y))

    def attraction(self, other):

        # Essa função é para calcular a força de atração gravitacional dos outros planetas e do sol sobre o planeta self.
        # Essa parte é mais fisica.

        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(math.pow(distance_x, 2) + pow(distance_y, 2))

        if other.sun:
            self.distance_to_sun = distance

        force = (self.G * self.mass * other.mass) / math.pow(distance, 2)
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return (force_x, force_y)

    def update_position(self, planets):

        # Essa função é para atualizar as posições dos planetas no display

        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        if not self.sun:
            
            # Estamos somandos, pois, essencialmente, isso fará com que o planeta mude sua direção

            self.x_vel += (total_fx/self.mass) * self.TIMESTEP 
            self.y_vel += (total_fy/self.mass) * self.TIMESTEP

            self.x += self.x_vel * self.TIMESTEP  
            self.y += self.y_vel * self.TIMESTEP

            self.orbit.append((self.x, self.y))     