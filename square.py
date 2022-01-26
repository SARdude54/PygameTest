from scripts.config import *


while running:
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    mx, my = pygame.mouse.get_pos()

    screen.fill(BACKGROUND_COLOR)

    for block in blocks:
        block.draw()

    player.draw()

    chicken.draw()

    line = Line((player_rect.centerx, player_rect.y), (mx, my), screen)

    if not throw:
        circle = Circle(player_rect.centerx, player_rect.y, 10, screen)

    if throw:
        if set_vector.get_x() < 0 and set_vector.get_y() < 0:
            circle.x -= (speed * math.cos(math.radians(set_vector.get_angle())))
            circle.y -= (speed * math.sin(math.radians(set_vector.get_angle())))
        if set_vector.get_x() < 0 and set_vector.get_y() > 0:
            circle.x -= (speed * math.cos(math.radians(set_vector.get_angle())))
            circle.y -= (speed * math.sin(math.radians(set_vector.get_angle())))
        if set_vector.get_y() < 0 and set_vector.get_x() > 0:
            circle.x += (speed * math.cos(math.radians(set_vector.get_angle())))
            circle.y += (speed * math.sin(math.radians(set_vector.get_angle())))
        if set_vector.get_y() > 0 and set_vector.get_x() > 0:
            circle.x += (speed * math.cos(math.radians(set_vector.get_angle())))
            circle.y += (speed * math.sin(math.radians(set_vector.get_angle())))

        if circle.collide(screen.get_width(), 0) or circle.collide(0, 0) or circle.collide(screen.get_width(), block.get_rect().y):
            circle.delete()
            throw = False

        circle.draw_circle()

    if jumping:
        jump -= 1
        player_rect.bottom -= jump
        if jump == 0:
            jumping = False
            jump = 20

    if chicken.rect.bottom < block.rect.y + 10:
        chicken.rect.y += gravity

    if player_rect.bottom < block.rect.y + 10:
        player_rect.y += gravity
        is_air = True

    if player_rect.bottom == block.rect.y + 10:
        jumping = False
        is_air = False

    if right:
        if player_rect.right < screen.get_width():
            player_rect.x += speed * dt

    if left:
        if player_rect.left > 0:
            player_rect.x -= speed * dt

    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN and not throw:
            circle = Circle(player_rect.centerx, player_rect.y, 10, screen)
            throw = True
            set_vector = line.get_vector()

        if event.type == KEYDOWN:
            if event.key == K_a:
                left = True
            if event.key == K_d:
                right = True
            if event.key == K_SPACE and not is_air:
                jumping = True

        if event.type == KEYUP:
            if event.key == K_a:
                left = False
            if event.key == K_d:
                right = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(framerate)
