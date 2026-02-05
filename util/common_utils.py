import json
from dataclasses import asdict

from models.aton.nodes.data_dictionary.node_schema import NodeSchema


def convert_camel_to_snake(data: dict) -> dict:
    """Convert camelCase keys to snake_case"""
    return {
        ''.join(['_' + c.lower() if c.isupper() else c for c in k]).lstrip('_'): v
        for k, v in data.items()
    }

def parse_schema(schema_str: str) -> str:
    """Parse a schema string into a JSON string"""
    node_schemas = []

    # split by |
    parts = schema_str.split("|")

    for part in parts:
        # split each segment by :
        name, type_, mandatory = part.split(":")

        node_schemas.append(
            NodeSchema(
                propertyName=name,
                propertyType=type_,
                mandatory=mandatory.lower() == "yes"
            )
        )

    # convert dataclass objects → dict → JSON string
    return json.dumps(
        [asdict(ns) for ns in node_schemas],
        indent=2
    )

def parse_entities(entities_str: str) -> list[str]:
    """Parse a string of entities into a list of strings"""
    return [e.strip() for e in entities_str.split("|") if e.strip()]