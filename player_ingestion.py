from fantasy_football import get_active_players, parse_game_log
from database_handler import DatabaseHandler
from string import ascii_uppercase


def consume(first_letter):
    player_db = DatabaseHandler()
    players = get_active_players(first_letter)
    for player in players:
        first_name = player.get('name', '').split(' ')[0]
        last_name = player.get('name', '').split(' ')[1]
        position = player.get('position')
        url = player.get('link')
        player_id = player_db.write_player(first_name, last_name, position, url)
        game_dict = parse_game_log(url)
        for game in game_dict:
            player_db.write_game(player_id, game)
        print 'Done with %s %s' % (first_name, last_name)
        from time import sleep
        sleep(1)


def get_all_active_players():
    for first_letter in ascii_uppercase:
        consume(first_letter)
        print 'done %s' % first_letter


def scrape():
    for letter in ascii_uppercase:
        consume(letter)
