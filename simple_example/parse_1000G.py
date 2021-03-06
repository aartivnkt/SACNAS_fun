#!/usr/bin/env python3
"""Simple code to parse a 1000G file
and return a dict with mean allele
frequency across populations"""
import argparse
import logging
import numpy as np

logging.basicConfig(filename='test.log',
                    level='DEBUG')


def read_csv(input_csv: str)->dict:
    """
    Parse a 1000G input csv and return
    a dict with required information

    Args:
        input_csv: input_csv file

    Returns: dict

    """
    with open(input_csv, 'r') as input_file:
        # get headers from input file
        input_header = input_file.readline().strip().split(',')
        # loop over records, create a dict with required
        # fields, add mean_allele_frequency field, and
        # return dict
        record_list = []
        for record in input_file:
            input_fields = record.strip().split(',')
            row_dict = dict(zip(input_header, input_fields))
            row_dict['mean_allele_frequency'] = cal_mean_allele_frequency(
                row_dict
            )
            record_list.append(row_dict)
        return record_list


def cal_mean_allele_frequency(row_dict: dict)->float:
    """
    Return a mean allele frequency from a dict with
    allele frequency values as input

    Args:
        row_dict: dict with population allele
        frequencies

    Returns: float, mean allele frequency

    """
    return np.round(np.mean([
                float(row_dict['EAS_AF']),
                float(row_dict['AMR_AF']),
                float(row_dict['AFR_AF']),
                float(row_dict['EUR_AF'])
            ]),decimals=3)


def setup_parser()->argparse.ArgumentParser:
    """
    Set up argparse

    Returns: argparse argument parser

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv',
                        dest='input_csv',
                        required=True,
                        help='1000G input csv '
                             'file'
                        )
    return parser.parse_args()


def main():
    args = setup_parser()
    logging.info('Read args {}'.format(args))
    allele_frequencies = read_csv(args.input_csv)
    logging.info('allele_frequencies {}'.format(
        allele_frequencies
    ))


if __name__ == '__main__':
    main()
