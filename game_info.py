# blue - 0, (false), red - 1 (true)

class GameInfo:
    def __init__(self, id, start_time, duration, winner, participants):
        self.id = id
        self.start_time = start_time
        self.duration = duration
        self.winner = winner
        self.participants = participants


class PlayerInfo:
    def __init__(self, id, name, kills, deaths, assists, champion_name, champion_id, gold, damage, creep_score, vision_score, team, multikills, position):
        self.id = id
        self.name = name
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.champion_name = champion_name
        self.champion_id = champion_id
        self.gold = gold
        self.damage = damage
        self.creep_score = creep_score
        self.vision_score = vision_score
        self.team = team
        self.multikills = multikills
        self.position = position