from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.counts = defaultdict(int)
        self.freq_map = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.counts[number]
    
        if old_freq > 0:
            self.freq_map[old_freq] -= 1
        
        new_freq = old_freq + 1
        self.counts[number] = new_freq
        
        self.freq_map[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.counts[number]
        
        if old_freq == 0:
            return
        
        self.freq_map[old_freq] -= 1
        
        new_freq = old_freq - 1
        self.counts[number] = new_freq
        
        if new_freq > 0:
            self.freq_map[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_map[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)