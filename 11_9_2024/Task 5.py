"""
Problem 5: Sports and Players
Create a function named list_sports() that returns the following list of sports: "Football", "Cricket", "Tennis", "Basketball".

Create a function named famous_player(sport) which receives a string argument representing a sport and returns the name of a famous player in that sport. For example, "Football" should return "Lionel Messi".

Call list_sports() and use famous_player() to print statements about each sport and a famous player, like "Lionel Messi is a famous Football player."
"""

def list_sports():
    return ["Football", "Cricket", "Tennis", "Basketball"]

def famous_player(sport):
    players = {
        "Football": "Lionel Messi",
        "Cricket": "Virat Kohli",
        "Tennis": "Roger Federer",
        "Basketball": "LeBron James"
    }
    return players.get(sport, "Unknown player")

sports = list_sports()
for sport in sports:
    print(f"{famous_player(sport)} is a famous {sport} player.")
