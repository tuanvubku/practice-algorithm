from collections import defaultdict
from bisect import  bisect_left, bisect_right
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.persons = persons 
        self.times = times
        self.cnt = defaultdict(int)
        # store lead at every moment t
        self.leads = []
        self.current_lead, self.numOfVotesLeading = -1, 0
        
        
        for p,t in zip(persons, times):
            # Calculate current rank tai moi thoi diem t
            self.cnt[p] += 1
            temp = self.cnt[p]

            # check is new lead
            if p == self.current_lead:
                self.numOfVotesLeading = temp
            if p != self.current_lead and temp >= self.numOfVotesLeading:
                self.numOfVotesLeading = temp
                self.current_lead = p
            
            # append new lead at t
            self.leads.append((t, self.current_lead))
    def q(self, t: int) -> int:
        print(self.leads)
        # search ai t who lead
        index = bisect_right(self.leads, (t,float('inf')))
        print(index)
        return self.leads[index-1][1]
# Your TopVotedCandidate object will be instantiated and called as such:
persons = [0,0,0,0,1]
times = [0,6,39,52, 75]
obj = TopVotedCandidate(persons, times)
param_1 = obj.q(99)
print(param_1)