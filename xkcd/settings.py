# -*- encoding: utf-8 -*-

from argparse import ArgumentParser


class Settings(object):  # pragma: no cover
    def __init__(self):
        self.arg_parser = self.setup_arg_parser()
        self.options = self.setup_arg_options()

    @staticmethod
    def setup_arg_parser():
        return ArgumentParser(
            prog='xkcd-Clock',
            add_help=True
        )

    def setup_arg_options(self):
        self.add_arguments()
        ag = ArgumentListener(self.arg_parser)
        return ag.options

    def add_arguments(self):
        self.arg_parser.add_argument("-s", "--summertime",
                                     help="Activates summertime", action="store_true")


class ArgumentListener(object):  # pragma: no cover
    def __init__(self, arg_parser):
        self.arg_parser = arg_parser
        self.options = self.arg_parser.parse_args()
