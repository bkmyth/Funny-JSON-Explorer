import json
from factory import *


class FunnyJsonExplorer:
    def __init__(self, style):
        self.abstract_factory = AbstractFactory(style)
        self.node_factory = self.abstract_factory.get_node()
        self.icon_family = None

    @staticmethod
    def load_json(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data

    def load_icon_families(self, icon_family_name):
        config_path = './config/icon_family.json'
        icon_family_config = self.load_json(config_path)
        if icon_family_name == "none":
            self.icon_family = {"middle": " ", "leaf": " "}
        elif icon_family_name in icon_family_config:
            self.icon_family = icon_family_config[icon_family_name]
        else:
            raise ValueError(f"Icon family {icon_family_name} not found in configure.")

    def parser_json(self, json_data, parent=None, is_first=True, is_last=True):
        if parent is None:
            parent = self.node_factory.create_root(self.icon_family['middle'])
        for i, (key, value) in enumerate(json_data.items()):
            if isinstance(value, dict):
                node = self.node_factory.create_container(self.icon_family['middle'], key, (is_first and (i == 0)),
                                                          False)
                parent.add(node)
                self.parser_json(value, node, False, (is_last and (i == len(json_data.items()) - 1)))
            else:
                leaf = self.node_factory.create_leaf(self.icon_family['leaf'], key, (is_first and (i == 0)),
                                                     (is_last and (i == len(json_data.items()) - 1)), value)
                parent.add(leaf)
                # print("----" + leaf.name)
                # print("++++" + str(leaf.is_first))
                # print("++++" + str(leaf.is_last))
        # print(parent.name)
        # print("++++" + str(parent.is_first))
        # print("++++" + str(parent.is_last))
        return parent

    def show(self, json_file_path):
        json_data = self.load_json(json_file_path)
        root_node = self.parser_json(json_data)
        style = self.abstract_factory.get_style()
        style_config = style.get_style_config()
        root_node.draw(style_config, 0, "", False)
