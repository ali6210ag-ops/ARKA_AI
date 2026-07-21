from memory.memory import ARKAMemory


class BrainEngine:
    def __init__(self):
        self.memory = ARKAMemory()
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def list_agents(self):
        return list(self.agents.keys())

    def remember(self, category, content):
        self.memory.save(category, content)

    def recall(self):
        return self.memory.read()