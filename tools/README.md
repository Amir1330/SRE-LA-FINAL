# SRE Custom Tools

This directory contains custom tools developed for Site Reliability Engineering tasks.

## Capacity Planner

The `capacity_planner.py` tool is designed to help predict future resource needs based on historical usage patterns captured in Prometheus metrics.

### Features

- Linear regression-based forecasting
- Confidence interval calculation
- Integration with Prometheus metrics
- Visual graphs of predictions
- Detailed reports in JSON format

### Usage

```bash
# Install required dependencies
pip install requests numpy scipy matplotlib

# Basic usage
python capacity_planner.py --prometheus http://localhost:9090

# Advanced usage with custom settings
python capacity_planner.py --prometheus http://localhost:9090 --range 14d --step 2h --output custom_report.json
```

### Parameters

- `--prometheus`: Prometheus server URL (required)
- `--range`: Time range to analyze (default: 7d)
- `--step`: Step size for data points (default: 1h)
- `--output`: Output file for the report (default: capacity_report.json)

### Output

The tool produces:
1. A JSON report with predictions
2. A PNG image with visualizations
3. A summary printed to the console

### Example Use Cases

1. Forecasting server capacity needs for the next 30 days
2. Planning infrastructure scaling ahead of expected traffic increases
3. Determining when to provision new resources based on growth trends

## Adding New Tools

When adding new SRE tools to this directory, please:

1. Create a dedicated Python file with proper docstrings
2. Update this README with details about the tool
3. Include usage examples
4. Add proper error handling and logging
5. Ensure dependencies are documented 