from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_identifier_type import DD_IdentifierType
from models.aton.nodes.data_dictionary.identifier_types import IdentifierTypes


def upsert_identifier_type(identifier_types: IdentifierTypes, data_dictionary: DataDictionary):
    identifier_types_node, is_created = IdentifierTypes.get_or_create(identifier_types)
    if is_created:
        data_dictionary.identifier_types.connect(identifier_types_node)
    for dd_identifier_type in identifier_types.context.get_dd_identifier_types():
        dd_identifier_type_node, is_dd_identifier_type_created = DD_IdentifierType.get_or_create(
            dd_identifier_type
        )
        # if dd_identifier_type_node:
        #     identifier_types_node.dd_identifier_type.connect(dd_identifier_type_node)
        #     dd_identifier_type_node.context = dd_identifier_type.context