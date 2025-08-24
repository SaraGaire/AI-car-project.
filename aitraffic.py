import random
import time

class AITraffic:
    """Simulates AI-controlled traffic that adapts to player behavior."""
    def __init__(self):
        self.traffic_speed = random.randint(30, 60)

    def update_traffic_speed(self, player_speeds):
        """Adjusts AI traffic speed based on average player speed."""
        avg_speed = sum(player_speeds) / len(player_speeds)
        self.traffic_speed = max(30, min(70, avg_speed + random.randint(-10, 10)))

class PlayerBehavior:
    """Analyzes player behavior and provides insights."""
    def __init__(self):
        self.speed_records = {}

    def record_speed(self, player_name, speed):
        """Records player speeds for analysis."""
        if player_name not in self.speed_records:
            self.speed_records[player_name] = []
        self.speed_records[player_name].append(speed)

    def analyze_behavior(self, player_name):
        """Analyzes the player's speeding patterns."""
        if player_name in self.speed_records:
            avg_speed = sum(self.speed_records[player_name]) / len(self.speed_records[player_name])
            print(f"{player_name} Average Speed: {avg_speed}")
            if avg_speed > 55:
                print(f"Warning: {player_name} frequently overspeeds!")

class AutonomousOpponent:
    """An AI opponent that adjusts its strategy based on player performance."""
    def __init__(self, name):
        self.name = name
        self.speed = random.randint(30, 60)

    def adjust_speed(self, player_speeds):
        avg_speed = sum(player_speeds) / len(player_speeds)
        if avg_speed > self.speed:
            self.speed += random.randint(5, 15)
        else:
            self.speed -= random.randint(5, 10)

class SpeedPredictor:
    """Predicts player overspeeding tendencies."""
    def __init__(self):
        self.history = {}

    def record_speed(self, player_name, speed):
        """Stores speed data for prediction."""
        if player_name not in self.history:
            self.history[player_name] = []
        self.history[player_name].append(speed)

    def predict_overspeeding(self, player_name):
        """Predicts if a player is likely to overspeed."""
        if player_name in self.history and len(self.history[player_name]) > 5:
            recent_speeds = self.history[player_name][-5:]
            avg_recent_speed = sum(recent_speeds) / len(recent_speeds)
            if avg_recent_speed > 55:
                print(f"Prediction: {player_name} is likely to overspeed soon!")

if __name__ == "__main__":
    ai_traffic = AITraffic()
    player_behavior = PlayerBehavior()
    ai_opponent = AutonomousOpponent("AI Racer")
    speed_predictor = SpeedPredictor()

    players = ["Player1", "Player2", "Player3"]
    for _ in range(10):  # Simulate 10 rounds
        player_speeds = [random.randint(30, 70) for _ in players]
        for i, player in enumerate(players):
            player_behavior.record_speed(player, player_speeds[i])
            speed_predictor.record_speed(player, player_speeds[i])
        
        ai_traffic.update_traffic_speed(player_speeds)
        ai_opponent.adjust_speed(player_speeds)
        for player in players:
            player_behavior.analyze_behavior(player)
            speed_predictor.predict_overspeeding(player)
        
        time.sleep(1)
