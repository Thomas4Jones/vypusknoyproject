import subprocess
import os
import pytest


@pytest.fixture
def report_dir():
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)
    return report_dir


def test_locust(report_dir):
    locust_process = subprocess.Popen(
        ["locust", "-f", "locustfile.py", "--headless", "--run-time", "1m", "--users", "100", "--spawn-rate", "10",
         "--html", f"{report_dir}/locust_report.html"])
    locust_process.wait()
    assert locust_process.returncode == 0, "Процесс завершился"
    report_file = f"{report_dir}/locust_report.html"
    assert os.path.exists(report_file), "Отчет не создан"
    with open(report_file, 'r') as f:
        first_line = f.readline().strip()
        assert first_line == "<!DOCTYPE html>", "Отчет не корректный"
