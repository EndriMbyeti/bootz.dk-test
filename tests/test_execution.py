import os
import sys
import webbrowser
import pytest

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def run_tests():
    # Define the report directory relative to the current file's location
    report_dir = os.path.join(os.path.dirname(__file__), '..', 'test_report')
    os.makedirs(report_dir, exist_ok=True)  # Create directory if it doesn't exist
    report_path = os.path.join(report_dir, "report.html")

    # Define the paths to test files relative to the current file
    test_files = [
        os.path.join(os.path.dirname(__file__), "test_1.py"),
        os.path.join(os.path.dirname(__file__), "test_2.py"),
        os.path.join(os.path.dirname(__file__), "test_3.py"),
    ]

    # Run pytest with options to include the HTML report
    pytest_args = test_files + [
        f"--html={report_path}",  # generate the HTML report
        "--self-contained-html"  # embed CSS and JavaScript for standalone viewing
    ]
    pytest.main(pytest_args)

    # Open the report in the default web browser after execution
    if os.path.exists(report_path):
        webbrowser.open(f"file://{os.path.abspath(report_path)}")


if __name__ == "__main__":
    run_tests()
