from typing import List

import pandas as pd


def get_df_from_model_list(*, models: List):
    return pd.DataFrame([model.model_dump() for model in models])
