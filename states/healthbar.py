pygame.init()
screen = pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
player = pygame.sprite.GroupSingle(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.sprite.get_health(200)


    screen.fill((30,30,30))
    player.draw(screen)
    player.update()
    pygame.display.update()
    clock.tick(60)