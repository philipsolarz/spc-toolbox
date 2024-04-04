from typing import Union, Dict, Callable, Concatenate, ParamSpec, TypeVar
import pandas as pd
import numpy as np
from spc_toolbox import ControlChart

P = ParamSpec('P')
R = TypeVar('R')

class UChart(ControlChart):
    def __init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {}):
        """Initializes a UChart object."""
        super().__init__(rules)

    def fit(self,
            index: Union[pd.Series, pd.Index],
            defects: pd.Series, # values: pd.Series
            sample_sizes: Union[pd.Series, int], # sample_sizes: Union[pd.Series, int]
            z: float = 3.0,
            **kwargs
        ):
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        if not isinstance(defects, pd.Series):
            raise TypeError("defective_items must be a Series.")
        if not isinstance(sample_sizes, pd.Series) and not isinstance(sample_sizes, int):
            raise TypeError("sample_sizes must be a Series or an integer.")
        if type(z) != float:
            raise TypeError("z must be a float.")

        defects_per_item = defects / sample_sizes
        defects_per_item.name = "Defects Per Item"
        average_defects_per_item = defects_per_item.mean()

        std_dev = np.sqrt(average_defects_per_item / sample_sizes)
        self.sigma = std_dev

        center_line = average_defects_per_item
        upper_control_limit = average_defects_per_item + z * std_dev
        lower_control_limit = np.maximum(average_defects_per_item - z * std_dev, 0)

        super().fit(index, defects_per_item, lower_control_limit, center_line, upper_control_limit)
        return self
