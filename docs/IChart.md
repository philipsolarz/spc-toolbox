# IChart Class Documentation

The `IChart` class extends the functionality of the `ControlChart` class from the `spc_toolbox` package, focusing on the implementation of an Individual (I) control chart, commonly used in Statistical Process Control (SPC) for monitoring process variations.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes an `IChart` object.

- **Parameters**
  - `rules`: A dictionary of rules where keys are rule names and values are callable functions that define the rule logic.

### `fit(self, index: Union[pd.Series, pd.Index], values: pd.Series, n: int = 2, **kwargs)`

Fits the data to the IChart, calculating the necessary control limits and the center line.

- **Parameters**
  - `index`: The index (datetime or otherwise) of the data points. Must be a `pandas.Series` or `pandas.Index`.
  - `values`: The measured values to be plotted and analyzed. Must be a `pandas.Series`.
  - `n`: The subgroup size used for calculating the moving range. Default is 2.
  - `**kwargs`: Additional keyword arguments.

- **Raises**
  - `TypeError`: If `index` is not a `pandas.Series` or `pandas.Index`, if `values` is not a `pandas.Series`, or if `n` is not an integer.
  - `ValueError`: If `n` is less than 1.

## Example Usage

This example demonstrates how to use the `IChart` class to fit data from a CSV file and plot the IChart.

```python
import pandas as pd
from spc_toolbox import IChart

# Load data
df = pd.read_csv("data/I-MRChart.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Initialize IChart
iChart = IChart()

# Fit data to the chart
iChart.fit(index=df["Date"], values=df["Measurement"], n=2)

# Plot the chart
iChart.plot()
```