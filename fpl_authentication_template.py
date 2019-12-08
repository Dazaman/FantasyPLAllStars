import asyncio
import aiohttp
from prettytable import PrettyTable
import numpy as np
from fpl import FPL
import pprint


## sudo $(which pip) install fpl


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()
        await fpl.login(email='balreddy27@gmail.com' , password='balreddy@27')
        user = await fpl.get_user(4752994)
        my_team = await user.get_team()
        my_picks = await user.get_picks()
        p = await fpl.get_player(460)
        
    team = np.array(my_team)
    players = np.array(players)

    print('\nmyteam  : ',team.shape, team[0])
    # print('\nmypicks  : ',my_picks.shape, team[0])
    print('players : ', players.shape, players[0])
    
    print(p)

    top_performers = sorted(
        players, key=lambda x: x.goals_scored + x.assists, reverse=True)

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "G", "A", "G + A"]
    player_table.align["Player"] = "l"

    for player in top_performers[:10]:
        goals = player.goals_scored
        assists = player.assists
        player_table.add_row([player.web_name, f"£{player.now_cost / 10}",
                            goals, assists, goals + assists])

    print(player_table)

if __name__ == "__main__":
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())