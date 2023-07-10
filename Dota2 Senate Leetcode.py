class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        radiant_count = senate.count('R')
        dire_count = len(senate) - radiant_count
        radiant_banned = dire_banned = 0
        while radiant_banned < radiant_count and dire_banned < dire_count:
            senator = queue.popleft()
            if senator == 'R':
                if radiant_banned > 0:
                    radiant_banned -= 1
                else:
                    queue.append('R')
                    dire_banned += 1
            else:
                if dire_banned > 0:
                    dire_banned -= 1
                else:
                    queue.append('D')
                    radiant_banned += 1
        return 'Radiant' if dire_count == dire_banned else 'Dire'
