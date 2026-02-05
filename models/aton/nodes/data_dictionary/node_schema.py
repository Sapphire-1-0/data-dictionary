from dataclasses import dataclass


@dataclass
class NodeSchema:
    propertyName: str
    propertyType: str
    mandatory: bool