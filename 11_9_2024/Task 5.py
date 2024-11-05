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
