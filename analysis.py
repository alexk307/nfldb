from database_handler import DatabaseHandler
from math import sqrt

# Points / item
POINTS = {
    'rec_yds_rec': .1,
    'rec_td': 6,
    'rec_rec': 1, # PPR
    'rush_yds': .1,
    'rush_td': 6,
    'pass_yds': (1/25),
    'pass_tds': 4,
    'pass_int': -2,
}


def calculate_fantasy_points(game):
    fantasy_points = 0
    for category in POINTS:
        stat = game.get(category, 0)
        if not stat:
            stat = 0
        fantasy_points += POINTS[category] * int(stat)
    return fantasy_points


def generate_statistics(vector):
    if vector:
        mean_points = sum(vector) / float(len(vector))

        variance_sum = 0
        for game_points in vector:
            variance_sum += (game_points - mean_points) ** 2

        variance = (variance_sum / float(len(vector)))
        return {'mean_points': mean_points,
                'variance': variance}
    else:
        return {'mean_points': 0,
                'variance': 0}

if __name__ == '__main__':
    data = DatabaseHandler()
    for i in xrange(1, 10):
        games = data.get_games_by_player(i)
        print data.get_name_by_player_id(i)
        career_vector = \
            [calculate_fantasy_points(data.get_game(game)) for game in games]
        print generate_statistics(career_vector)
