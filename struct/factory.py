import json
import xml.etree.ElementTree as Etree
from typing import Union


class JSONConnector:
    def __init__(self, filepath):
        self.data = {}
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = Etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath: str) -> Union[JSONConnector, JSONConnector]:
    if filepath.endswith("json"):
        connector = JSONConnector
    elif filepath.endswith("xml"):
        connector = XMLConnector
    else:
        raise ValueError(f"Cannot connect to {filepath}")
    return connector(filepath)


def connect_to(filepath: str):
    factory = None
    try:
        factory = connector_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


if __name__ == "__main__":
    xml_instance = connect_to("../data/person.xml")
    print(xml_instance.parsed_data)
    json_instance = connect_to("../data/donut.json")
    print(json_instance.parsed_data)
