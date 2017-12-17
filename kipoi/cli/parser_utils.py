"""Utility functions for CLI parsing
"""
from __future__ import absolute_import
from __future__ import print_function

import kipoi


# parsers

def add_source(parser, default="kipoi"):
    parser.add_argument('--source', default=default,
                        choices=list(kipoi.config.model_sources().keys()),
                        help='Model source to use. Specified in ~/.kipoi/config.yaml' +
                        " under model_sources. " +
                        "'dir' is an additional source referring to the local folder.")


def add_model(parser, source="kipoi"):
    parser.add_argument('model', help='Model name.')
    add_source(parser, default=source)


def add_dataloader_main(parser, with_args=True):
    parser.add_argument('dataloader', help='Dataloader name.')
    parser.add_argument('--source', default="kipoi",
                        choices=list(kipoi.config.model_sources().keys()),
                        help='Dataloader source to use. Specified in ~/.kipoi/config.yaml' +
                        " under model_sources. " +
                        "'dir' is an additional source referring to the local folder.")
    if with_args:
        parser.add_argument('--dataloader_args',
                            help="Dataloader arguments either as a json string:'{\"arg1\": 1} or " +
                            "as a file path to a json file")


def add_dataloader(parser, with_args=True):
    parser.add_argument('--dataloader', default=None,
                        help="Dataloader name. If not specified, the model's default" +
                        "DataLoader will be used")
    parser.add_argument('--dataloader_source', default="kipoi",
                        help="Dataloader source")

    if with_args:
        parser.add_argument('--dataloader_args',
                            help="Dataloader arguments either as a json string:" +
                            "'{\"arg1\": 1} or as a file path to a json file")