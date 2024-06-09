def print_in_red(data):
    # ANSI escape code for red color
    red_color = "\033[91m"
    # ANSI escape code to reset color
    reset_color = "\033[0m"

    print(red_color + data + reset_color)


def get_gender_average_balance(df,gender_value,avg_column_name):
    return df[df['gender'] == gender_value][avg_column_name].mean().round(2)


def get_gender_total_number_of_accounts(df,gender_value):
    return df[df['gender'] == gender_value]['gender'].agg(['count'])


def get_number_accounts_above_and_below_average(df, gender_value, avg_column_name, account_column_name):
    average = get_gender_average_balance(df, gender_value, avg_column_name)
    return df[ (df['gender']==gender_value) & (df[avg_column_name] > average) ][account_column_name].sum(), df[ (df['gender']==gender_value) & (df[avg_column_name] <= average) ][account_column_name].sum()


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

# Function to get the furthest step for each user in each session
def get_furthest_step(group):
    return group['process_step'].max()