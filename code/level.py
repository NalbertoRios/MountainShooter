#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import entity
from code.const import COLOR_WHITE, WIN_HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory



class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000 # 20 segundos


    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
       # while True:                ### CÓDIGO DA AULA ###
        #    clock.tick(60)
         #   for ent in self.entity_list:
          #      self.window.blit(source=ent.surf, dest=ent.rect)
           #     ent.move()
            ##or event in pygame.event.get():
              #  if event.type == pygame.QUIT:
               #     pygame.quit()
                #    sys.exit()  # provisório (aula)

        while True:             ### CÓDIGO SUGERIDO PELA (IA) DEVIDO A IMAGEM APRESENTAR LATÊNCIA###
            clock.tick(60)

            # 1️⃣ eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # volta para o menu (mais correto que sys.exit)

            # 2️⃣ lógica
            for ent in self.entity_list:
                ent.move()

            # 3️⃣ desenho (TODO FRAME)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()

            # printed text
    #        self.level_text(text_size 14, text f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
     #       COLOR-WHITE, tex_pos(10, 5))
      #      self.level_text(text_size 14, text f'fps: {clock.get_fps():.0f}', COLOR_WHITE,
     #       text_pos(10, WIN_HEIGHT - 35))
     #      self.level_text(text_size 14, text f'entidades: {len(self.entity_list)}', COLOR_WHITE,
      #      text_pos(10, WIN_HEIGHT - 20))
#            pygame.display.flip()
            pass

 #   def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple,):
 #       text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
 #       text_surf: Surface = text_font.render(text, antialias=True, text_color).convert_alpha()
 #       text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
 #       self.window.blit(source=text_surf, dest=text_rect)