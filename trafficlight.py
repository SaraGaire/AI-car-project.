import time
import threading
import random

class TrafficLight:
    """Controls the traffic lights in the game."""
    def __init__(self):
        self.state = "RED"
        self.running = True

    def change_light(self):
        """Changes the traffic light state at regular intervals."""
        while self.running:
            if self.state == "RED":
                time.sleep(50) 
                self.state = "GREEN"
            elif self.state == "GREEN":
                time.sleep(60)  
                self.state = "YELLOW"
            elif self.state == "YELLOW":
                time.sleep(30) 
                self.state = "RED"

    def start(self):
        """Starts the traffic light system in a separate thread."""
        thread = threading.Thread(target=self.change_light, daemon=True)
        thread.start()

    def get_state(self):
        return self.state

class Player:
    def __init__(self, name, speed_limit=50):
        self.name = name
        self.speed = 0
        self.speed_limit = speed_limit
        self.points = 0
        self.active = True

    def update_speed(self, new_speed):
        self.speed = new_speed
        if self.speed > self.speed_limit:
            print(f"{self.name} received a ticket for overspeeding! Speed: {self.speed}")
            self.points -= 10 
        else:
            self.points += 5  

    def block_other(self, other_player):
        """Blocks another player by reducing their speed."""
        if other_player.active:
            other_player.speed = max(0, other_player.speed - 10)
            print(f"{self.name} blocked {other_player.name}, reducing their speed!")

    def eliminate(self, other_player):
        """Removes another player from the game."""
        if other_player.active:
            other_player.active = False
            print(f"{self.name} eliminated {other_player.name} from the race!")

# Game Setup
def start_game():
    """Sets up the game environment and runs the race."""
    traffic_light = TrafficLight()
    traffic_light.start()
    
    players = [Player("Player1"), Player("Player2"), Player("Player3")]
    
    for _ in range(10):  # Simulating 10 rounds of racing
        print("Traffic Light State:", traffic_light.get_state())
        for player in players:
            if player.active:
                speed = random.randint(30, 70)  # Randomly assign a speed to the player
                player.update_speed(speed)
                print(f"{player.name} speed: {player.speed}, Points: {player.points}")
                
                if random.random() < 0.2:  # 20% chance to block another player
                    target = random.choice([p for p in players if p != player and p.active])
                    player.block_other(target)
                    
                if random.random() < 0.1:  # 10% chance to eliminate another player
                    target = random.choice([p for p in players if p != player and p.active])
                    player.eliminate(target)
        time.sleep(1)
    
'''sorting the player based on there hightest speed in game and placing the winner.'''

    ranked_players = sorted( players, key=lambda p: p.points, reverse=True)
    
    print("\n🏆 Final Results 🏆")
    for i, player in enumerate(ranked_players[:3]):  # Display top 3 players
        position = ["🥇 Winner", "🥈 Second", "🥉 Third"][i]
        print(f"{position}: {player.name} with {player.points} points")

    if __name__ == "__main__":
           start_game()
