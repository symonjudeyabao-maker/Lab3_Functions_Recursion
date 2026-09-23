# diagnostic.py
import math

# Student Identity Configuration parameters
LAST_NAME = "YABAO"
SEED_NUM = 8
FAVORITE_ARTIST = "ARTHUR NERY"

# 4. Decorator to record the diagnostic process
def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Initiating execution of: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] Completed execution of: {func.__name__}\n")
        return result
    return wrapper

# 1. Generate student-specific equipment readings
def generate_readings():
    # Deterministic generation using string metrics to prevent random flukes
    base_calc = (len(LAST_NAME) * len(FAVORITE_ARTIST)) + (SEED_NUM * 12)
    
    # Intentionally inserting an invalid string entry to satisfy the requirement
    # "Invalid entries must be handled without terminating the program"
    readings = [base_calc, base_calc - 40, "INVALID_SIGNAL", base_calc + 25]
    return readings

# 2. Separate validation function
def validate_reading(val):
    if not isinstance(val, (int, float)):
        raise TypeError("Non-numeric sensor reading detected.")
    if val <= 0:
        raise ValueError("Critical zero or negative voltage bounds breached.")
    return True

# 2. Separate calculation and classification function
def classify_reading(val):
    if val > 120:
        return "CRITICAL OVERLOAD"
    elif val >= 85:
        return "OPTIMAL OPERATION"
    else:
        return "LOW VOLTAGE WARNING"

# Main diagnostic manager engine
@diagnostic_logger
def run_system_diagnostic():
    print(f"=== INITIALIZING MONITORING PLATFORM: {LAST_NAME} ===")
    print(f"System Seed Core: {SEED_NUM} | Calibration Target: {FAVORITE_ARTIST}\n")
    
    sensor_data = generate_readings()
    processed_results = []
    
    # 3. Handle invalid input using appropriate exception handling
    for idx, reading in enumerate(sensor_data, start=1):
        print(f"Analyzing Sensor Channel Row {idx}: Raw Input = {reading}")
        try:
            validate_reading(reading)
            condition = classify_reading(reading)
            processed_results.append((reading, condition))
            print(f"-> Validation: PASSED | Condition Evaluation: {condition}")
        except (TypeError, ValueError) as err:
            processed_results.append((reading, f"MALFUNCTION ERROR: {err}"))
            print(f"-> Validation: FAILED | Error Action Logged: {err}")
            
    # 5. Display a summary based on the processed data
    print("\n" + "="*50)
    print("           DIAGNOSTIC EXECUTIVE SUMMARY           ")
    print("="*50)
    for idx, (val, status) in enumerate(processed_results, start=1):
        print(f"Channel #{idx} Data: [{val}] -> Diagnostic Node Status: {status}")
    print("="*50)

if __name__ == "__main__":
    run_system_diagnostic()