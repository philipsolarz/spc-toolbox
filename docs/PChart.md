# PChart Class Documentation

The `PChart` class is derived from the `ControlChart` class within the `spc_toolbox` package. It is specifically designed for creating and managing a Proportion Chart (P-Chart), which is widely used in statistical process control (SPC) to monitor the proportion of defective items in a process.

## Class Definition

### `__init__(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = {})`

Initializes a `PChart` object with an optional set of rules.

- **Parameters**
  - `rules`: A dictionary where keys are rule names and values are callable functions defining the rule's logic. Defaults to an empty dictionary.

### `fit(self, index: Union[pd.Series, pd.Index], defective_items: pd.Series, total_items: Union[pd.Series, int], z: float = 3.0, **kwargs)`

Fits the data to the P-Chart, calculating the necessary control limits and the center line based on the proportion of defects.

- **Parameters**
  - `index`: The index (e.g., sample number) for the data points. Can be a `pandas.Series` or `pandas.Index`.
  - `defective_items`: A `pandas.Series` containing the number of defective items for each sample.
  - `total_items`: The total number of items inspected per sample, which can be a constant integer (if the sample size is constant) or a `pandas.Series` (if the sample size varies).
  - `z`: The number of standard deviations from the mean to set the control limits, often referred to as the Z-score. Defaults to 3.0.
  - `**kwargs`: Additional keyword arguments not explicitly handled in this method.

- **Raises**
  - `TypeError`: If the provided arguments do not match their expected types.

## Example Usage

The following example demonstrates how to load data from a CSV file, fit it to a P-Chart, and then plot the chart:

```python
import pandas as pd
from spc_toolbox import PChart

# Load data from CSV
df = pd.read_csv("data/PChart.csv")

# Initialize PChart
pChart = PChart()

# Fit data to the chart
pChart.fit(index=df["Sample_Number"], defective_items=df["Defective_Items"], total_items=df["Total_Items"], z=3.0)

# Plot the chart
pChart.plot()
```