# ControlChart and CompositeControlChart Documentation

## ControlChart Class

### `__init__(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]] = {})`

Initializes a `ControlChart` object with a dictionary of rules.

#### Parameters:
- `rules` (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

### `__and__(self, other)`

Combines two `ControlChart` objects into a `CompositeControlChart` object.

#### Parameters:
- `other` (ControlChart): The other `ControlChart` object to be combined.

#### Returns:
- A `CompositeControlChart` object containing both `ControlChart` objects.

#### Raises:
- `ValueError`: If the other object is not a `ControlChart`.

### `add_rule(self, name: str, rule: Callable[Concatenate['ControlChart', P], R])`

Adds a single rule to the dictionary of rules.

#### Parameters:
- `name` (str): The name of the rule to be added.
- `rule` (Callable): The rule function to be added.

#### Returns:
- The `ControlChart` object with the rule added to the dictionary of rules.

#### Raises:
- `TypeError`: If the rule is not callable.

### `add_rules(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]])`

Adds multiple rules to the dictionary of rules.

#### Parameters:
- `rules` (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

#### Returns:
- The `ControlChart` object with the rules added to the dictionary of rules.

#### Raises:
- `TypeError`: If any of the rules are not callable.

### `remove_rule(self, name: str)`

Removes a specific rule from the dictionary of rules by name.

#### Parameters:
- `name` (str): The name of the rule to be removed.

#### Returns:
- The `ControlChart` object with the rule removed from the dictionary of rules.

#### Raises:
- `ValueError`: If the rule does not exist.

### `remove_rules(self, names: List[str])`

Removes multiple specific rules from the dictionary of rules by their names.

#### Parameters:
- `names` (List[str]): The names of the rules to be removed.

#### Returns:
- The `ControlChart` object with the rules removed from the dictionary of rules.

#### Raises:
- `ValueError`: If any of the rules do not exist.

### `clear_rules(self)`

Clears all rules from the dictionary, removing all currently set rules.

#### Returns:
- The `ControlChart` object with all rules removed from the dictionary of rules.

### `evaluate_rules(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]] = None)`

Evaluates the rules in the dictionary of rules. If no rules are provided, the currently set rules are used.

#### Parameters:
- `rules` (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

#### Returns:
- A dictionary with rule names as keys and rule evaluation results as values.

#### Raises:
- `ValueError`: If no rules are provided and no rules have been set.

### `fit(self, x: pd.Series, y: pd.Series, lower_control_limit: Union[pd.Series, float], center_line: Union[pd.Series, float], upper_control_limit: Union[pd.Series, float])`

Fits the data for the control chart.

### `plot(self, fig: Optional[plt.Figure] = None, ax: Optional[plt.Axes] = None)`

Plots the control chart.

## CompositeControlChart Class

### `__init__(self, charts: List[ControlChart])`

Initializes a `CompositeControlChart` object with a list of `ControlChart` objects.

#### Parameters:
- `charts` (List[ControlChart]): A list of `ControlChart` objects to be combined into a composite chart.

### `add_rule(self, name: str, rule: Callable[Concatenate[ControlChart, P], R])`

Adds a single rule to the dictionary of rules for each `ControlChart` object in the list.

#### Parameters:
- `name` (str): The name of the rule to be added.
- `rule` (Callable): The rule function to be added.

#### Returns:
- The `CompositeControlChart` object with the rule added to the dictionary of rules for each `ControlChart` object.

### `add_rules(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]])`

Adds multiple rules to the dictionary of rules for each `ControlChart` object in the list.

#### Parameters:
- `rules` (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

#### Returns:
- The `CompositeControlChart` object with the rules added to the dictionary of rules for each `ControlChart` object.

### `remove_rule(self, name: str)`

Removes a specific rule from the dictionary of rules for each `ControlChart` object in the list.

#### Parameters:
- `name` (str): The name of the rule to be removed.

#### Returns:
- The `CompositeControlChart` object with the rule removed from the dictionary of rules for each `ControlChart` object.

### `remove_rules(self, names: List[str])`

Removes multiple specific rules from the dictionary of rules for each `ControlChart` object in the list.

#### Parameters:
- `names` (List[str]): The names of the rules to be removed.

#### Returns:
- The `CompositeControlChart` object with the rules removed from the dictionary of rules for each `ControlChart` object.

### `clear_rules(self)`

Clears all rules from the dictionary for each `ControlChart` object in the list.

#### Returns:
- The `CompositeControlChart` object with all rules removed from the dictionary of rules for each `ControlChart` object.

### `evaluate_rules(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = None)`

Evaluates the rules in the dictionary of rules for each `ControlChart` object in the list. If no rules are provided, the currently set rules are used.

#### Parameters:
- `rules` (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

#### Returns:
- A dictionary with rule names as keys and rule evaluation results as values for each `ControlChart` object in the list.

### `fit(self, **kwargs)`

Fits the data for each `ControlChart` object in the list.

#### Parameters:
- `kwargs`: Keyword arguments to be passed to the fit method of each `ControlChart` object.

#### Returns:
- The `CompositeControlChart` object with the data fitted for each `ControlChart` object in the list.

### `plot(self)`

Plots the composite control chart.
