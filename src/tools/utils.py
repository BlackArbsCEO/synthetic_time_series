import pandas as pd
import numpy as np
from pathlib import Path
import dask
import dask.dataframe
import logzero
from src.CONSTANTS import *

# =============================================================================
## setup logger

def setup_system_logger(out_log_fp, pdir, logger):
    """
    setup logger for various package modules

    Params
    ------
    out_log_fp: str
        log file fp name doesn't include extension fn will add it
    logger: logzero logger object

    Returns
    -------
    logger: logzero logger instance
    """
    now = pd.to_datetime('now', utc=True)
    file_ = out_log_fp + f'_{now.date()}.log'
    logfile = Path(pdir / 'logs' / file_).as_posix()
    check_path(logfile)
    formatter = logzero.LogFormatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
    logzero.setup_default_logger(logfile=logfile, formatter=formatter)
    return logger

# =============================================================================
# general utils

def get_relative_project_dir(project_repo_name=None, partial=True):
    """
    helper fn to get local project directory

    :param project_repo_name: str, name of top level local project directory
    :param partial: bool, allow partial matches
    :return:
    """
    current_working_directory = Path.cwd()
    cwd_parts = current_working_directory.parts
    if partial:
        while project_repo_name not in cwd_parts[-1]:
            current_working_directory = current_working_directory.parent
            cwd_parts = current_working_directory.parts
    else:
        while cwd_parts[-1] != project_repo_name:
            current_working_directory = current_working_directory.parent
            cwd_parts = current_working_directory.parts
    return current_working_directory


def check_path(fp):
    """
    create file directory if it doesn't exist

    :param fp: str, filepath
    :return:
    """
    if not Path(fp).exists():

        if len(Path(fp).suffix) > 0:  # check if file
            Path(fp).parent.mkdir(exist_ok=True, parents=True)

        else:  # or directory
            Path(fp).mkdir(exist_ok=True, parents=True)


def cprint(df, nrows=None, sample=False):
    """
    custom print function to view pandas and dask dataframes

    :param df: dataframe
    :param nrows: number of rows to return
    :param sample: bool, return random sample for view
    :return:
    """
    if not isinstance(df, (pd.DataFrame, dask.dataframe.DataFrame)):
        try:
            df = df.to_frame()
        except:
            raise ValueError('object cannot be coerced to df')

    if not nrows: nrows = 5
    print('-' * 79)
    print('dataframe information')
    print('-' * 79)
    if sample:
        print(df.sample(nrows))
    else:
        print(df.tail(nrows))
    print('-' * 50)
    print(df.info())
    print('-' * 79)
    print()


def get_range(df, col):
    """
    get range of values from dataframe column

    :param df: pd.DataFrame
    :param col: column
    :return: tuple min, max values
    """
    return df[col].min(), df[col].max()
# =============================================================================