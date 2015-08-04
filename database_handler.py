import MySQLdb
from re import escape


COLS = ['week', 'year', 'game_num', 'date', 'age', 'team', 'away', 'opp',
        'result', 'rec_tgt', 'rec_rec', 'rec_yds_rec', 'rec_ypr', 'rec_td',
        'rush_att', 'rush_yds', 'rush_ypa', 'rush_td', 'pass_cmp', 'pass_att',
        'pass_cmp_pct', 'pass_yds', 'pass_td', 'pass_int', 'pass_rate',
        'pass_ypa', 'pass_adjusted_ypa', 'kick_ret', 'kick_ret_yds',
        'kick_ret_ypa', 'kick_ret_td', 'punt_ret', 'punt_ret_yds',
        'punt_ret_ypa', 'punt_ret_td', 'two_pt_con', 'pts', 'sack', 'tackle',
        'ast_tackle', 'games_started']


class DatabaseHandler():
    def __init__(self):
        kwargs = {
            'host': 'localhost',
            'user': 'root',
            'db': 'nfl',
            'port': 3306,
            'charset': 'utf8'
        }

        self._db = MySQLdb.connect(**kwargs)

    def _execute_query(self, query):
        cursor = self._db.cursor()
        cursor.execute(query)
        self._db.commit()
        return cursor.lastrowid

    def write_game(self, player_id, game_dict):
        for item in game_dict.keys():
            if item not in COLS:
                game_dict.pop(item, None)

        query = """INSERT INTO games (player_id, %s) VALUES ('%s', '%s')""" % \
                (','.join(game_dict.keys()), player_id,
                 "','".join(game_dict.values()))
        return self._execute_query(query)

    def write_player(self, first_name, last_name, position, url):
        query = """INSERT INTO players (first_name, last_name, position, url)
                VALUES ('%s', '%s', '%s', '%s')""" % \
                (escape(first_name),
                 escape(last_name),
                 escape(position),
                 escape(url))
        return self._execute_query(query)

    def get_game(self, game_id):
        query = """SELECT * FROM games WHERE id = '%s'""" % game_id
        cur = self._db.cursor()
        cur.execute(query)
        results = cur.fetchone()
        return dict(zip(map(lambda x: x[0], cur.description), results))

    def get_games_by_player(self, player_id):
        query = """SELECT games.id FROM games JOIN players p ON p.id = games.player_id WHERE p.id = %s""" % player_id
        cur = self._db.cursor()
        cur.execute(query)
        return map(lambda x: int(x[0]), cur.fetchall())

    def get_name_by_player_id(self, player_id):
        query = """SELECT first_name, last_name FROM players WHERE id = %s""" % player_id
        cur = self._db.cursor()
        cur.execute(query)
        name = cur.fetchone()
        return "%s %s" % (name[0], name[1])