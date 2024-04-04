# UChart Class Documentation

The `UChart` class extends the `ControlChart` class from the `spc_toolbox` package. It is designed to create and manage U-Charts, which are utilized in statistical process control (SPC) to monitor the number of defects per unit across samples or groups.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes a `UChart` object with an optional set of rules for statistical process control.

- **Parameters**
  - `rules`: A dictionary where keys are rule names and values are callable functions that define the rule's logic. Defaults to an empty dictionary.

### `fit(self, index: Union[pd.Series, pd.Index], defects: pd.Series, sample_sizes: Union[pd.Series, int], z: float = 3.0, **kwargs)`

Fits the data to the U-Chart, calculating the control limits and center line based on the defects per unit.

- **Parameters**
  - `index`: The index (e.g., time, batch number) for the data points. Can be a `pandas.Series` or `pandas.Index`.
  - `defects`: A `pandas.Series` containing the number of defects for each sample.
  - `sample_sizes`: The total number of units inspected per sample, which can be a constant integer (if the sample size is constant) or a `pandas.Series` (if the sample size varies).
  - `z`: The number of standard deviations from the mean to set the control limits. Defaults to 3.0.
  - `**kwargs`: Additional keyword arguments not explicitly handled in this method.

- **Raises**
  - `TypeError`: If the provided arguments do not match their expected types.

## Example Usage

The following example demonstrates how to load data from a CSV file, fit it to a U-Chart, and then plot the chart:

```python
import pandas as pd
from spc_toolbox import UChart

# Load data from CSV
df = pd.read_csv("data/UChart.csv")

# Initialize UChart
uChart = UChart()

# Fit data to the chart
uChart.fit(index=df["Unit"], defects=df["Defects"], sample_sizes=df["SampleSize"], z=3.0)

# Plot the chart
uChart.plot()
```