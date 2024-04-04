from typing import Dict, Callable, Concatenate, ParamSpec, TypeVar, Union
import pandas as pd
from spc_toolbox import ControlChart
from spc_toolbox.utils import get_chart_constant

P = ParamSpec('P')
R = TypeVar('R')

class XBarChart(ControlChart):
    def __init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {}):
        """Initializes an XBarChart object."""
        super().__init__(rules)

    def fit(self,
            index: Union[pd.Series, pd.Index],
            values: pd.DataFrame,
            axis: int = 0,
            dispersion_type: str = "range",
            **kwargs
        ):
        if not isinstance(index, pd.Series) and not isinstance(index, pd.Index):
            raise TypeError("index must be a Series or an Index.")
        if isinstance(index, pd.Index):
            index = pd.Series(index)
        
        if not isinstance(values, pd.DataFrame):
            raise TypeError("values must be a DataFrame.")
        
        if not isinstance(axis, (int, str)):
            raise ValueError("Invalid axis. Must be either 'index' (0), 'columns' (1), 0, or 1")
        
        if isinstance(axis, str):
            if axis.lower() == 'index':
                axis = 0
            elif axis.lower() == 'columns':
                axis = 1
            else:
                raise ValueError("String value for axis must be 'index' or 'columns'")
            
        if axis not in [0, 1]:
            raise ValueError("Integer value for axis must be 0 (for index) or 1 (for columns)")
        
        if dispersion_type not in ["range", "std_dev"]:
            raise ValueError("Invalid dispersion type. Please use 'range' or 'std_dev'.")
        
        subgroup_sizes = values.count(axis=axis, numeric_only=True)
        subgroup_means = values.mean(axis=axis)
        subgroup_means.name = "Mean"
        subgroup_ranges = values.max(axis=axis) - values.min(axis=axis)
        subgroup_std_devs = values.std(axis=axis)

        average_subgroup_mean = subgroup_means.mean()
        average_subgroup_range = subgroup_ranges.mean()
        average_subgroup_std_dev = subgroup_std_devs.mean()

        if dispersion_type == "range":
            A2 = subgroup_sizes.apply(lambda x: get_chart_constant('A2', x))
            d2 = subgroup_sizes.apply(lambda x: get_chart_constant('d2', x))
            d3 = subgroup_sizes.apply(lambda x: get_chart_constant('d3', x))
            f = (d2 ** 2) / (d3 ** 2)
            self.sigma = (f * subgroup_ranges).sum() / (f / d2).sum()

            center_line = average_subgroup_mean
            upper_control_limit = average_subgroup_mean + A2 * average_subgroup_range
            lower_control_limit = average_subgroup_mean - A2 * average_subgroup_range
        else:
            A3 = subgroup_sizes.apply(lambda x: get_chart_constant('A3', x))
            c4 = subgroup_sizes.apply(lambda x: get_chart_constant('c4', x))
            h = (c4 ** 2) / ((1 - c4) ** 2)
            self.sigma = (h * subgroup_std_devs / c4).sum() / h.sum()
            
            center_line = average_subgroup_mean
            upper_control_limit = average_subgroup_mean + A3 * average_subgroup_std_dev
            lower_control_limit = average_subgroup_mean - A3 * average_subgroup_std_dev

        super().fit(index, subgroup_means, lower_control_limit, center_line, upper_control_limit)
        return self
