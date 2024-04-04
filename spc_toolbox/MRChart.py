from typing import Dict, Callable, Concatenate, ParamSpec, TypeVar, Union
import pandas as pd
from spc_toolbox import ControlChart
from spc_toolbox.utils import get_chart_constant

P = ParamSpec('P')
R = TypeVar('R')


class MRChart(ControlChart):
    def __init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {}):
        """Initializes a MRChart object."""
        super().__init__(rules)

    def fit(self,
            index: Union[pd.Series, pd.Index],
            values: pd.Series,
            n: int = 2,
            **kwargs
        ):
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        if not isinstance(values, pd.Series):
            raise TypeError("values must be a Series.")
        if type(n) != int:
            raise ValueError("n must be an integer.")
        if n < 1:
            raise ValueError("n must be greater than 0.")
        
        moving_range = values.diff(n - 1).abs()
        moving_range_average = values.diff(n - 1).abs().mean()

        D4 = get_chart_constant('D4', n)
        D3 = get_chart_constant('D3', n)
        d2 = get_chart_constant('d2', n)
        self.sigma = moving_range_average / d2

        center_line = moving_range_average
        upper_control_limit = D4 * moving_range_average
        lower_control_limit = D3 * moving_range_average
        
        super().fit(index, moving_range, lower_control_limit, center_line, upper_control_limit)
        return self
 