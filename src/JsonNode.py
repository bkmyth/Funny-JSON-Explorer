from abc import ABC, abstractmethod

"""
这里使用了组合模式.
组合模式的使用:
  Component 类是抽象基类,定义了所有组件的公共接⼝, 如方法 draw .
  Container 类是容器节点,为复合对象, 可以包含其他 Component 对象, 其重写的 draw 能够递归地绘制其子组件.
  Leaf 类是叶子节点, 其不会包含其他 Component 对象.
"""


class Component(ABC):
    def __init__(self, icon, name, is_first, is_leaf, is_last):
        self.icon = icon
        self.name = name
        # self.level = level
        self.is_first = is_first
        self.is_leaf = is_leaf
        self.is_last = is_last

    @abstractmethod
    def draw(self, style_config, depth, prefix, is_child_last):
        pass


class Container(Component):
    def __init__(self, icon, name, is_first, is_leaf, is_last, level):
        super().__init__(icon, name, is_first, is_leaf, is_last)
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, style_config, depth=0, prefix="", is_child_last=False):
        if depth != 0:
            if self.is_first:
                connector = style_config["first"]["start"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                pre_len = len(pre_str)
                pad = str(style_config["first"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["first"]["end"])
            elif self.is_last:
                prefix = (style_config["last"]["start"]["open"] + prefix[2:])
                connector = style_config["last"]["follow"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                pre_len = len(pre_str)
                pad = str(style_config["last"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["last"]["end"])
            else:
                connector = style_config["body"]["follow"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                pre_len = len(pre_str)
                pad = str(style_config["body"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["body"]["end"])
            print(f"{prefix}{connector} {self.icon}{self.name} {pad}")

            if depth > 1 or is_child_last:
                prefix += style_config["body"]["follow"]["lasting"]
            else:
                prefix += style_config["body"]["follow"]["opening"]

        for i, child in enumerate(self.children):
            child.draw(style_config, depth + 1, prefix, i == len(self.children) - 1)


class Leaf(Component):
    def __init__(self, icon, name, is_first, is_leaf, is_last, value):
        super().__init__(icon, name, is_first, is_leaf, is_last)
        self.value = value

    def draw(self, style_config, depth=0, prefix="", is_child_last=False):
        if depth != 0:
            if self.is_first:
                connector = style_config["first"]["start"]["last" if is_child_last else "open"]
                if self.value is None:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                else:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name}: {self.value} "
                pre_len = len(pre_str)
                pad = str(style_config["first"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["first"]["end"])
            elif self.is_last:
                prefix = (style_config["last"]["start"]["lasting" if is_child_last else "opening"] +
                          prefix[2:])
                connector = style_config["last"]["follow"]["last" if is_child_last else "open"]
                if self.value is None:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                else:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name}: {self.value} "
                pre_len = len(pre_str)
                pad = str(style_config["last"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["last"]["end"])
            else:
                connector = style_config["body"]["follow"]["last" if is_child_last else "open"]
                if self.value is None:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name} "
                else:
                    pre_str = f"{prefix}{connector} {self.icon}{self.name}: {self.value} "
                pre_len = len(pre_str)
                pad = str(style_config["body"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["body"]["end"])
            if self.value is None:
                print(f"{prefix}{connector} {self.icon}{self.name} {pad}")
            else:
                print(f"{prefix}{connector} {self.icon}{self.name}: {self.value} {pad}")

            if depth > 1 or is_child_last:
                prefix += style_config["body"]["follow"]["lasting"]
            else:
                prefix += style_config["body"]["follow"]["opening"]
