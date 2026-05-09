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

# Loading the images

def load_imgs():
    # White Base character img
    character = pygame.image.load("images/base01.png").convert_alpha()
    character = pygame.transform.scale(character, (800, 800))

    #Skintone options
    skintones = {
        "base2": pygame.transform.scale(
            pygame.image.load("images/base02.png").convert_alpha(),
            (800, 800)
        ),
        "base3": pygame.transform.scale(
            pygame.image.load("images/base03.png").convert_alpha(),
            (800, 800)
        ),
        "base4": pygame.transform.scale(
            pygame.image.load("images/base04.png").convert_alpha(),
            (800, 800)
        )
    }

    #Shirt options
    shirts = {
        "blue": pygame.transform.scale(
            pygame.image.load("images/shirt_b.png").convert_alpha(),
            (800, 800)
        ),
        "red": pygame.transform.scale(
            pygame.image.load("images/shirt_r.png").convert_alpha(),
            (800, 800)
        ),
        "pink": pygame.transform.scale(
            pygame.image.load("images/shirt_p.png").convert_alpha(),
            (800, 800)
        ),
    }

    #Hair options
    hairs = {
        "blond1": pygame.transform.scale(
            pygame.image.load("images/hair01_b.png").convert_alpha(),
            (800, 800)
        ),
        "brown1": pygame.transform.scale(
            pygame.image.load("images/hair01_br.png").convert_alpha(),
            (800, 800)
        ),
        "ginger1": pygame.transform.scale(
            pygame.image.load("images/hair01_g.png").convert_alpha(),
            (800, 800)
        ),
        "blond2": pygame.transform.scale(
            pygame.image.load("images/hair02_b.png").convert_alpha(),
            (800, 800)
        ),
        "brown2": pygame.transform.scale(
            pygame.image.load("images/hair02_br.png").convert_alpha(),
            (800, 800)
        ),
        "ginger2": pygame.transform.scale(
            pygame.image.load("images/hair02_g.png").convert_alpha(),
            (800, 800)
        )
    }

    #Eye options
    eyes = {
        "blueeyes1": pygame.transform.scale(
            pygame.image.load("images/eyes01_b.png").convert_alpha(),
            (800, 800)
        ),
        "browneyes1": pygame.transform.scale(
            pygame.image.load("images/eyes01_br.png").convert_alpha(),
            (800, 800)
        ),
        "greeneyes1": pygame.transform.scale(
            pygame.image.load("images/eyes01_g.png").convert_alpha(),
            (800, 800)
        ),
        "blueeyes2": pygame.transform.scale(
            pygame.image.load("images/eyes02_b.png").convert_alpha(),
            (800, 800)
        ),
        "browneyes2": pygame.transform.scale(
            pygame.image.load("images/eyes02_br.png").convert_alpha(),
            (800, 800)
        ),
        "greeneyes2": pygame.transform.scale(
            pygame.image.load("images/eyes02_g.png").convert_alpha(),
            (800, 800)
        )
    }

    #Nose options
    noses = {
        "nose1": pygame.transform.scale(
            pygame.image.load("images/nose01.png").convert_alpha(),
            (800, 800)
        ),
        "nose2": pygame.transform.scale(
            pygame.image.load("images/nose02.png").convert_alpha(),
            (800, 800)
        ),
        "nose3": pygame.transform.scale(
            pygame.image.load("images/nose03.png").convert_alpha(),
            (800, 800)
        )
    }

    #Eyebrow options
    eyebrows = {
        "blondbrow1": pygame.transform.scale(
            pygame.image.load("images/eyebrows01_b.png").convert_alpha(),
            (800, 800)
        ),
        "brownbrow1": pygame.transform.scale(
            pygame.image.load("images/eyebrows01_br.png").convert_alpha(),
            (800, 800)
        ),
        "gingerbrows1": pygame.transform.scale(
            pygame.image.load("images/eyebrows01_g.png").convert_alpha(),
            (800, 800)
        )
    }
    return character, skintones, shirts, hairs, eyes, noses, eyebrows

def background_img():
    background = pygame.image.load("images/Bkgrnd.png").convert_alpha()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    return background

def load_save_button():
    save_button = pygame.transform.scale(
        pygame.image.load("images/savebutton.png").convert_alpha(),
        (250, 250)
    )
    return save_button
character, skintones, shirts, hairs, eyes, noses, eyebrows = load_imgs()
background = background_img()
save_button = load_save_button()

# Button class
class Button:
    def __init__(self, x, y, image, item_name, item_type):
        self.image = image
        self.rect = image.get_rect(topleft=(x, y))
        self.item_name = item_name
        self.item_type = item_type

    def draw(self):
        window.blit(self.image, self.rect)

# Buttons for selections
def button_options():
    buttons = []

    #Skintones
    x = 70
    for name, image in skintones.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "skintone"))
        x += 50
    #Shirts
    x = 70
    for name, image in shirts.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "shirt"))
        x += 50
    #Hairs
    x = 70
    for name, image in hairs.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "hair"))
        x += 50
    #Eyes
    x = 70
    for name, image in eyes.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "eye"))
        x += 50
    #Noses
    x = 70
    for name, image in noses.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "nose"))
        x += 50
    #Eyebrows
    x = 70
    for name, image in eyebrows.items():
        thumbnail = pygame.transform.scale(image, (80, 80))
        buttons.append(Button(x, 150, thumbnail, name, "eyebrow"))
        x += 50

    #Save button
    save_button_rect = Button(940, 900, save_button, "save", "save")
    return buttons, save_button_rect

buttons, save_button_rect = button_options()

