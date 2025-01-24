import customtkinter as ctk
from PIL import Image
import os
import subprocess

def launch_game():
    try:
        subprocess.Popen(['python', 'Documents/pycraft.py'])
        root.quit()
    except Exception as e:
        ctk.CTkMessagebox(title="Error", message=f"Could not launch PyCraft: {e}")

def show_settings():
    settings_window = ctk.CTkToplevel()
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    resolution_label = ctk.CTkLabel(settings_window, text="Resolution:")
    resolution_label.pack(pady=10)

    resolution_option = ctk.CTkOptionMenu(settings_window, values=["1920x1080", "1280x720", "800x600"])
    resolution_option.pack(pady=10)

    save_button = ctk.CTkButton(settings_window, text="Save", command=lambda: save_settings(resolution_option.get()))
    save_button.pack(pady=20)

def save_settings(resolution):
    print(f"Resolution set to: {resolution}")

# Main launcher window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("PyCraft Launcher")
root.geometry("800x500")
root.minsize(800,500)
root.maxsize(800,500)



title_label = ctk.CTkLabel(root, text="PyCraft Launcher", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=20)

game_image = ctk.CTkImage(Image.open("Documents/PyCraft/launcherimage.png"), size=(600,350))
bg_image = ctk.CTkLabel(root, image=game_image, text="")
bg_image.place(relx=0.125, rely=0.15)
play_button = ctk.CTkButton(root, text="Play", font=ctk.CTkFont(size=18), command=launch_game, fg_color="#24ab26", hover_color="#1b801c")
play_button.place(x=325, y=450)
settings_gear = ctk.CTkImage(Image.open("Documents/PyCraft/Textures/settingsgear.png"), size=(20,20))
settings_button = ctk.CTkButton(root, text="", image=settings_gear, font=ctk.CTkFont(size=18), width=20, height=25, command=show_settings, fg_color="#6b6b6b", hover_color="#4d4d4d")
settings_button.place(x=10, y=10)

version_dropdown = ctk.CTkOptionMenu(root, values=["PyCraft 3.3", "PyCraft 3.2", "PyCraft 3.1"])
version_dropdown.place(x=50, y=450)

quit_button = ctk.CTkButton(root, text="Quit", font=ctk.CTkFont(size=18), command=root.quit)
quit_button.place(x=600, y=450)

version_label = ctk.CTkLabel(root, text="Created by Mabindy", font=ctk.CTkFont(size=12))
version_label.place(x=340, y=480)

root.mainloop()
