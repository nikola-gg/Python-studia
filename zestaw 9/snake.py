import pygame
import random
import sys

"""
-- SNAKE --

Sterowanie: strzałki
Niebieski kwadrat = dobry owoc (+1 punkt)
Czerwony kwadrat = trujący owoc (-1 punkt, poniżej 0 = koniec gry)
Czarny kwadrat = bomba (natychmiastowy koniec gry)
Nie wolno zawracać.
Plansza ma periodyczne warunki brzegowe.
Z czasem rośnie prędkość (trochę szybciej).
Na ekranie może być kilka jedzeń naraz, każde znika po losowym czasie.
"""

pygame.init()

WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")

GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

snake_size = 20

font = pygame.font.SysFont("arial", 24)

moves = {
    "UP": (0, -5),
    "DOWN": (0, 5),
    "LEFT": (-5, 0),
    "RIGHT": (5, 0)
}
opposite = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT"
}

FRUIT_MIN_LIFETIME = 3.0
FRUIT_MAX_LIFETIME = 8.0
MAX_FOODS = 5
SPAWN_CHANCE = 0.02


def spawn_food(current_time):
    x = random.randint(0, WIDTH - snake_size)
    y = random.randint(0, HEIGHT - snake_size)

    r = random.random()
    if r < 0.7:
        t = "GOOD"
    elif r < 0.95:
        t = "BAD"
    else:
        t = "BOMB"

    lifetime = random.uniform(FRUIT_MIN_LIFETIME, FRUIT_MAX_LIFETIME)
    return [x, y, t, current_time, lifetime]


def main():
    clock = pygame.time.Clock()

    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2

    score = 0
    running = True
    game_over = False
    reason = ""

    direction = "RIGHT"

    start_ticks = pygame.time.get_ticks()
    time_limit = 120

    base_speed = 20
    max_speed = 60

    elapsed_at_start = 0.0
    foods = [spawn_food(elapsed_at_start)]

    while running:
        elapsed = (pygame.time.get_ticks() - start_ticks) / 1000

        speed = min(max_speed, base_speed + int(elapsed / 3))
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP:
                    new = "UP"
                elif event.key == pygame.K_DOWN:
                    new = "DOWN"
                elif event.key == pygame.K_LEFT:
                    new = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    new = "RIGHT"
                else:
                    new = direction

                if new == opposite[direction]:
                    game_over = True
                    reason = "Niedozwolony ruch!"
                else:
                    direction = new

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    return main()

        if not game_over:

            if elapsed > time_limit:
                game_over = True
                reason = f"Gratulacje, zdobyłeś {score} pkt."
            
            if not game_over:
                dx, dy = moves[direction]
                snake_x += dx
                snake_y += dy

                if snake_x < 0:
                    snake_x = WIDTH
                if snake_x > WIDTH:
                    snake_x = 0
                if snake_y < 0:
                    snake_y = HEIGHT
                if snake_y > HEIGHT:
                    snake_y = 0

                new_foods = []
                for fx, fy, typ, born_time, lifetime in foods:
                    if elapsed - born_time <= lifetime:
                        new_foods.append([fx, fy, typ, born_time, lifetime])
                foods = new_foods

                if len(foods) < MAX_FOODS and random.random() < SPAWN_CHANCE:
                    foods.append(spawn_food(elapsed))

                eaten_indices = []
                for i, (fx, fy, typ, born_time, lifetime) in enumerate(foods):
                    if abs(snake_x - fx) < snake_size and abs(snake_y - fy) < snake_size:
                        if typ == "GOOD":
                            score += 1
                        elif typ == "BAD":
                            score -= 1
                            if score < 0:
                                game_over = True
                                reason = "Wynik poniżej 0!"
                        elif typ == "BOMB":
                            game_over = True
                            reason = "Zjadłeś bombę!"

                        eaten_indices.append(i)
                        if game_over:
                            break

                for i in reversed(eaten_indices):
                    foods.pop(i)

        WIN.fill((30, 30, 30))

        pygame.draw.rect(WIN, GREEN, (snake_x, snake_y, snake_size, snake_size))

        for fx, fy, typ, born_time, lifetime in foods:
            color = BLUE if typ == "GOOD" else RED if typ == "BAD" else BLACK
            pygame.draw.rect(WIN, color, (fx, fy, snake_size, snake_size))

        WIN.blit(font.render(f"Wynik: {score}", True, WHITE), (10, 10))
        WIN.blit(font.render(f"Czas: {int(max(0, time_limit - elapsed))}s", True, WHITE), (10, 40))

        if game_over:
            t1 = font.render("Koniec gry!", True, WHITE)
            t2 = font.render(reason, True, WHITE)
            t3 = font.render("Naciśnij SPACJĘ, aby zagrać ponownie", True, WHITE)
            WIN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
            WIN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 190))
            WIN.blit(t3, (WIDTH // 2 - t3.get_width() // 2, 230))

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
