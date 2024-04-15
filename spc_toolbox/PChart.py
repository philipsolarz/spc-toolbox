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
            defectives: pd.Series, # defectives: pd.Series
            sample_sizes: Union[pd.Series, int], # sample_sizes: Union[pd.Series, int]
            z: float = 3.0,
            **kwargs
        ):
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        if not isinstance(defectives, pd.Series):
            raise TypeError("defectives must be a Series.")
        if not isinstance(sample_sizes, pd.Series) and not isinstance(sample_sizes, int):
            raise TypeError("sample_sizes must be a Series or an integer.")
        if type(z) != float:
            raise TypeError("z must be a float.")

        proportions = defectives / sample_sizes

        overall_proportion = defectives.sum() / sample_sizes.sum()

        std_dev = np.sqrt(proportions * (1 - proportions) / sample_sizes)
        self.sigma = std_dev

        center_line = overall_proportion
        # center_line = pd.Series([average_proportion] * len(index))
        upper_control_limit = overall_proportion + z * std_dev
        lower_control_limit = np.maximum(overall_proportion - z * std_dev, 0)

        super().fit(index, proportions, lower_control_limit, center_line, upper_control_limit)
        return self
