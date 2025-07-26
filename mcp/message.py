from typing import Any, Dict


class MCPMessage:
    def __init__(
        self,
        type: str,
        sender: str,
        receiver: str,
        trace_id: str,
        payload: Dict[str, Any]
    ):
        self.type = type
        self.sender = sender
        self.receiver = receiver
        self.trace_id = trace_id
        self.payload = payload

    def to_dict(self):
        return {
            "type": self.type,
            "sender": self.sender,
            "receiver": self.receiver,
            "trace_id": self.trace_id,
            "payload": self.payload
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return MCPMessage(
            type=data["type"],
            sender=data["sender"],
            receiver=data["receiver"],
            trace_id=data["trace_id"],
            payload=data["payload"]
        )
