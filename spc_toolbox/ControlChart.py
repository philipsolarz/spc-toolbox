import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, List, Dict, Callable, Union, TypeVar, ParamSpec, Concatenate

P = ParamSpec('P')
R = TypeVar('R')

class ControlChart:
    def __init__(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]] = {}):
        """
        Initializes a ControlChart object with a dictionary of rules.

        Parameters:
        - rules (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.
        
        """
        self.rules = rules

    def __and__(self, other):
        """
        Combines two ControlChart objects into a CompositeControlChart object.

        Parameters:
        - other (ControlChart): The other ControlChart object to be combined.

        Returns:
        - A CompositeControlChart object containing both ControlChart objects.

        Raises:
        - ValueError: If the other object is not a ControlChart.
        """
        if isinstance(other, ControlChart):
            return CompositeControlChart([self, other])
        else:
            raise ValueError("Operation '&' is not supported between ControlChart and {}".format(type(other)))

    def add_rule(self, name: str, rule: Callable[Concatenate['ControlChart', P], R]):
        """
        Adds a single rule to the dictionary of rules.

        Parameters:
        - name (str): The name of the rule to be added.
        - rule (Callable): The rule function to be added.

        Returns:
        - The ControlChart object with the rule added to the dictionary of rules.

        Raises:
        - TypeError: If the rule is not callable.
        """
        if not callable(rule):
            raise TypeError("The rule must be callable.")
        self.rules[name] = rule
        return self

    def add_rules(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]]):
        """
        Adds multiple rules to the dictionary of rules.

        Parameters:
        - rules (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

        Returns:
        - The ControlChart object with the rules added to the dictionary of rules.

        Raises:
        - TypeError: If any of the rules are not callable.
        """
        if not all(callable(rule) for rule in rules.values()):
            raise TypeError("All rules must be callable.")
        self.rules.update(rules)
        return self

    def remove_rule(self, name: str):
        """
        Removes a specific rule from the dictionary of rules by name.

        Parameters:
        - name (str): The name of the rule to be removed.

        Returns:
        - The ControlChart object with the rule removed from the dictionary of rules.

        Raises:
        - ValueError: If the rule does not exist.
        """
        if name not in self.rules:
            raise ValueError(f"No rule named '{name}' exists.")
        del self.rules[name]
        return self

    def remove_rules(self, names: List[str]):
        """
        Removes multiple specific rules from the dictionary of rules by their names.

        Parameters:
        - names (List[str]): The names of the rules to be removed.

        Returns:
        - The ControlChart object with the rules removed from the dictionary of rules.

        Raises:
        - ValueError: If any of the rules do not exist.
        """
        if not all(name in self.rules for name in names):
            missing_rules = [name for name in names if name not in self.rules]
            raise ValueError(f"The following rules do not exist: {missing_rules}")
        for name in names:
            del self.rules[name]
        return self

    def clear_rules(self):
        """
        Clears all rules from the dictionary, removing all currently set rules.
        
        Returns:
        - The ControlChart object with all rules removed from the dictionary of rules.
        """
        self.rules.clear()
        return self
    
    def evaluate_rules(self, rules: Dict[str, Callable[Concatenate['ControlChart', P], R]] = None):
        """
        Evaluates the rules in the dictionary of rules. If no rules are provided, the currently set rules are used.

        Parameters:
        - rules (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

        Returns:
        - A dictionary with rule names as keys and rule evaluation results as values.

        Raises:
        - ValueError: If no rules are provided and no rules have been set.
        """
        if rules is None and self.rules is None:
            raise ValueError("No rules have been set.")
        
        if rules is None:
            rules = self.rules

        results = {}

        for name, rule in rules.items():
            results[name] = rule(self)
        return results

    def fit(self,
            x: pd.Series,
            y: pd.Series,
            lower_control_limit: Union[pd.Series, float],
            center_line: Union[pd.Series, float],
            upper_control_limit: Union[pd.Series, float]
        ):
        """
        Fits the data to the ControlChart object.

        Parameters:
        - x (pd.Series): The x data.
        - y (pd.Series): The y data.
        - lower_control_limit (Union[pd.Series, float]): The lower control limit.
        - center_line (Union[pd.Series, float]): The center line.
        - upper_control_limit (Union[pd.Series, float]): The upper control limit.

        Returns:
        - The ControlChart object with the data fitted.

        Raises:
        - TypeError: If the x data is not a Series.
        - TypeError: If the y data is not a Series.
        - TypeError: If the lower control limit is not a Series or a float.
        - TypeError: If the center line is not a Series or a float.
        - TypeError: If the upper control limit is not a Series or a float.
        - ValueError: If the lengths of x and y do not match.
        - ValueError: If the length of lower_control_limit does not match the length of x.
        - ValueError: If the length of center_line does not match the length of x.
        - ValueError: If the length of upper_control_limit does not match the length of x.
        """
        if not isinstance(x, pd.Series):
            raise TypeError("The x data must be a Series.")
        
        if not isinstance(y, pd.Series):
            raise TypeError("The y data must be a Series.")
        
        if not isinstance(lower_control_limit, pd.Series) and not isinstance(lower_control_limit, float):
            raise TypeError("The lower control limit must be a Series or a float.")
        
        if not isinstance(center_line, pd.Series) and not isinstance(center_line, float):
            raise TypeError("The center line must be a Series or a float.")
        
        if not isinstance(upper_control_limit, pd.Series) and not isinstance(upper_control_limit, float):
            raise TypeError("The upper control limit must be a Series or a float.")

        if not len(x) == len(y):
            raise ValueError("The lengths of x and y must match.")

        if isinstance(lower_control_limit, pd.Series) and not len(lower_control_limit) == len(x):
            raise ValueError("The length of lower_control_limit must match the length of x.")

        if isinstance(center_line, pd.Series) and not len(center_line) == len(x):
            raise ValueError("The length of center_line must match the length of x.")

        if isinstance(upper_control_limit, pd.Series) and not len(upper_control_limit) == len(x):
            raise ValueError("The length of upper_control_limit must match the length of x.")

        self.x = x
        self.y = y

        if isinstance(lower_control_limit, pd.Series):
            self.lower_control_limit = lower_control_limit
        else:
            self.lower_control_limit = pd.Series([lower_control_limit] * len(x), index=x.index)

        if isinstance(center_line, pd.Series):
            self.center_line = center_line
        else:
            self.center_line = pd.Series([center_line] * len(x), index=x.index)

        if isinstance(upper_control_limit, pd.Series):
            self.upper_control_limit = upper_control_limit
        else:
            self.upper_control_limit = pd.Series([upper_control_limit] * len(x), index=x.index)


        self.center_line.name = "CL"
        self.upper_control_limit.name = "UCL"
        self.lower_control_limit.name = "LCL"
        self.df = pd.concat([self.x, self.y, self.lower_control_limit, self.center_line, self.upper_control_limit], axis=1)
        return self

    def plot(self, fig: Optional[plt.Figure] = None, ax: Optional[plt.Axes] = None):
        """
        Plots the ControlChart object.
        
        Parameters:
        - fig (Optional[plt.Figure]): The figure to plot the chart on.
        - ax (Optional[plt.Axes]): The axes to plot the chart on.
        
        Raises:
        - ValueError: If the data has not been set.
        - ValueError: If the center line has not been set.
        - ValueError: If the upper control limit has not been set.
        - ValueError: If the lower control limit has not been set.
        - TypeError: If the figure is not a Figure object.
        - TypeError: If the axes is not an Axes object.
        """
        if self.df is None:
            raise ValueError("The data has not been set.")
        
        if self.center_line is None:
            raise ValueError("The center line has not been set.")
        
        if self.upper_control_limit is None:
            raise ValueError("The upper control limit has not been set.")
        
        if self.lower_control_limit is None:
            raise ValueError("The lower control limit has not been set.")
        
        if fig is not None and not isinstance(fig, plt.Figure):
            raise TypeError("The figure must be a Figure object.")
        
        if ax is not None and not isinstance(ax, plt.Axes):
            raise TypeError("The axes must be an Axes object.")
        
        if fig is None and ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))

        ax.set_title(f"{self.__class__.__name__}")
        ax.set_xlabel(self.x.name)
        ax.set_ylabel(self.y.name)
        ax.plot(self.x, self.upper_control_limit, 'r--', label='UCL')
        ax.plot(self.x, self.center_line, color='green', linestyle='-', label='CL')
        ax.plot(self.x, self.lower_control_limit, 'r--', label='LCL')
        ax.plot(self.x, self.y, marker='o', linestyle='-')

