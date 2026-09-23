# fault_trace.py
LAST_NAME = "YABAO"
SEED_NUM = 8
FAVORITE_ARTIST = "ARTHUR NERY"

# Counter to keep track of recursive execution layers
recursive_count = 0
trace_log = []

def recursive_fault_trace(fault_code):
    global recursive_count
    recursive_count += 1
    
    # Log the current trace state
    trace_log.append(fault_code)
    
    # 3. Base condition definition
    if fault_code <= 10:
        return f"Fault successfully isolated at final index block: {fault_code}"
    
    # 2. Recursive function step execution down the stack
    next_fault_code = math.floor(fault_code / 2) + SEED_NUM
    
    # Safety breakout to avoid infinite recursion flukes
    if next_fault_code >= fault_code:
        return f"Fault trace stabilization reached at: {fault_code}"
        
    return recursive_fault_trace(next_fault_code)

if __name__ == "__main__":
    import math
    # 1. Generate unique baseline student fault code value
    initial_code = (len(LAST_NAME) + len(FAVORITE_ARTIST)) * SEED_NUM
    
    print("--- STARTING RECURSIVE FAULT DECOMPOSITION ---")
    final_status = recursive_fault_trace(initial_code)
    
    print(f"Generated Fault Data: {initial_code}")
    print(f"Recursive Trace Path: {trace_log}")
    print(f"Number of Recursive Calls: {recursive_count}")
    print(f"Final Outcome Report: {final_status}\n")