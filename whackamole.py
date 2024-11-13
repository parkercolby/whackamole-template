import pygame, random

def draw_grid(screen):
    for i in range(1, 16):
        pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))
    for i in range(1, 20):
        pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32,640))


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        check = (16,16)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    rx = random.randrange(0, 19)
                    ry = random.randrange(0, 15)
                    check = (16 * (rx * 2 + 1), 16 * (ry * 2 + 1))
                    if check != pos:
                        screen.blit(mole_image, mole_image.get_rect(center=check))
                        pygame.display.flip()
                    else:
                        while check == pos:
                            rx = random.randrange(0, 19)
                            ry = random.randrange(0, 15)
                            check = (16 * (rx * 2 + 1), 16 * (ry * 2 + 1))
                        screen.blit(mole_image, mole_image.get_rect(center=check))
                        pygame.display.flip()
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(center=check))
            pygame.display.flip()
            clock.tick(60)






    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
