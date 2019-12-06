import os

import pandas as pd
import yaml


def load_config() -> dict:
    """
    load config file
    :return:
    """
    with open(os.getcwd() + "/conf/config.yaml", "r", encoding="utf-8") as conf_f:
        conf = yaml.safe_load(conf_f)
    return conf


if __name__ == "__main__":
    # load configuration file
    conf = load_config()
    # read input data
    records = pd.read_csv(conf["input"]["file_path"]+conf["input"]["file_name"], index_col="student_name")
    # calculate mean for every student
    records = pd.concat([records, pd.Series(records.mean(axis=1), name="average")], axis=1)
    # generate csv file
    for key, level in conf["level"].items():
        result = records[records["average"] > int(level["score"])]
        result["average"].to_csv(conf["output"]["file_path"]+level["output_file"], header=True)
