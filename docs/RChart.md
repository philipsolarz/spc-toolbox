# RChart Class Documentation

The `RChart` class extends the `ControlChart` class from the `spc_toolbox` package. It is designed for creating and managing Range Charts (R-Charts), which are used in statistical process control (SPC) for monitoring the variability of a process across subgroups.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes an `RChart` object.

- **Parameters**
  - `rules`: A dictionary of rules where keys are rule names and values are callable functions that define the rule logic. Defaults to an empty dictionary.

### `fit(self, index: Union[pd.Series, pd.Index], values: pd.DataFrame, axis: int = 0, **kwargs)`

Fits the data to the RChart, calculating the necessary control limits and the center line based on the range of the data.

- **Parameters**
  - `index`: The index (e.g., time or batch number) for the data points. Can be a `pandas.Series` or `pandas.Index`.
  - `values`: A `pandas.DataFrame` containing the measured values for each subgroup.
  - `axis`: Determines whether subgroups are defined along rows (`0` or `'index'`) or columns (`1` or `'columns'`). Default is `0`.
  - `**kwargs`: Additional keyword arguments not explicitly handled in this method.

- **Raises**
  - `TypeError`: If the provided arguments do not match their expected types.
  - `ValueError`: If `axis` is not one of the expected values (`0`, `1`, `'index'`, or `'columns'`).

## Example Usage

The following example demonstrates how to load data from a CSV file, fit it to an R-Chart, and then plot the chart:

```python
import pandas as pd
from spc_toolbox import RChart

# Load data from CSV
df = pd.read_csv("data/XBar-RChart.csv")

# Initialize RChart
rChart = RChart()

# Fit data to the chart
rChart.fit(index=df.index, values=df, axis=1)

# Plot the chart
rChart.plot()
```