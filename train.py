from dela_cond_detr.main import get_args_parser, main
import argparse
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Conditional DETR training and evaluation script', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
    # my_args = sys.argv
    # print("In mymodule:")
    # for arg in my_args:
    #     print(arg)

