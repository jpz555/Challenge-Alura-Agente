from dataclasses import dataclass, field
from langchain_core.messages import BaseMessage


@dataclass
class ChatSession:
    messages: list[BaseMessage] = field(default_factory=list)
    def reset(self):
        self.messages.clear()
