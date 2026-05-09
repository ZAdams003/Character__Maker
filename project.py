import pygame

pygame.init()

# Window:

WIDTH, HEIGHT = 1200, 1200
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Character Maker")
clock = pygame.time.Clock()

# Positions of assets

BODY_POS = (200, 250)
SKINTONE_POS = BODY_POS
SHIRT_POS = BODY_POS
HAIR_POS = BODY_POS
EYE_POS = BODY_POS
NOSE_POS = BODY_POS
EYEBROW_POS = BODY_POS

