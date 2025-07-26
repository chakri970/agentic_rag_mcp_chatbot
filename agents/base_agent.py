from abc import ABC, abstractmethod
from mcp.message import MCPMessage
from mcp.bus import MCPBus


class BaseAgent(ABC):
    def __init__(self, name: str, bus: MCPBus):
        self.name = name
        self.bus = bus
        self.bus.register_agent(self.name, self.receive)

    def send(self, message: MCPMessage):
        self.bus.send(message)

    @abstractmethod
    def receive(self, message: MCPMessage):
        pass
