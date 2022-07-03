from networkx.algorithms.structuralholes import constraint
import pandas as pd
from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from causalnex.structure.notears import from_pandas
from logs import log
import os, sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts"))
)
from causal import Causal

causal = Causal()


data = pd.read_csv("../data/data_clean.csv")

sel_feat = data[
    [
        "diagnosis",
        "concave points_mean",
        "radius_worst",
        "concave points_worst",
        "perimeter_worst",
        "area_mean",
        "area_worst",
        "perimeter_mean",
        "radius_mean",
    ]
]


def get_causal_model(data):
    """Get Causal Model

    Args:
        data (_type_): _description_
        structural_model (_type_): _description_

    Returns:
        _type_: _description_
    """
    sample_80 = sel_feat.sample(frac=0.5, random_state=42)
    sm_80 = from_pandas(sample_80, tabu_parent_nodes=["diagnosis"])
    return sm_80


if __name__ == "__main__":
    sm_80 = get_causal_model(data)
    causal.plot_structure_model(sm_80, threshold=0)
