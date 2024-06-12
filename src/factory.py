from abc import ABC, abstractmethod
from JsonNode import *

"""
这里使用了工厂方法模式和抽象工厂模式.
工厂方法的使用:
1.StyleFactory 类是一个抽象工厂基类, 提供一个创建获取不同可视化风格的接口 get_style .
  TreeStyleFactory 和 RectangleStyleFactory 继承自 StyleFactory 并实现了 get_style 方法,
  分别用于创建 TreeStyle 和 RectangleStyle 对象.这三个类提供了创建 Style 对象的不同子类的方法.
  Style 是抽象产品, 而 TreeStyle 和 RectangleStyle 是它的子类,为具体产品.
2.NodeFactory 类,其展示工厂方法的使用.
  这个类提供三个静态方法/接口 create_root 、create_container 、 create_leaf, 三个方法/接口用于创建不同类型的json节点,
  由这个工厂类决定要实例化(创建)的节点是哪种类型.
抽象工厂模式:
  这里由于底层设计不当,导致实际上并不能完全体现抽象工厂模式的思想.
  AbstractFactory 提供两个接口,一个用于创建风格,一个用于创建节点.
  理论上 node_factory 和 style_factory 应该负责创建一组相互关联的产品
  但由于底层设计的不当,实际上风格与节点这两个并不互相依赖和关联,导致到并不能很好地体现抽象工厂模式的思想.
  由于本次作业截止的时间快到了,我也没有时间再进行修正完善.会争取下一次完善.
"""


class AbstractFactory:
    def __init__(self, style):
        self.node_factory = NodeFactory()
        self.style_factory = None
        if style == "tree":
            self.style_factory = TreeStyleFactory()
        elif style == "rectangle":
            self.style_factory = RectangleStyleFactory()

    def get_style(self):
        return self.style_factory.get_style()

    def get_node(self):
        return self.node_factory


class StyleFactory(ABC):
    @abstractmethod
    def get_style(self):
        pass


class TreeStyleFactory(StyleFactory):
    def get_style(self):
        return TreeStyle()


class RectangleStyleFactory(StyleFactory):
    def get_style(self):
        return RectangleStyle()


class Style(ABC):
    def __init__(self, first, body, last):
        self.first = first
        self.body = body
        self.last = last
        self.style_config = {}

    @abstractmethod
    def set_style_config(self):
        pass

    def get_style_config(self):
        return self.style_config


class TreeStyle(Style):
    def __init__(self):
        super().__init__({}, {}, {})
        self.set_style_config()

    def set_style_config(self):
        self.first = {
            "padding": " ",
            "start": {
                "open": "├─",
                "opening": "│  ",
                "last": "└─",
                "lasting": "  "
            },
            "follow": {
                "open": "├─",
                "opening": "│  ",
                "last": "└─",
                "lasting": "  "
            },
            "end": " "
        }
        self.body = {
            "padding": " ",
            "start": {
                "open": "├─",
                "opening": "│  ",
                "last": "└─",
                "lasting": "  "
            },
            "follow": {
                "open": "├─",
                "opening": "│  ",
                "last": "└─",
                "lasting": "  "
            },
            "end": " "
        }
        self.last = {
            "padding": " ",
            "start": {
                "open": "└─",
                "opening": "└─",
                "last": "└─",
                "lasting": "  "
            },
            "follow": {
                "open": "├─",
                "opening": "│  ",
                "last": "└─",
                "lasting": "   "
            },
            "end": " "
        }
        self.style_config = {"first": self.first, "body": self.body, "last": self.last}


class RectangleStyle(Style):
    def __init__(self):
        super().__init__({}, {}, {})
        self.set_style_config()

    def set_style_config(self):
        self.first = {
            "padding": "─",
            "start": {
                "open": "┌─",
                "opening": "│  ",
                "last": "├─",
                "lasting": "│  "
            },
            "follow": {
                "open": "┌─",
                "opening": "│  ",
                "last": "├─",
                "lasting": "│  "
            },
            "end": "─┐"
        }
        self.body = {
            "padding": "─",
            "start": {
                "open": "├─",
                "opening": "│  ",
                "last": "├─",
                "lasting": "│  "
            },
            "follow": {
                "open": "├─",
                "opening": "│  ",
                "last": "├─",
                "lasting": "│  "
            },
            "end": "─┤"
        }
        self.last = {
            "padding": "─",
            "start": {
                "open": "└─",
                "opening": "└─",
                "last": "└─",
                "lasting": "└─"
            },
            "follow": {
                "open": "┴─",
                "opening": "┴─",
                "last": "┴─",
                "lasting": "┴─"
            },
            "end": "─┘"
        }
        self.style_config = {"first": self.first, "body": self.body, "last": self.last}


class NodeFactory:
    @staticmethod
    def create_root(icon):
        return Container(icon, 'root', False, False, False, None)

    @staticmethod
    def create_container(icon, name, is_first, is_last):
        return Container(icon, name, is_first, False, is_last, None)

    @staticmethod
    def create_leaf(icon, name, is_first, is_last, value):
        return Leaf(icon, name, is_first, True, is_last, value)
