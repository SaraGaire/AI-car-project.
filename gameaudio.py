import pygame
import time
import random
import json

class GameAudio:
    """Handles game sound effects and music."""
    def __init__(self, player_name):
        pygame.mixer.init()
        self.player_name = player_name
        self.sounds = {
            "engine": pygame.mixer.Sound("sounds/engine.wav"),
            "honk": pygame.mixer.Sound("sounds/honk.wav"),
            "crash": pygame.mixer.Sound("sounds/crash.wav"),
            "background": pygame.mixer.Sound(f"sounds/bg_{player_name}.wav")
        }
    
    def play_sound(self, sound_type):
        """Plays a specific sound effect."""
        if sound_type in self.sounds:
            self.sounds[sound_type].play()

    def play_background_music(self):
        self.sounds["background"].play(-1)  # Loop the background music

class TrafficLightVisual:
    """Handles animated traffic light visuals."""
    def __init__(self):
        self.states = ["RED", "GREEN", "YELLOW"]
        self.current_state = "RED"
    
    def change_light(self):
        while True:
            self.current_state = random.choice(self.states)
            print(f"Traffic Light Changed to: {self.current_state}")
            time.sleep(50)

class UserProgress:
    def __init__(self, filename="user_progress.json"):
        self.filename = filename
        self.data = self.load_progress()
    
    def load_progress(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def save_progress(self, player_name, points):
        """Saves player progress and achievements."""
        if player_name not in self.data:
            self.data[player_name] = {"points": 0, "achievements": []}
        
        self.data[player_name]["points"] += points
        
        if self.data[player_name]["points"] >= 100 and "Unlocked Custom Car Color" not in self.data[player_name]["achievements"]:
            self.data[player_name]["achievements"].append("Unlocked Custom Car Color")
            print(f"🏆 {player_name} has unlocked a custom car color!")
        
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)
    
    def get_feedback(self, player_name):
        if player_name in self.data:
            points = self.data[player_name]["points"]
            if points < 50:
                return "Keep improving your speed control and obeying traffic rules!"
            elif points < 100:
                return "Great job! You're on your way to unlocking special rewards!"
            else:
                return "You're a top racer! Enjoy your unlocked rewards!"
        return "Start playing to earn rewards!"

if __name__ == "__main__":
    player_name = "Player1"
    audio = GameAudio(player_name)
    traffic_light = TrafficLightVisual()
    user_progress = UserProgress()
    
    audio.play_background_music()
    user_progress.save_progress(player_name, 20)  # Example of saving progress
    print(user_progress.get_feedback(player_name))
