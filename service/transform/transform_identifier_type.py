import logging

from models.aton.nodes.data_dictionary.context.dd_identifier_type_context import DDIdentifierTypeContext
from models.aton.nodes.data_dictionary.context.identifier_types_context import IdentifierTypesContext
from models.aton.nodes.data_dictionary.data_dictionary import DataDictionary
from models.aton.nodes.data_dictionary.dd_identifier_type import DD_IdentifierType
from models.aton.nodes.data_dictionary.identifier_types import IdentifierTypes
from models.data_classes.identifier_type import IdentifierTypesDC
from util.common_utils import parse_schema, parse_entities

log = logging.getLogger(__name__)


def transform_identifier_type(id_types: IdentifierTypesDC, data_dictionary:DataDictionary):
    identifier_types: IdentifierTypes = IdentifierTypes(definition="Identifier Types node")
    identifier_types.context = IdentifierTypesContext(identifier_types)
    for id_type in id_types.identifier_types:
        log.info(f"Transforming identifier type: {id_type}")
        log.info(f"Transforming identifier type: {id_type.code}")
        log.info(f"Identifier type's applicable entities: {id_type.applicable_entities}")
        log.info(f"Applicable Entities: {parse_entities(id_type.applicable_entities)}")
        applicable_entities = parse_entities(id_type.applicable_entities)
        log.info(f"Identifier type's node schema: {id_type.node_schema}")
        log.info(f"Node schema parsed into json string: {parse_schema(id_type.node_schema)}")
        node_schema = parse_schema(id_type.node_schema)
        dd_identifier_type: DD_IdentifierType = DD_IdentifierType(code=id_type.code,
                                                                  value=id_type.value,
                                                                   description=id_type.description,
                                                                  applicable_entities=applicable_entities,
                                                                  node_schema=node_schema,
                                                                  label_name=id_type.label_name,
                                                                  relationship_name=id_type.relationship_name)
        identifier_types.context.add_dd_identifier_type(dd_identifier_type)
        data_dictionary.context.set_identifier_types(identifier_types)
