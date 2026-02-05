from typing import Any

from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipFrom, DoesNotExist


class DD_IdentifierType(StructuredNode):
    code = StringProperty(required=True)
    value = StringProperty(required=True)
    description = StringProperty(required=False, db_property='description')
    applicable_entities = ArrayProperty(required=False, db_property='applicable_entities')
    label_name = StringProperty(required=False, db_property='labelName')
    relationship_name = StringProperty(required=False, db_property='relationshipName')
    node_schema = StringProperty(required=False, db_property='nodeSchema')

    identifier_types = RelationshipFrom('models.aton.nodes.data_dictionary.identifier_types.IdentifierTypes',
                                        'DEFINED_BY')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: Any = None

    @classmethod
    def get_or_create(cls, instance: "DD_IdentifierType") -> tuple["DD_IdentifierType", bool]:
        try:
            node = cls.nodes.get(code=instance.code)
            created = False
        except DoesNotExist:
            node = cls(value=instance.value,
                       code=instance.code,
                       description=instance.description,
                       applicable_entities=instance.applicable_entities,
                       label_name=instance.label_name,
                       relationship_name=instance.relationship_name,
                       node_schema=instance.node_schema).save()
            created = True
        return node, created