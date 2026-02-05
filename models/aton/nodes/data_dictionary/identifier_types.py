from typing import Any

from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, DoesNotExist


class IdentifierTypes(StructuredNode):
    definition: str = StringProperty(required=True)
    dd_identifier_type = RelationshipTo("models.aton.nodes.data_dictionary.dd_identifier_type.DD_IdentifierType",
                                        "DEFINED_BY")

    data_dictionary = RelationshipFrom("models.aton.nodes.data_dictionary.data_dictionary.DataDictionary", "IDENTIFIER_TYPES_DEFINED")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "IdentifierTypes") -> tuple["IdentifierTypes", bool]:
        try:
            node = cls.nodes.get(definition=instance.definition)
            created = False
        except DoesNotExist:
            node = cls(definition=instance.definition).save()
            created = True
        return node, created