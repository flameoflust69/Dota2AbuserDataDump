import json, urllib.request
import sqlite3
import os

# 163392533 -> BrokeBack

# 86874930 -> désolé

# 21853297 -> Keith

# 48964589 -> WORMY

# 201972588 -> 无心

# 113457541 -> SACRAMENT OF WILDERNESS

# 162747012 -> MAGICAL~

# 224051329 -> SUFF

# 101312582 -> CHEWWWWWWWWWW

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TargetSteamId = 101312582
TotalMatches = 200

def main():
    url = "https://api.stratz.com/api/v1/Player/" + str(TargetSteamId) + "/matches?lobbyType=7&isParty=false&take=" + str(TotalMatches)
    
    with urllib.request.urlopen(url) as dataQuery:
        data = json.loads(dataQuery.read())
    
    for loopValue in data['results']:
        for PlayersData in loopValue['players']:
            if PlayersData['steamId'] == TargetSteamId:
                if PlayersData['isRadiant'] == True:
                    LocalPlayer = 1
                else:
                    LocalPlayer = 2

        db_path = ROOT_DIR + "\\Output\\Output.sqlite3"

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            rows = [
                        int(loopValue['id']),
                        LocalPlayer,
                        loopValue['players'][0]['steamId'],
                        loopValue['players'][1]['steamId'],
                        loopValue['players'][2]['steamId'],
                        loopValue['players'][3]['steamId'],
                        loopValue['players'][4]['steamId'],
                        loopValue['players'][5]['steamId'],
                        loopValue['players'][6]['steamId'],
                        loopValue['players'][7]['steamId'],
                        loopValue['players'][8]['steamId'],
                        loopValue['players'][9]['steamId']
                    ]
            cursor.execute('insert into "' + str(TargetSteamId) + '" values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', rows)
            conn.commit()
        finally:
            conn.close()

    print(db_path)

if __name__ == "__main__":
    main()