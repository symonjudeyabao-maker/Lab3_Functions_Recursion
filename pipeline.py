# pipeline.py
import math

LAST_NAME = "YABAO"
SEED_NUM = 8
FAVORITE_ARTIST = "ARTHUR NERY"

def monitor_pipeline(func):
    def wrapper(*args, **kwargs):
        print("[PIPELINE START] Beginning telemetry processing sequence.")
        res = func(*args, **kwargs)
        print("[PIPELINE END] Telemetry stream fully processed.")
        return res
    return wrapper

def telemetry_generator():
    base_signal = (len(LAST_NAME) * 10) + len(FAVORITE_ARTIST)
    raw_data = [base_signal, base_signal * 2, "BAD_STREAM_SIGNAL", -15, base_signal + 10]
    for reading in raw_data:
        yield reading

def recursive_anomaly_cooldown(val, step=1):
    if val <= 75:
        return f"Stabilized after {step} cycles"
    return recursive_anomaly_cooldown(val - 15, step + 1)

@monitor_pipeline
def process_system_telemetry():
    print(f"Loading Modules for: {LAST_NAME} | Calibration Seed: {SEED_NUM}")
    
    valid_count = 0
    invalid_count = 0
    abnormal_count = 0
    total_processed = 0
    summary_report = []
    
    scale_signal = lambda x: x + SEED_NUM

    for raw_val in telemetry_generator():
        total_processed += 1
        print(f"\nProcessing Telemetry Frame #{total_processed}: Input = {raw_val}")
        
        try:
            if not isinstance(raw_val, (int, float)):
                raise TypeError("Non-numeric artifact present in stream.")
            if raw_val < 0:
                raise ValueError("Negative bounds breach detected.")
            
            valid_count += 1
            transformed = scale_signal(raw_val)
            
            if transformed > 100:
                abnormal_count += 1
                recursive_trace = recursive_anomaly_cooldown(transformed)
                status = f"ABNORMAL (Trace: {recursive_trace})"
            else:
                status = "NORMAL OPERATION"
                
            summary_report.append((raw_val, f"VALID -> {status}"))
            print(f"Status Evaluation: {status}")
            
        except (TypeError, ValueError) as err:
            invalid_count += 1
            summary_report.append((raw_val, f"INVALID -> Error: {err}"))
            print(f"Status Evaluation: FAILED | {err}")

    print("\n" + "="*55)
    print("                 SYSTEM METRICS BREAKDOWN                 ")
    print("="*55)
    print(f"Total Streams Sampled: {total_processed}")
    print(f"Valid Telemetry Nodes: {valid_count}")
    print(f"Invalid Stream Faults: {invalid_count}")
    print(f"Abnormal Spikes Traced: {abnormal_count}")
    print(f"Overall Equipment Status: {'ATTENTION REQUIRED' if abnormal_count > 0 else 'HEALTHY'}")
    print("="*55)
    
    return summary_report

if __name__ == "__main__":
    process_system_telemetry()