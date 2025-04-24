
class Memory:
    passwords=[]
    context=[]
    def __init__(self):
        self.passwords=[{"AWS":"abcd1234","OpenAI":"TSAIistheBEST"}]
        

    def getMemory(self):
        return self.context
    
    def appendMemory(self,mem):
        self.context.append(mem)