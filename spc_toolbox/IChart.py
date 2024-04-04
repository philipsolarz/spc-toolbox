from typing import Dict, Callable, Concatenate, ParamSpec, TypeVar, Union
import pandas as pd
import numpy as np
from spc_toolbox import ControlChart
from spc_toolbox.utils import get_chart_constant

P = ParamSpec('P')
R = TypeVar('R')

class IChart(ControlChart):
    def __init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {}):
        """Initializes an IChart object."""
        super().__init__(rules)

    def fit(self,
            index: Union[pd.Series, pd.Index],
            values: pd.Series,
            n: int = 2,
            **kwargs
        ):
        """
        Fits the IChart object to the data.
        
        """
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        if not isinstance(values, pd.Series):
            raise TypeError("values must be a Series.")
        if type(n) != int:
            raise TypeError("n must be an integer.")
        if n < 1:
            raise ValueError("n must be greater than 0.")
        
        sample_mean = values.mean()
        moving_range_average = values.diff(n - 1).abs().mean()

        E2 = get_chart_constant('A2', n) * np.sqrt(n)
        d2 = get_chart_constant('d2', n)
        self.sigma = moving_range_average / d2

        center_line = sample_mean
        upper_control_limit = sample_mean + E2 * moving_range_average
        lower_control_limit = sample_mean - E2 * moving_range_average
        
        super().fit(index, values, lower_control_limit, center_line, upper_control_limit)
        return self
