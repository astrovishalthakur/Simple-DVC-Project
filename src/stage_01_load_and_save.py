from pkgutil import get_data
import pandas as pd
import argparse
from src.utils.common_utils import *
# import logging

def get_data(config_path):
    config = read_params(config_path)

    data_path = config["data_source"]["github_source"]
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_data_dir = config["artifacts"]["raw_local_data_dir"]
    raw_local_data = config["artifacts"]["raw_local_data"]

    clean_prev_dirs_if_exists(artifacts_dir)

    create_dir(dirs=[artifacts_dir, raw_local_data_dir])

    df = pd.read_csv(data_path, sep=",")

    save_local_df(df, raw_local_data, header=True)

    return None


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()


    try:
        data = get_data(config_path=parsed_args.config)
    except Exception as e:
        raise e