# Funny JSON Explorer
JSON文件可视化的命令行界面简易工具
# 运行方法
我已经编写了.bat文件， 你可以直接在项目根目录执行以下命令：
```
fje  -f <json file path> -s <style> -i <icon family>
```
或者直接运行源码
```
python ./src/fje.py -f <json file path> -s <style> -i <icon family>
```
# 功能简介
FJE可以快速切换**风格**（style），包括：树形（tree）、矩形（rectangle），
也可以指定**图标族**（icon family），为中间节点或叶节点指定一套icon。
如果你想增加风格,那你需要添加必须的抽象工厂。
如果你想增加图标族,请直接修改配置文件`./config/icon_family.json`。
