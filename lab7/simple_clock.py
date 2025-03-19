import pygame 
import tkinter as tk
from tkinter import filedialog
import os
class musicplayer:
    def __init__(self,root):
        self.root=root
        self.root.title("Pygame Music Player")
        self.root.geometry("300x200")

        pygame.mixer.init()


