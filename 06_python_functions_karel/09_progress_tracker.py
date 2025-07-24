# 📊 Progress Tracker Project
# Show progress bar using while loop

import time

def progress_tracker():
    total_steps = 10
    current_step = 0
    
    print("📊 Starting Progress Tracker...")
    
    # Show initial state
    progress_calculation = (current_step / total_steps) * 100
    print(f"[{'-' * total_steps}] {progress_calculation:.0f}% Complete ({current_step}/{total_steps}) items")
    
    while current_step < total_steps:
        current_step += 1
        progress_calculation = (current_step / total_steps) * 100
        
        # Create progress bar
        completed_bars = '#' * current_step
        remaining_bars = '-' * (total_steps - current_step)
        
        print(f"[{completed_bars}{remaining_bars}] {progress_calculation:.0f}% Complete ({current_step}/{total_steps}) items")
        
        # Add realistic delay
        time.sleep(0.5)
    
    print(" Progress complete!")

# Run the progress tracker
progress_tracker()
