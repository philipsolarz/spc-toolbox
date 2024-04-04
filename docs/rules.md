# Setting Up and Evaluating Rules for ControlCharts

In statistical process control (SPC), rules are employed to detect out-of-control conditions within a process. These rules, when applied to ControlCharts, enable the identification of specific patterns or anomalies that suggest a need for process adjustment or investigation.

## Defining Rules

The `ControlChart` class allows you to define custom rules for monitoring process variations. These rules are defined as callable functions that take the chart instance and the data as input and return some indication whether the data in the chart is within control or not.

Here's an example of defining a rule for the `XBarChart` class:

```python
import pandas as pd
from spc_toolbox import XBarChart

# Load data from CSV
df = pd.read_csv("data/XBar-RChart.csv")

# Initialize XBarChart
xbarChart = XBarChart()

# Fit data to the chart
xbarChart.fit(index=df.index, values=df, axis=1, dispersion_type="range")

# Define a custom rule function
def custom_rule(chart):
    # Check if the data is within control
    within_limits = (chart.lower_control_limit < chart.y) & (chart.y < chart.upper_control_limit)
    return within_limits.all()

# Evaluate the custom rule
results = xbarChart.evaluate_rules(rules={"custom_rule": custom_rule})
```

In this example, the `custom_rule` function checks if the data in the `XBarChart` instance is within control limits. The `evaluate_rules` method is then used to apply this rule to the chart and return the results.
