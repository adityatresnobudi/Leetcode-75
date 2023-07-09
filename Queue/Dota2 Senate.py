# make queue
# everytime ban happens, opposite ban counter + 1
# if next queue is the opposite side, then pop until ban counter goes back to zero

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue = deque(senate)
        countRadiant = senate.count("R")
        countDire = senate.count("D")
        bannedRadiant = 0
        bannedDire = 0

        while bannedRadiant < countRadiant and bannedDire < countDire:
            turn = queue.popleft()
            if turn == "R":
                if bannedRadiant == 0:
                    queue.append(turn)
                    bannedDire += 1
                else:
                    bannedRadiant -= 1
            else:
                if bannedDire == 0:
                    queue.append(turn)
                    bannedRadiant += 1
                else:
                    bannedDire -= 1
        
        return "Radiant" if countDire == bannedDire else "Dire"
