## DataFilterTool

DataFilterTool is a Python package designed to facilitate filtering and analyzing employee data. It offers functionality to filter employees based on their date of joining and to calculate the average salary for a given designation. This package is suitable for use in various data analysis and human resources applications.

## Features

- Filter employees based on the date of joining.
- Calculate the average salary for a given designation.
- Organize input, output, and log files in separate directories.
- Append timestamps to output and log files for tracking.
- Utilize a configuration file to define the location of log files.

## Installation

You can install DataFilterTool from PyPI using pip:

```bash
pip install DataFilterTool
```

## Usage

### Filtering Employees

To filter employees based on their date of joining, use the `filter_by_date` function. This function takes the date of joining as input and saves the filtered list of employees in a new file in the output directory.

```python
from DataFilterTool.filter_by_date import filter_by_date

# Example usage
date_of_joining = "2022-01-01"
filter_by_date(date_of_joining)
```

### Calculating Average Salary

To calculate the average salary for a given designation, use the `average_salary_by_designation` function. This function takes the designation as input and prints the average salary for that designation in an output file with a timestamp.

```python
from DataFilterTool.avg_sal_by_des import average_salary_by_designation

# Example usage
designation = "Manager"
average_salary_by_designation(designation)
```

### Configuration

You can customize the location of log files by modifying the configuration file (`config.py`). This allows you to specify the path to the log directory relative to the root user.

## File Structure

```
dataFilterTool/
|-- init.py
|-- dataenv/
|-- DataFilterTool/
|   |-- __init__.py
|   |-- filter_by_date.py
|   |-- avg_sal_by_des.py
|   |-- config.py
|   |-- version.py
|
|-- dataFilter_config/
|-- |-- init.py
|-- |-- config.ini
|-- input/
|   |-- employee_data.xlsx 
|-- output/
|   |-- average_salary_output.txt
|   |-- filtered_output_{timestamp}.xlsx
|-- logs/
|   |-- filtered_logs_{timestamp}.txt
|-- tests/
|   |-- test_filter_functions.py
|   |-- test_average_salary_functions.py
|-- scripts/
|   |-- data_generation.py
|-- setup.py
|-- MANIFEST.py
|-- README.md
|-- requirements.txt
```

## Contributing

Contributions to DataFilterTool are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
