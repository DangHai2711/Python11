import pygame

# Tạo màn hình game
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Tải hình ảnh khủng long
dinosaur_image = pygame.image.load("dragon.jpg")

# Khởi tạo vị trí khủng long
dinosaur_x = 200
dinosaur_y = 300

# Tạo chướng ngại vật
obstacle_image = pygame.image.load("naruto.jpg ")
obstacle_x = 800
obstacle_y = 300

# Tạo biến để kiểm tra trạng thái nhảy
is_jumping = False

# Tạo vòng lặp game
while True:

    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jumping = True

    # Cập nhật trạng thái khủng long
    if is_jumping:
        dinosaur_y -= 5
        if dinosaur_y <= 0:
            is_jumping = False

    # Vẽ màn hình
    screen.fill((0, 0, 0))
    screen.blit(dinosaur_image, (dinosaur_x, dinosaur_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Di chuyển chướng ngại vật
    obstacle_x -= 5

    # Kiểm tra va chạm
    if dinosaur_x + dinosaur_image.get_width() >= obstacle_x and dinosaur_x <= obstacle_x + obstacle_image.get_width() and dinosaur_y + dinosaur_image.get_height() >= obstacle_y and dinosaur_y <= obstacle_y + obstacle_image.get_height():
        print("Game over!")
        exit()

    # Cập nhật màn hình
    pygame.display.update()