# XBarChart Class Documentation

The `XBarChart` class extends the `ControlChart` from the `spc_toolbox` package. It is specifically designed to create and manage X-Bar Charts, which are used in statistical process control (SPC) for monitoring the process mean over time.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes an `XBarChart` object with an optional set of rules for SPC analysis.

- **Parameters**
  - `rules`: A dictionary where keys are rule names and values are callable functions that define the rule's logic. Defaults to an empty dictionary.

### `fit(self, index: Union[pd.Series, pd.Index], values: pd.DataFrame, axis: int = 0, dispersion_type: str = "range", **kwargs)`

Fits the data to the XBarChart, calculating the control limits and center line based on the specified dispersion measure (range or standard deviation).

- **Parameters**
  - `index`: The index (e.g., time, batch number) for the data points. Can be a `pandas.Series` or `pandas.Index`.
  - `values`: A `pandas.DataFrame` containing the measured values for each subgroup.
  - `axis`: Determines whether subgroups are defined along rows (`0` or `'index'`) or columns (`1` or `'columns'`). Default is `0`.
  - `dispersion_type`: Specifies the type of dispersion measure to use, either `'range'` or `'std_dev'`, for control limit calculations. Default is `'range'`.
  - `**kwargs`: Additional keyword arguments not explicitly handled in this method.

- **Raises**
  - `TypeError`: If the provided arguments do not match their expected types.
  - `ValueError`: If `axis` or `dispersion_type` is not one of the expected values.

## Example Usage

The following example demonstrates how to load data from a CSV file, fit it to an XBarChart, and then plot the chart:

```python
import pandas as pd
from spc_toolbox import XBarChart

# Load data from CSV
df = pd.read_csv("data/XBar-RChart.csv")

# Initialize XBarChart
xbarChart = XBarChart()

# Fit data to the chart
xbarChart.fit(index=df.index, values=df, axis=1, dispersion_type="range")

# Plot the chart
xbarChart.plot()
