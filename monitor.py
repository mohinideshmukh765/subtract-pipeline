import os
import numpy as np
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

rng = np.random.default_rng(42)

# Reference data: what the model/API normally sees
reference = pd.DataFrame({"a": rng.integers(0, 100, 200),
                          "b": rng.integers(0, 100, 200)})
reference["result"] = reference["a"] - reference["b"]

# Current data: real requests logged by the API (falls back to simulated data)
if os.path.exists("requests_log.csv") and len(pd.read_csv("requests_log.csv")) >= 5:
    current = pd.read_csv("requests_log.csv")
else:
    current = pd.DataFrame({"a": rng.integers(50, 200, 200),
                            "b": rng.integers(0, 50, 200)})
    current["result"] = current["a"] - current["b"]

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html("evidently_report.html")
print("Report saved: evidently_report.html")