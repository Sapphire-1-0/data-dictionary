from dataclasses import dataclass, field


@dataclass
class IdentifierType:
    code: str
    value: str
    description: str
    applicable_entities: str
    label_name: str
    relationship_name: str
    node_schema: str

    def __str__(self):
        return (f"IdentifierType: "
                f" code: {self.code},"
                f" value: {self.value},"
                f" description: {self.description},"
                f" applicableEntities: {self.applicable_entities},"
                f" labelName: {self.applicable_entities},"
                f" relationshipName: {self.applicable_entities},"
                f" nodeSchema: {self.node_schema}")

@dataclass
class IdentifierTypesDC:
    identifier_types: list[IdentifierType] = field(default_factory=list)

    def __str__(self):
        return f"IdentifierTypesDC: {self.identifier_types}"