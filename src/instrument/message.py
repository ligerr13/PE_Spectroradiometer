from dataclasses import dataclass
from typing import Dict


@dataclass
class Message:
    params: Dict[str, any]
    message: bytes
