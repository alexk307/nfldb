import requests
import re
from bs4 import BeautifulSoup
import copy

INTERESTED_POSITIONS = ['QB', 'RB', 'TE', 'WR']

COLS = ['week', 'year', 'game_num', 'date', 'age', 'team', 'away', 'opp',
        'result', 'rec_tgt', 'rec_rec', 'rec_yds_rec', 'rec_ypr', 'rec_td',
        'rush_att', 'rush_yds', 'rush_ypa', 'rush_td', 'pass_cmp', 'pass_att',
        'pass_cmp_pct', 'pass_yds', 'pass_td', 'pass_int', 'pass_rate',
        'pass_ypa', 'pass_adjusted_ypa', 'kick_ret', 'kick_ret_yds',
        'kick_ret_ypa', 'kick_ret_td', 'punt_ret', 'punt_ret_yds',
        'punt_ret_ypa', 'punt_ret_td', 'two_pt_con', 'pts', 'sack', 'tackle',
        'ast_tackle']

DEFAULT_COLS = ['week', 'year', 'game_num', 'date', 'age', 'team', 'away',
                'opp', 'result']
PASSING_COLS = ['pass_cmp', 'pass_att', 'pass_cmp_pct', 'pass_yds', 'pass_td',
                'pass_int', 'pass_rate', 'pass_ypa', 'pass_adjusted_ypa']
RUSHING_COLS = ['rush_att', 'rush_yds', 'rush_ypa', 'rush_td']
REC_COLS = ['rec_tgt', 'rec_rec', 'rec_yds_rec', 'rec_ypr', 'rec_td']
TACKLE_COLS = ['sack', 'tackle', 'ast_tackle']
KICK_COLS = ['kick_ret', 'kick_ret_yds', 'kick_ret_ypa', 'kick_ret_td']
PUNT_COLS = ['punt_ret', 'punt_ret_yds', 'punt_ret_ypa', 'punt_ret_td']
PUNTING_COLS = ['punts', 'yards', 'yards_per_punt', 'blocked']
SCORING_COLS = ['two_pt_con', 'pts']


def get_active_players(first_letter):
    res = requests.get(
        'http://www.pro-football-reference.com/players/%s/' % first_letter)
    soup = BeautifulSoup(res.text)
    players = soup.findAll('b')
    player_list = []
    for player in players:
        s = BeautifulSoup(str(player))
        matched_position = False
        for position in INTERESTED_POSITIONS:
            if position in str(s):
                matched_position = position
        if not matched_position:
            continue

        res = s.findAll('a')
        if res:
            player_list.append(
                {'name': _strip_html(str(res[0])),
                 'link': process_gamelog_url(res[0].get('href'), first_letter),
                 'position': matched_position}
            )
    return player_list


def process_gamelog_url(uri, first_letter):
    base_url = 'http://www.pro-football-reference.com'
    player_specific = uri.split('.htm')[0] + '/gamelog'
    return base_url + player_specific


def _get_overlay_columns(rows):
    return map(
        lambda x: _strip_html(str(x)),
        filter(
            lambda x: 'over_header' in str(x), rows)
    )

def _get_active_columns(columns, sub_columns):

    sub_columns = filter(lambda x: x != '' and x not in columns, sub_columns)
    active_columns = copy.copy(DEFAULT_COLS)
    for col in columns:
        if col == 'GS':
            active_columns.append('games_started')
        if col == 'Rushing':
            active_columns.extend(RUSHING_COLS)
        if col == 'Receiving':
            active_columns.extend(REC_COLS)
        if col == 'Passing':
            active_columns.extend(PASSING_COLS)
        if col == 'Kick Returns':
            active_columns.extend(KICK_COLS)
        if col == 'Punt Returns':
            active_columns.extend(PUNT_COLS)
        if col == 'Scoring':
            active_columns.extend(SCORING_COLS)
        if col == 'Sacks &amp; Tackles':
            active_columns.extend(TACKLE_COLS)
        if col == 'Punting':
            active_columns.extend(PUNTING_COLS)

    if 'Pts' in sub_columns and 'Scoring' not in columns:
        spot = sub_columns.index('Pts')
        active_columns.insert(spot + 1, 'pts')

    if '2PM' in sub_columns and 'Scoring' not in columns:
        spot = sub_columns.index('2PM')
        active_columns.insert(spot + 1, 'two_pt_con')

    if 'GS' in sub_columns:
        spot = sub_columns.index('GS')
        active_columns.insert(spot + 1, 'games_started')

    return active_columns


def _strip_html(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def parse_game_log(gamelog_url):
    res = requests.get(gamelog_url)
    soup = BeautifulSoup(res.text)
    parsed = soup.findAll('div',
                          {'class': 'table_container', 'id': 'div_stats'})
    if not parsed:
        # No data, this is a rookie
        return []

    sub_headers = map(
        lambda x: _strip_html(str(x)),
        parsed[0].findAll('thead')[0].findAll('th')
    )
    headers = _get_overlay_columns(parsed[0].findAll('thead')[0].findAll('th'))

    parsed_log = \
        _parse_table_response(parsed[0].findAll('td'),
                              _get_active_columns(headers, sub_headers))

    # Don't return the last row as that has summary information
    return parsed_log[0:len(parsed_log) - 1]


def _parse_table_response(data, row_names):
    t = []
    count = 0
    for i in range(int(len(data)) / len(row_names)):
        row = {}
        for j in range(len(row_names)):
            row[row_names[j]] = _strip_html(str(data[count]))
            count += 1
        t.append(row)
    return t
