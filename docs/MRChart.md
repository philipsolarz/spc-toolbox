# MRChart Class Documentation

The `MRChart` class extends the `ControlChart` class from the `spc_toolbox` package. It is designed to create and manage a Moving Range (MR) Chart, a tool commonly used in statistical process control for monitoring the variability of a process based on the moving range of the data.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes an `MRChart` object.

- **Parameters**
  - `rules`: A dictionary of rules where keys are rule names and values are callable functions that define the rule logic. The default is an empty dictionary.

### `fit(self, index: Union[pd.Series, pd.Index], values: pd.Series, n: int = 2, **kwargs)`

Fits the data to the MRChart, calculating the necessary control limits and the center line.

- **Parameters**
  - `index`: The index (datetime or otherwise) of the data points. Must be a `pandas.Series` or `pandas.Index`.
  - `values`: The measured values to be plotted and analyzed. Must be a `pandas.Series`.
  - `n`: The subgroup size used for calculating the moving range. Default is 2.
  - `**kwargs`: Additional keyword arguments not specifically handled in this method.

- **Raises**
  - `TypeError`: If `index` is not a `pandas.Series` or `pandas.Index`, or if `values` is not a `pandas.Series`.
  - `ValueError`: If `n` is not an integer or if `n` is less than 1.

## Example Usage

This example demonstrates how to use the `MRChart` class to fit data from a CSV file and plot the MRChart.

```python
import pandas as pd
from spc_toolbox import MRChart

# Load data
df = pd.read_csv("data/I-MRChart.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Initialize MRChart
mrChart = MRChart()

# Fit data to the chart
mrChart.fit(index=df["Date"], values=df["Measurement"], n=2)

# Plot the chart
mrChart.plot()
```