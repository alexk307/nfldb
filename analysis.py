from database_handler import DatabaseHandler
from math import sqrt

# Points / item
POINTS = {
    'rec_yds_rec': .1,
    'rec_td': 6,
    'rec_rec': 1, # PPR
    'rush_yds': .1,
    'rush_td': 6,
    'pass_yds': (1/25.0),
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
                'variance': sqrt(variance)}
    else:
        return {'mean_points': 0,
                'variance': 0}


def create_analysis_file(year):
    data = DatabaseHandler()
    player_ids = data.get_all_player_ids()
    with open('nfl_player_variance_%s.csv' % year, 'a') as f:
        f.write('name,mean_points,variance\n')
        for i in player_ids:
            games = data.get_games_by_player(i, year=year)
            name = data.get_name_by_player_id(i)
            career_vector = \
                [calculate_fantasy_points(data.get_game(game)) for game in games]
            stats = generate_statistics(career_vector)
            f.write('%s,%s,%s\n' % (name, stats['mean_points'], stats['variance']))


if __name__ == '__main__':
    create_analysis_file(2014)
