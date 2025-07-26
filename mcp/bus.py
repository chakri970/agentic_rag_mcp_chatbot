from typing import Dict, Callable
from mcp.message import MCPMessage


class MCPBus:
    def __init__(self):
        self.agents: Dict[str, Callable[[MCPMessage], None]] = {}

    def register_agent(self, name: str, handler: Callable[[MCPMessage], None]):
        self.agents[name] = handler

    def send(self, message: MCPMessage):
        receiver = message.receiver
        if receiver not in self.agents:
            raise ValueError(f"Receiver agent '{receiver}' not registered.")
        self.agents[receiver](message)
