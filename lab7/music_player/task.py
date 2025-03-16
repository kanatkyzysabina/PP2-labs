import pygame
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((800, 600))
running = True
FPS = 60
clock = pygame.time.Clock()
screen_bg = pygame.image.load('lab7/music_player/screen_bg.JPG').convert()

# text- - - - 
text_font = pygame.font.Font('lab7/music_player/Pixeltype1.ttf', 50)

title_surf = text_font.render('Music Player!', False, (64,64,64))
title_surf_rect = title_surf.get_rect(center = (300, 200))

message_surf = text_font.render('Click SPACE to play/stop', False, "Black")
message_surf_rect = message_surf.get_rect(center = (400, 350))


# player- - - 
music_player = pygame.image.load('lab7/music_player/music_player.png').convert_alpha()
music_player_rect = music_player.get_rect(center = (400, 200))

# music- - - 
is_playing = True
playlist = ['lab7/music_player/song1.mp3', 'lab7/music_player/song2.mp3',
                 'lab7/music_player/song3.mp3', 'lab7/music_player/song4.mp3']
current_song = 0
pygame.mixer.music.load(playlist[current_song])
pygame.mixer.music.play()
pygame.mixer.music.pause()


# text2 - displaying what music plays currently :)
song1_text = text_font.render('Mitski - Jobeless Monday', False, "Black")
song1_text_rect = message_surf.get_rect(center = (400,60))

song2_text = text_font.render('White Town - Your Woman', False, "Black")
song2_text_rect = message_surf.get_rect(center = (400,60))

song3_text = text_font.render('beabadobee - The Perfect Pair', False, "Black")
song3_text_rect = message_surf.get_rect(center = (370,60))

song4_text = text_font.render('Steven Universe - Escapism', False, "Black")
song4_text_rect = message_surf.get_rect(center = (370,60))

#rotating player decal
def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

angle = 0
player_decal = pygame.image.load('lab7/music_player/play.png').convert_alpha()
x = 400
y = 470

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if pressed_keys[pygame.K_SPACE]:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
                if playlist[current_song]== playlist[0]:
                    screen.blit(song1_text, song1_text_rect)
            if pressed_keys[pygame.K_LEFT]:
                current_song = (current_song + 1)%len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                is_playing = True
            if pressed_keys[pygame.K_RIGHT]:
                current_song = (current_song - 1)%len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                is_playing = True

        
    screen.fill('White')
    screen.blit(screen_bg, (0,0))
    screen.blit(music_player, music_player_rect)
    screen.blit(title_surf, title_surf_rect)
    pygame.draw.rect(screen, (247, 195, 223), message_surf_rect)
    screen.blit(message_surf, message_surf_rect)

    rotated_decal, rotated_decal_rect = rot_center(player_decal, angle, x, y)
    screen.blit(rotated_decal, rotated_decal_rect)
    angle+=1
    if playlist[current_song] == playlist[0]:
        screen.blit(song1_text, song1_text_rect)
    elif playlist[current_song] == playlist[1]:
        screen.blit(song2_text, song2_text_rect)
    elif playlist[current_song] == playlist[2]:
        screen.blit(song3_text, song3_text_rect)
    elif playlist[current_song] == playlist[3]:
        screen.blit(song4_text, song4_text_rect)

    


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()