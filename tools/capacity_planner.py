#!/usr/bin/env python3
"""
SRE Capacity Planning Tool
--------------------------
This tool helps predict required resources based on current usage and growth patterns.
It analyzes Prometheus metrics to predict future resource needs.
"""

import argparse
import datetime
import json
import sys
import time
import requests
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class CapacityPlanner:
    def __init__(self, prometheus_url, time_range='7d', step='1h'):
        self.prometheus_url = prometheus_url
        self.time_range = time_range
        self.step = step
        
    def query_prometheus(self, query):
        """Query Prometheus for metrics"""
        end_time = int(time.time())
        
        # Convert time range to seconds
        time_unit = self.time_range[-1]
        time_value = int(self.time_range[:-1])
        
        if time_unit == 'd':
            seconds = time_value * 24 * 60 * 60
        elif time_unit == 'h':
            seconds = time_value * 60 * 60
        else:
            seconds = time_value * 60
        
        start_time = end_time - seconds
        
        url = f"{self.prometheus_url}/api/v1/query_range"
        params = {
            'query': query,
            'start': start_time,
            'end': end_time,
            'step': self.step
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error querying Prometheus: {response.text}")
            return None
        
        result = response.json()
        
        if result['status'] != 'success' or not result['data']['result']:
            print(f"No data returned for query: {query}")
            return None
        
        return result['data']['result']
    
    def predict_resource_needs(self, resource_query, prediction_days=30, confidence=0.95):
        """Predict future resource needs based on current usage patterns"""
        data = self.query_prometheus(resource_query)
        
        if not data:
            return None
        
        # Extract time series data
        times = []
        values = []
        
        for point in data[0]['values']:
            times.append(point[0])
            values.append(float(point[1]))
        
        times = np.array(times)
        values = np.array(values)
        
        # Perform linear regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(times, values)
        
        # Calculate prediction
        last_time = times[-1]
        prediction_time = last_time + (prediction_days * 24 * 60 * 60)
        prediction_range = np.linspace(last_time, prediction_time, 100)
        
        prediction = intercept + slope * prediction_range
        
        # Calculate confidence intervals
        n = len(times)
        mean_x = np.mean(times)
        ss_x = np.sum((times - mean_x) ** 2)
        
        confs = std_err * stats.t.ppf((1 + confidence) / 2., n - 2)
        pred_error = confs * np.sqrt(1 + 1/n + (prediction_range - mean_x) ** 2 / ss_x)
        
        upper_bound = prediction + pred_error
        lower_bound = prediction - pred_error
        
        # Return results
        result = {
            'current_value': values[-1],
            'predicted_value': float(prediction[-1]),
            'lower_bound': float(lower_bound[-1]),
            'upper_bound': float(upper_bound[-1]),
            'growth_rate': slope * (24 * 60 * 60),  # Daily growth rate
            'r_squared': r_value ** 2
        }
        
        return result
    
    def generate_report(self, metrics):
        """Generate a capacity planning report for multiple metrics"""
        report = {
            'generated_at': datetime.datetime.now().isoformat(),
            'prediction_metrics': {}
        }
        
        # Plot setup
        plt.figure(figsize=(12, 8))
        
        for name, query in metrics.items():
            print(f"Analyzing {name}...")
            prediction = self.predict_resource_needs(query)
            
            if prediction:
                report['prediction_metrics'][name] = prediction
                
                # Create subplot for this metric
                plt.subplot(len(metrics), 1, list(metrics.keys()).index(name) + 1)
                plt.title(f"{name} - Current: {prediction['current_value']:.2f}, Predicted: {prediction['predicted_value']:.2f}")
                
                # Query data again to plot
                data = self.query_prometheus(query)
                if data:
                    times = [point[0] for point in data[0]['values']]
                    values = [float(point[1]) for point in data[0]['values']]
                    
                    # Convert timestamps to dates for plotting
                    dates = [datetime.datetime.fromtimestamp(t) for t in times]
                    
                    # Plot historical data
                    plt.plot(dates, values, 'b-', label='Historical')
                    
                    # Generate future dates
                    last_time = times[-1]
                    future_times = np.linspace(last_time, last_time + (30 * 24 * 60 * 60), 30)
                    future_dates = [datetime.datetime.fromtimestamp(t) for t in future_times]
                    
                    # Calculate predicted values
                    slope, intercept, _, _, _ = stats.linregress(times, values)
                    future_values = intercept + slope * future_times
                    
                    # Plot prediction
                    plt.plot(future_dates, future_values, 'r--', label='Predicted')
                    plt.legend()
                    plt.grid(True)
            else:
                report['prediction_metrics'][name] = "No data available"
        
        plt.tight_layout()
        plt.savefig('capacity_prediction.png')
        
        return report


def main():
    parser = argparse.ArgumentParser(description='SRE Capacity Planning Tool')
    parser.add_argument('--prometheus', required=True, help='Prometheus server URL')
    parser.add_argument('--range', default='7d', help='Time range to analyze (e.g., 7d, 24h)')
    parser.add_argument('--step', default='1h', help='Step size for data points')
    parser.add_argument('--output', default='capacity_report.json', help='Output file for the report')
    
    args = parser.parse_args()
    
    planner = CapacityPlanner(args.prometheus, args.range, args.step)
    
    # Define metrics to analyze
    metrics = {
        'CPU Usage': 'avg(rate(node_cpu_seconds_total{mode!="idle"}[5m])) by (instance)',
        'Memory Usage': 'avg(node_memory_MemUsed_bytes) by (instance)',
        'Request Rate': 'sum(rate(app_request_count[5m]))',
        'Error Rate': 'sum(rate(app_request_count{http_status="500"}[5m])) / sum(rate(app_request_count[5m]))',
        'Response Time': 'histogram_quantile(0.95, sum(rate(app_request_latency_seconds_bucket[5m])) by (le))'
    }
    
    report = planner.generate_report(metrics)
    
    # Print summary
    print("\nCapacity Planning Report Summary:")
    print("================================")
    
    for metric, data in report['prediction_metrics'].items():
        if isinstance(data, dict):
            print(f"\n{metric}:")
            print(f"  Current value: {data['current_value']:.4f}")
            print(f"  Predicted in 30 days: {data['predicted_value']:.4f}")
            print(f"  95% confidence interval: [{data['lower_bound']:.4f}, {data['upper_bound']:.4f}]")
            print(f"  Daily growth rate: {data['growth_rate']:.4f}")
            print(f"  R² (prediction quality): {data['r_squared']:.4f}")
        else:
            print(f"\n{metric}: {data}")
    
    # Save full report
    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nFull report saved to {args.output}")
    print(f"Prediction chart saved to capacity_prediction.png")


if __name__ == "__main__":
    main() 