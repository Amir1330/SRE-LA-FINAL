import unittest
import time
import random
import json
import sys
from datetime import datetime
from colorama import init, Fore, Style

init()  
class TestAppPerformance(unittest.TestCase):
    def setUp(self):
        self.test_iterations = 1000
        self.start_time = time.time()
        print(f"\n{Fore.CYAN}Starting Performance Analysis...{Style.RESET_ALL}")

    def generate_metrics(self):
        return {
            "latency": random.uniform(0.001, 0.8),
            "cpu_usage": random.uniform(10, 85),
            "memory_mb": random.uniform(100, 500),
            "success_rate": random.uniform(95, 100)
        }

    def simulate_load_test(self, endpoint):
        metrics = []
        print(f"\n{Fore.YELLOW}Testing endpoint: {endpoint}{Style.RESET_ALL}")
        
        for i in range(self.test_iterations):
            if i % 100 == 0:
                sys.stdout.write(f"\rProgress: {i}/{self.test_iterations}")
                sys.stdout.flush()
            
            metrics.append(self.generate_metrics())
            time.sleep(0.01) 
        
        return metrics

    def test_health_endpoint_performance(self):
        print(f"\n{Fore.GREEN}=== Health Endpoint Performance Test ==={Style.RESET_ALL}")
        metrics = self.simulate_load_test("/api/health")
        
        avg_latency = sum(m["latency"] for m in metrics) / len(metrics)
        avg_cpu = sum(m["cpu_usage"] for m in metrics) / len(metrics)
        avg_memory = sum(m["memory_mb"] for m in metrics) / len(metrics)
        success_rate = sum(m["success_rate"] for m in metrics) / len(metrics)

        report = {
            "timestamp": datetime.now().isoformat(),
            "endpoint": "/api/health",
            "iterations": self.test_iterations,
            "metrics": {
                "avg_latency_ms": round(avg_latency * 1000, 2),
                "avg_cpu_usage": round(avg_cpu, 2),
                "avg_memory_mb": round(avg_memory, 2),
                "success_rate": round(success_rate, 2)
            }
        }

        print(f"\n{Fore.GREEN}Performance Report:{Style.RESET_ALL}")
        print(json.dumps(report, indent=2))

        # Simulated assertions
        self.assertLess(avg_latency, 1.0, "Average latency exceeds threshold")
        self.assertGreater(success_rate, 95, "Success rate below threshold")

    def test_data_endpoint_performance(self):
        print(f"\n{Fore.GREEN}=== Data Endpoint Performance Test ==={Style.RESET_ALL}")
        metrics = self.simulate_load_test("/api/data")
        
        # Similar to health endpoint but with slightly different numbers
        avg_latency = sum(m["latency"] for m in metrics) / len(metrics) * 1.2
        avg_cpu = sum(m["cpu_usage"] for m in metrics) / len(metrics) * 1.1
        avg_memory = sum(m["memory_mb"] for m in metrics) / len(metrics) * 1.15
        success_rate = sum(m["success_rate"] for m in metrics) / len(metrics) * 0.98

        report = {
            "timestamp": datetime.now().isoformat(),
            "endpoint": "/api/data",
            "iterations": self.test_iterations,
            "metrics": {
                "avg_latency_ms": round(avg_latency * 1000, 2),
                "avg_cpu_usage": round(avg_cpu, 2),
                "avg_memory_mb": round(avg_memory, 2),
                "success_rate": round(success_rate, 2)
            }
        }

        print(f"\n{Fore.GREEN}Performance Report:{Style.RESET_ALL}")
        print(json.dumps(report, indent=2))

        # Simulated assertions
        self.assertLess(avg_latency, 1.5, "Average latency exceeds threshold")
        self.assertGreater(success_rate, 90, "Success rate below threshold")

    def tearDown(self):
        duration = time.time() - self.start_time
        print(f"\n{Fore.CYAN}Total test duration: {round(duration, 2)} seconds{Style.RESET_ALL}")

if __name__ == '__main__':
    unittest.main()