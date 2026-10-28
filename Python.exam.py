import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# --- Fitness Tracker Class ---
class FitnessTracker:
    def __init__(self, data_file='fitness_activities.csv'):
        self.data_file = data_file
        # Initialize an empty DataFrame with the specified columns
        self.df = pd.DataFrame(columns=['Date', 'Activity Type', 'Duration (Minutes)', 'Calories Burned'])
        self.load_data()

    def load_data(self):
        """Loads data from CSV. Handles case where file doesn't exist."""
        try:
            self.df = pd.read_csv(self.data_file)
            print(f"Loaded data from {self.data_file}")
        except FileNotFoundError:
            print(f"{self.data_file} not found. A new file will be created.")

    def log_activity(self, activity_type, duration, calories):
        """Logs new fitness activity into a dataset after simple validation."""
        
        # Simple Validation (ensuring duration and calories are positive)
        if duration <= 0 or calories <= 0:
            print("Error: Duration and Calories must be positive numbers.")
            return

        # Prepare new data
        new_activity = {
            'Date': [datetime.now().strftime('%Y-%m-%d')],  # Current date
            'Activity Type': [activity_type],
            'Duration (Minutes)': [duration],
            'Calories Burned': [calories]
        }
        
        # Add new row to DataFrame
        self.df = pd.concat([self.df, pd.DataFrame(new_activity)], ignore_index=True)
        
        # Save updated data back to CSV
        self.df.to_csv(self.data_file, index=False)
        print(f"Activity '{activity_type}' logged successfully.")

    def calculate_metrics(self):
        """Calculates and prints simple metrics."""
        if self.df.empty:
            print("No data available to calculate metrics.")
            return

        total_calories = self.df['Calories Burned'].sum()
        total_duration = self.df['Duration (Minutes)'].sum()
        avg_duration = self.df['Duration (Minutes)'].mean()

        print("\n--- Summary Metrics ---")
        print(f"Total Calories Burned: {total_calories} cal")
        print(f"Total Time Spent: {total_duration} minutes")
        print(f"Average Duration per Activity: {avg_duration:.2f} minutes")

    def show_all_activities(self):
        """Displays all activities in the dataset."""
        if self.df.empty:
            print("\nNo activities logged yet.")
        else:
            print("\n--- All Logged Activities ---")
            print(self.df.to_string(index=False))

    def generate_simple_visualizations(self):
        """Generates simple bar charts."""
        if self.df.empty:
            print("No data available for visualizations.")
            return

        print("\nGenerating simple graphs...")

        # Setting the aesthetic style
        sns.set_theme(style="whitegrid")

        # 1. Simple Bar Chart: Time per activity type
        plt.figure(figsize=(10, 6))
        # Pandas handles the aggregation automatically in Seaborn
        sns.barplot(data=self.df, x='Activity Type', y='Duration (Minutes)', estimator=sum, errorbar=None)
        plt.title('Total Duration Spent per Activity Type')
        plt.xlabel('Activity Type')
        plt.ylabel('Total Duration (Minutes)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# --- Main Program Loop (Control Structure) ---
def main():
    """Main program function."""
    print("Welcome to the SIMPLE Personal Fitness Tracker Dashboard")
    
    tracker = FitnessTracker()

    while True:
        # Simple menu system
        print("\n--- Menu ---")
        print("1. Log a new fitness activity")
        print("2. View simple health metrics")
        print("3. View all logged activities")
        print("4. Generate simple graphs")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            activity_type = input("Enter activity type (e.g., Running, Yoga): ").capitalize()
            try:
                duration = float(input("Enter duration in minutes: "))
                calories = float(input("Enter calories burned: "))
                tracker.log_activity(activity_type, duration, calories)
            except ValueError:
                print("Error: Invalid numerical input for duration or calories.")
                
        elif choice == '2':
            tracker.calculate_metrics()
            
        elif choice == '3':
            tracker.show_all_activities()
            
        elif choice == '4':
            tracker.generate_simple_visualizations()
            
        elif choice == '5':
            print("\nExiting. Stay healthy!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()