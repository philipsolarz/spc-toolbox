from typing import Union, Dict, Callable, Concatenate, ParamSpec, TypeVar
import pandas as pd
import numpy as np
from spc_toolbox import ControlChart

P = ParamSpec('P')
R = TypeVar('R')

class PChart(ControlChart):
    def __init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {}):
        """Initializes a PChart object."""
        super().__init__(rules)

    def fit(self,
            index: Union[pd.Series, pd.Index],
            defective_items: pd.Series, # values: pd.Series
            total_items: Union[pd.Series, int], # sample_sizes: Union[pd.Series, int]
            z: float = 3.0,
            **kwargs
        ):
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        if not isinstance(defective_items, pd.Series):
            raise TypeError("defective_items must be a Series.")
        if not isinstance(total_items, pd.Series) and not isinstance(total_items, int):
            raise TypeError("total_items must be a Series or an integer.")
        if type(z) != float:
            raise TypeError("z must be a float.")

        proportions = defective_items / total_items
        average_proportion = proportions.mean()

        std_dev = np.sqrt(proportions * (1 - proportions) / total_items)
        self.sigma = std_dev

        center_line = average_proportion
        upper_control_limit = average_proportion + z * std_dev
        lower_control_limit = np.maximum(average_proportion - z * std_dev, 0)

        super().fit(index, proportions, lower_control_limit, center_line, upper_control_limit)
        return self
