import argparse
from FunnyJsonExplorer import FunnyJsonExplorer


def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer(FJE)")
    parser.add_argument("-f", "--filepath", required=True, type=str, help="Path of the json file")
    parser.add_argument("-s", "--style", type=str, default="tree", choices=['tree', 'rectangle'],
                        help="Visualization style (tree, rectangle)")
    parser.add_argument("-i", "--icons", type=str, default="none",
                        help="Icon family (eg. poker-face, weather)")
    args = parser.parse_args()

    explorer = FunnyJsonExplorer(args.style)
    explorer.load_icon_families(args.icons)
    explorer.show(args.filepath)


if __name__ == '__main__':
    main()
