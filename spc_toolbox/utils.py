import pandas as pd

_chart_constants = {
    "Sample Size": list(range(2, 26)),
    "A2": [1.880, 1.023, 0.729, 0.577, 0.483, 0.419, 0.373, 0.337, 0.308, 0.285, 0.266, 0.249, 0.235, 0.223, 0.212, 0.203, 0.194, 0.187, 0.180, 0.173, 0.167, 0.162, 0.157, 0.153],
    "A3": [2.659, 1.954, 1.628, 1.427, 1.287, 1.182, 1.099, 1.032, 0.975, 0.927, 0.886, 0.850, 0.817, 0.789, 0.763, 0.739, 0.718, 0.698, 0.680, 0.663, 0.647, 0.633, 0.619, 0.606],
    "d2": [1.128, 1.693, 2.059, 2.326, 2.534, 2.704, 2.847, 2.970, 3.078, 3.173, 3.258, 3.336, 3.407, 3.472, 3.532, 3.588, 3.640, 3.689, 3.735, 3.778, 3.819, 3.858, 3.895, 3.931],
    "d3": [0.853, 0.888, 0.880, 0.864, 0.848, 0.833, 0.820, 0.808, 0.797, 0.787, 0.778, 0.770, 0.763, 0.756, 0.750, 0.744, 0.739, 0.734, 0.729, 0.724, 0.720, 0.716, 0.712, 0.708],
    "d4": [0.954, 1.588, 1.978, 2.257, 2.472, 2.645, 2.791, 2.915, 3.024, 3.121, 3.207, 3.285, 3.356, 3.422, 3.482, 3.538, 3.591, 3.640, 3.686, 3.730, 3.771, 3.811, 3.847, 3.883],
    "D3": [0.000, 0.000, 0.000, 0.000, 0.000, 0.076, 0.136, 0.184, 0.223, 0.256, 0.283, 0.307, 0.328, 0.347, 0.363, 0.378, 0.391, 0.403, 0.415, 0.425, 0.434, 0.443, 0.451, 0.459],
    "D4": [3.267, 2.574, 2.282, 2.114, 2.004, 1.924, 1.864, 1.816, 1.777, 1.744, 1.717, 1.693, 1.672, 1.653, 1.637, 1.622, 1.608, 1.597, 1.585, 1.575, 1.566, 1.557, 1.548, 1.541],
    "B3": [0.000, 0.000, 0.000, 0.000, 0.030, 0.118, 0.185, 0.239, 0.284, 0.321, 0.354, 0.382, 0.406, 0.428, 0.448, 0.466, 0.482, 0.497, 0.510, 0.523, 0.534, 0.545, 0.555, 0.565],
    "B4": [3.267, 2.568, 2.266, 2.089, 1.970, 1.882, 1.815, 1.761, 1.716, 1.679, 1.646, 1.618, 1.594, 1.572, 1.552, 1.534, 1.518, 1.503, 1.490, 1.477, 1.466, 1.455, 1.445, 1.435],
}

_chart_constants = pd.DataFrame(_chart_constants)

def get_chart_constant(constant: str, sample_size: int):
    """
    Get the chart constant for a given sample size.
    
    Parameters:
    - constant (str): The chart constant to retrieve.
    - sample_size (int): The sample size to retrieve the chart constant for.
    
    Returns:
    - float: The chart constant for the given sample size.

    Raises:
    - TypeError: If the sample size is not an integer or if the constant is not a string.
    - ValueError: If the sample size is not between 2 and 25 or if the constant is not a valid chart constant.
    """

    if type(sample_size) != int:
        raise TypeError("Sample size must be an integer.")
    
    if type(constant) != str:
        raise TypeError("Constant must be a string.")

    if sample_size < 2 or sample_size > 25:
        raise ValueError("Sample size must be between 2 and 25.")
    
    if constant not in _chart_constants.columns:
        raise ValueError(f"Invalid chart constant '{constant}'.")
    
    chart_constant = _chart_constants.loc[_chart_constants["Sample Size"] == sample_size, constant].values[0]

    return chart_constant