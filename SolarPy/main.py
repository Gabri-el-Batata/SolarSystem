import pygame
import planet

pygame.init() # Inicializa o modulo

# Decidir uma altura e largura para a janela que será aberta

WIDTH, HEIGHT = 800, 800 # Altura e largura da janela

# Contrução da janela

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

BLACK = (0, 0, 0) # Cor preta em RGB

# Quando estamos trabalhando com um tipo de "jogo",
# Precisamos que ocorra um loop na janela do "jogo", para que ela não abra e feche instantaneamente
# Então fazemos:

def main():

    run = True
    clock = pygame.time.Clock() # Esse relógio é essencialmente a velocidade do jogo.

    sun = planet.Planet("Sun", 0, 0, 20, (255, 255, 0), 1.989 * 10**30, WIN)
    sun.sun = True

    # Precisamos da velocidade de translação do planeta (y_vel)

    earth = planet.Planet("Earth", -1* planet.Planet.AU, 0, 16, (0, 0, 255), 5.9742 * 10**24, WIN)
    earth.y_vel = 29.783 * 1000

    mars = planet.Planet("Mars", -1.524 * planet.Planet.AU, 0, 12, (255, 0, 0), 6.39 * 10**23, WIN)
    mars.y_vel = 24.077 * 1000

    mercury = planet.Planet("Mercury", 0.387 * planet.Planet.AU, 0, 8, (0,255,0), 3.30 * 10**23, WIN)
    mercury.y_vel = -47.4 * 1000

    venus = planet.Planet("Venus", 0.723 * planet.Planet.AU, 0, 14, (255, 255, 255), 4.8686 * 10**24, WIN)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) # 60 quadros p/ segundo
        WIN.fill(BLACK)
        #pygame.display.update() # Estamos atualizando o display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)

            planet.draw(WIN, (WIDTH, HEIGHT))

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()