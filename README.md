
# Statistical Process Control Toolbox Documentation

Welcome to the Statistical Process Control (SPC) Toolbox Documentation. This toolbox provides a comprehensive set of tools for monitoring and analyzing manufacturing processes. The toolbox is designed to help quality assurance professionals and engineers to maintain high standards of quality by identifying variations in processes using various SPC charts.

## Installation

To install the SPC Toolbox, use the following command:

```bash
pip install spc-toolbox
```

## Quick Start

Here's a quick example of how to use the XBarChart class to monitor process means:

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
```

This example demonstrates how to create an `XBarChart` object, fit it with sample data, and plot the control chart to visualize the process means.

##  Control Charts

The SPC Toolbox provides several types of control charts, each designed to monitor different aspects of a manufacturing process. Here are the main control charts available in the toolbox:

- [XBarChart](docs/XBarChart.md): Monitors the average of subgroup means in a process.
- [RChart](docs/RChart.md): Tracks the range of values within subgroups to assess process variability.
- [SChart](docs/SChart.md): Monitors the standard deviation of subgroups to evaluate process dispersion.
- [UChart](docs/UChart.md): Tracks the number of defects per unit of output to assess process quality.
- [PChart](docs/PChart.md): Monitors the proportion of defective items in a sample to evaluate process quality.
- [IChart](docs/IChart.md): Tracks the number of defects per unit of output in a Poisson process.
- [MRChart](docs/MRChart.md): Monitors the moving range of consecutive observations to assess process variability.

Each control chart class provides methods for fitting data, plotting the control chart, and accessing statistical parameters.

## Contributing

If you would like to contribute to the SPC Toolbox, please read our [contributing guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

The SPC Toolbox is released under the [MIT License](LICENSE).
