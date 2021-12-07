#!/usr/bin/env python

import argparse
import logging
from contextlib import ExitStack


def main(args: argparse.Namespace) -> None:
    with ExitStack() as stack:
        in_train_file = stack.enter_context(open(args.train_path, "r"))
        in_dev_file = stack.enter_context(open(args.dev_path, "r"))
        in_test_file = stack.enter_context(open(args.test_path, "r"))

        inf_train_file = stack.enter_context(open("train.ita.inf", "w"))
        psr_train_file = stack.enter_context(open("train.ita.psr", "w"))
        
        inf_dev_file = stack.enter_context(open("dev.ita.inf", "w"))
        psr_dev_file = stack.enter_context(open("dev.ita.psr", "w"))
        
        inf_test_file = stack.enter_context(open("test.ita.inf", "w"))
        psr_test_file = stack.enter_context(open("test.ita.psr", "w"))

        for line in in_train_file:
            inf, psr, cat = line.split("\t")
            inf = " ".join(inf) + " " + " ".join(cat.strip().split(";"))
            psr = " ".join(psr)
            print(inf, file=inf_train_file)
            print(psr, file=psr_train_file)

        for line in in_dev_file:
            inf, psr, cat = line.split("\t")
            inf = " ".join(inf) + " " + " ".join(cat.strip().split(";"))
            psr = " ".join(psr)
            print(inf, file=inf_dev_file)
            print(psr, file=psr_dev_file)

        for line in in_test_file:
            inf, psr, cat = line.split("\t")
            inf = " ".join(inf) + " " + " ".join(cat.strip().split(";"))
            psr = " ".join(psr)
            print(inf, file=inf_test_file)
            print(psr, file=psr_test_file)


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        format="%(levelname)s: %(message)s"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--train_path",
        type=str,
        required=True,
        help="path to input training data"
    )
    parser.add_argument(
        "--dev_path",
        type=str,
        required=True,
        help="path to input development data"
    )
    parser.add_argument(
        "--test_path",
        type=str,
        required=True,
        help="path to input test data"
    )
    main(parser.parse_args())


