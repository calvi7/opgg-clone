from riotwatcher import LolWatcher, ApiError


class DataFinder:
    def __init__(self, region, userName):
        self.watcher = LolWatcher(api_key='<your-api-key>')
        self.userName = userName
        self.region = region
    
    def player_data(self):
        regions: dict = {
            'la1': 'americas',
            'la2': 'americas',
            'na1': 'americas',
        }
        try:
            player = self.watcher.summoner.by_name(self.region, self.userName)
        except ApiError as e:
            if e.response.status_code == 404:
                return False
            else:
                return False
        else:
            player_puuid = player['puuid']
            matchData = self.watcher.match.matchlist_by_puuid('americas', puuid=player_puuid, count=10)
            temp_data = []
            for gameID in matchData:
                info = (self.watcher.match.by_id(regions[self.region], gameID))
                coolData = info['info']['participants']
                info = list(filter(lambda x: x['summonerName']==self.userName, coolData))
                if not info:
                    return False
                else:
                    temp_data.append(info[0])
            return temp_data

    def data_dragon(self):
        regions: dict = {
            'la1': 'lan',
            'la2': 'las',
            'na1': 'na',
        }
        # version = self.watcher.data_dragon.versions_for_region(regions[self.region])

            
    def match_stats(self, data):
        champ = data['championName']
        won = "VICTORIA" if data["win"]==True else "DERROTA"
        kda = f"{data['kills']}/{data['deaths']}/{data['assists']}"
        nivel = data['champLevel']
        goldEarned = data['goldEarned']
        cs = data['totalMinionsKilled']
        return champ, won, kda, nivel, cs


if __name__ == "__main__":
    name = DataFinder(region='la2', userName='joshele')
    x = name.data_dragon()