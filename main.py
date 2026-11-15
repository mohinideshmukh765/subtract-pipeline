import csv
import os
from fastapi import FastAPI
from subtract import subtract

app = FastAPI(title="Subtraction API")
LOG_FILE = "requests_log.csv"


def log_request(a, b, result):
    new_file = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["a", "b", "result"])
        writer.writerow([a, b, result])


@app.get("/")
def home():
    return {"message": "Subtraction API is running"}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract(a, b)
    log_request(a, b, result)
    return {"a": a, "b": b, "result": result}