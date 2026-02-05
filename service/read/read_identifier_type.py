import logging
import os

from models.data_classes.identifier_type import IdentifierTypesDC, IdentifierType
from service.read.read_util import read_csv
from util.common_utils import convert_camel_to_snake

log = logging.getLogger(__name__)




def read_identifier_type() -> IdentifierTypesDC:
    log.debug("Reading identifier type")
    # Go up two levels from current file to reach project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Path to disorder types folder
    base_dir = os.path.join(project_root, "dictionary_files", "identifier_types")

    if not os.path.exists(base_dir):
        raise FileNotFoundError(f" Identifier types directory not found: {base_dir}")

    # Define category mapping (filename prefix -> category name)
    identifier_data = {
        "identifier_types": []
    }

    identifier_type_data = []

    # Loop through each CSV file in the folder
    for filename in os.listdir(base_dir):
        log.debug("Reading file: {}".format(filename))
        if filename.endswith("identifier_types.csv"):
            raw_data = read_csv(filename, base_dir)
            # Convert each dictionary to an IdentifierType instance
            identifier_type_data = [IdentifierType(**convert_camel_to_snake(item)) for item in raw_data]

    return IdentifierTypesDC(identifier_types=identifier_type_data)