class CompositeControlChart:
    def __init__(self, charts: List[ControlChart]):
        """
        Initializes a CompositeControlChart object with a list of ControlChart objects.
        
        Parameters:
        - charts (List[ControlChart]): A list of ControlChart objects to be combined into a composite chart.
        """
        self.charts = charts

    def add_rule(self, name: str, rule: Callable[Concatenate[ControlChart, P], R]):
        """
        Adds a single rule to the dictionary of rules for each ControlChart object in the list.
        
        Parameters:
        - name (str): The name of the rule to be added.
        - rule (Callable): The rule function to be added.
        
        Returns:
        - The CompositeControlChart object with the rule added to the dictionary of rules for each ControlChart object.
        """
        for chart in self.charts:
            chart.add_rule(name, rule)
        return self
    
    def add_rules(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]]):
        """
        Adds multiple rules to the dictionary of rules for each ControlChart object in the list.

        Parameters:
        - rules (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.

        Returns:
        - The CompositeControlChart object with the rules added to the dictionary of rules for each ControlChart object.
        """
        for chart in self.charts:
            chart.add_rules(rules)
        return self
    
    def remove_rule(self, name: str):
        """
        Removes a specific rule from the dictionary of rules for each ControlChart object in the list.

        Parameters:
        - name (str): The name of the rule to be removed.

        Returns:
        - The CompositeControlChart object with the rule removed from the dictionary of rules for each ControlChart object.
        """
        for chart in self.charts:
            chart.remove_rule(name)
        return self
    
    def remove_rules(self, names: List[str]):
        """
        Removes multiple specific rules from the dictionary of rules for each ControlChart object in the list.
        
        Parameters:
        - names (List[str]): The names of the rules to be removed.
        
        Returns:
        - The CompositeControlChart object with the rules removed from the dictionary of rules for each ControlChart object.
        """
        for chart in self.charts:
            chart.remove_rules(names)
        return self
    
    def clear_rules(self):
        """
        Clears all rules from the dictionary for each ControlChart object in the list.
        
        Returns:
        - The CompositeControlChart object with all rules removed from the dictionary of rules for each ControlChart object.
        """
        for chart in self.charts:
            chart.clear_rules()
        return self
    
    def evaluate_rules(self, rules: Dict[str, Callable[Concatenate[ControlChart, P], R]] = None):
        """
        Evaluates the rules in the dictionary of rules for each ControlChart object in the list. If no rules are provided, the currently set rules are used.
        
        Parameters:
        - rules (Dict[str, Callable]): A dictionary with rule names as keys and rule functions as values.
        
        Returns:
        - A dictionary with rule names as keys and rule evaluation results as values for each ControlChart object in the list.
        """
        results = {}

        for chart in self.charts:
            results[chart.__class__.__name__] = chart.evaluate_rules(rules)
        return results

    def fit(self, **kwargs):
        """
        Fits the data for each ControlChart object in the list.
        
        Parameters:
        - kwargs: Keyword arguments to be passed to the fit method of each ControlChart object.
        
        Returns:
        - The CompositeControlChart object with the data fitted for each ControlChart object in the list.
        """
        for chart in self.charts:
            chart.fit(**kwargs)
        return self

    def plot(self):
        """
        Plots the CompositeControlChart object.
        """
        fig, axs = plt.subplots(1, len(self.charts), figsize=(len(self.charts) * 10, 6))
        for chart, ax in zip(self.charts, axs):
            chart.plot(fig, ax)