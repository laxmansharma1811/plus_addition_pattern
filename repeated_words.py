class Repeated:
    
    def __init__(self, words):
        self.words = words
    
    def repeat(self):
        result = []
        current = self.words[0]
        count = 0
        
        if not self.words:
            return []
        
        for char in self.words:
            if char == current:
                count += 1
            else:
                result.append((char, count))
                current = char
                count = 1
        result.append((char, count))
        return result
        
a = Repeated("aaabbb")

print(a.repeat())