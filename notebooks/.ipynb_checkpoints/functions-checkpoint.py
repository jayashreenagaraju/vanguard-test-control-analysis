def print_in_red(data):
    # ANSI escape code for red color
    red_color = "\033[91m"
    # ANSI escape code to reset color
    reset_color = "\033[0m"

    print(red_color + data + reset_color)


 # Calculate the completion rate
    def calculate_completion_rate(df):
        unique_visits = df['visit_id'].nunique()
        confirm_visits = df[df['process_step'] == 'confirm']['visit_id'].nunique()
        completion_rate = confirm_visits / unique_visits
        return completion_rate


 # Calculate the average duration spent on each step
    def calculate_average_time_per_step(df):
        # Sort the DataFrame by visitor_id, visit_id, and date_time
        df = df.sort_values(by=['visitor_id', 'visit_id', 'date_time'])
        
        # Calculate the time difference between consecutive steps for each visit_id
        df['time_diff'] = df.groupby(['visitor_id', 'visit_id'])['date_time'].diff()
        
        # Filter out rows where time_diff is NaT (i.e., the first step of each visit)
        df_filtered = df.dropna(subset=['time_diff'])
        
        # Calculate the average duration spent on each step
        average_time_per_step = df_filtered.groupby('process_step')['time_diff'].mean()
        return average_time_per_step   

