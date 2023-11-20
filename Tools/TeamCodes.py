def get_team_codes():
    return [
        'ARI',
        'ATL',
        'RAV',
        'BUF',
        'CAR',
        'CHI',
        'CIN',
        'CLE',
        'DAL',
        'DEN',
        'DET',
        'GNB',
        'HTX',
        'CLT',
        'JAX',
        'KAN',
        'RAI',
        'SDG',
        'RAM',
        'MIA',
        'MIN',
        'NWE',
        'NOR',
        'NYG',
        'NYJ',
        'PHI',
        'PIT',
        'SFO',
        'SEA',
        'TAM',
        'OTI',
        'WAS'
    ]


def translate_team_id_to_code(team_id):
    return {
        1:'ARI',
        1:'CRD',
        2:'ATL',
        3:'BAL',
        3:'RAV',
        4:'BUF',
        5:'CAR',
        6:'CHI',
        7:'CIN',
        8:'CLE',
        9:'DAL',
        10:'DEN',
        11:'DET',
        12:'GNB',
        13:'HOU',
        13:'HTX',
        14:'IND',
        14:'CLT',
        15:'JAX',
        16:'KAN',
        17:'LVR',
        17:'RAI',
        18:'LAC',
        18:'SDG',
        19:'LAR',
        19:'RAM',
        20:'MIA',
        21:'MIN',
        22:'NWE',
        23:'NOR',
        24:'NYG',
        25:'NYJ',
        26:'PHI',
        27:'PIT',
        28:'SFO',
        29:'SEA',
        30:'TAM',
        31:'TEN',
        31:'OTI',
        32:'WAS'
    }[team_id]


def translate_team_code_to_id(team):
    return {
        'ARI':1,
        'CRD':1,
        'ATL':2,
        'BAL':3,
        'RAV':3,
        'BUF':4,
        'CAR':5,
        'CHI':6,
        'CIN':7,
        'CLE':8,
        'DAL':9,
        'DEN':10,
        'DET':11,
        'GNB':12,
        'HOU':13,
        'HTX':13,
        'IND':14,
        'CLT':14,
        'JAX':15,
        'KAN':16,
        'LVR':17,
        'RAI':17,
        'LAC':18,
        'SDG':18,
        'LAR':19,
        'RAM':19,
        'MIA':20,
        'MIN':21,
        'NWE':22,
        'NOR':23,
        'NYG':24,
        'NYJ':25,
        'PHI':26,
        'PIT':27,
        'SFO':28,
        'SEA':29,
        'TAM':30,
        'TEN':31,
        'OTI':31,
        'WAS':32,
        '':'',
        '2TM':''
    }[team]

def translate_team_name_to_id(team):
    return {
        'ARI':1,
        'Arizona Cardinals':1,
        'CRD':1,
        'ATL':2,
        'Atlanta Falcons':2,
        'BAL':3,
        'RAV':3,
        'Baltimore Ravens':3,
        'BUF':4,
        'Buffalo Bills':4,
        'CAR':5,
        'Carolina Panthers':5,
        'CHI':6,
        'Chicago Bears':6,
        'CIN':7,
        'Cincinnati Bengals':7,
        'CLE':8,
        'Cleveland Browns':8,
        'DAL':9,
        'Dallas Cowboys':9,
        'DEN':10,
        'Denver Broncos':10,
        'DET':11,
        'Detroit Lions':11,
        'GB':12,
        'Green Bay Packers':12,
        'GNB':12,
        'HOU':13,
        'HTX':13,
        'Houston Texans':13,
        'IND':14,
        'Indianapolis Colts':14,
        'CLT':14,
        'JAC':15,
        'JAX':15,
        'Jacksonville Jaguars':15,
        'KAN':16,
        'KC':16,
        'Kansas City Chiefs':16,
        'LV':17,
        'LVR':17,
        'RAI':17,
        'Las Vegas Raiders':17,
        'LAC':18,
        'Los Angeles Chargers':18,
        'SDG':18,
        'LAR':19,
        'Los Angeles Rams':19,
        'RAM':19,
        'MIA':20,
        'Miami Dolphins':20,
        'MIN':21,
        'Minnesota Vikings':21,
        'NWE':22,
        'New England Patriots':22,
        'NE':22,
        'NOR':23,
        'New Orleans Saints':23,
        'NO':23,
        'NYG':24,
        'New York Giants':24,
        'NYJ':25,
        'New York Jets':25,
        'PHI':26,
        'Philadelphia Eagles':26,
        'PIT':27,
        'Pittsburgh Steelers':27,
        'SF':28,
        'San Francisco 49ers':28,
        'SFO':28,
        'SEA':29,
        'Seattle Seahawks':29,
        'TB':30,
        'Tampa Bay Buccaneers':30,
        'TAM':30,
        'TEN':31,
        'Tennessee Titans':31,
        'OTI':31,
        'WAS':32,
        'Washington Football Team':32,
        'Washington Commanders':32,
        '':'',
        '2TM':''
    }[team]