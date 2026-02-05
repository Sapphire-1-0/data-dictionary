from models.aton.nodes.data_dictionary.dd_identifier_type import DD_IdentifierType
from models.aton.nodes.data_dictionary.identifier_types import IdentifierTypes


class IdentifierTypesContext:
    def __init__(self, identifier_types: IdentifierTypes):
        self.dd_disorder_types: list[DD_IdentifierType] = []

    def add_dd_identifier_type(self, dd_identifier_type: DD_IdentifierType):
        self.dd_disorder_types.append(dd_identifier_type)

    def get_dd_identifier_types(self):
        return self.dd_disorder_types