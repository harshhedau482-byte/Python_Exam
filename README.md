# Personal Fitness Tracker Dashboard

This is a Python-based **Personal Fitness Tracker Dashboard** designed to allow fitness enthusiasts to log, analyze, and visualize their activity and health trends.

This project is submitted to **Red & White Skill Education** as part of the Skill Development project requirements. It integrates fundamental programming concepts and data analysis tools including Object-Oriented Programming (OOP), Data Handling, NumPy, Pandas, and professional visualization using Matplotlib and Seaborn.

---

## Project Structure

*   `fitness_tracker.py`: The main application script containing the `FitnessTracker` class and the command-line interface.
*   `generate_data.py`: A utility script used to generate a sample dataset (`fitness_activities.csv`) for testing and demonstration purposes.
*   `fitness_activities.csv`: (Generated automatically) The dataset file where activities are stored.
*   `README.md`: This document.

---

## Features and Functionalities

The application implements the following core features:

1.  **Activity Logging (OOP & Pandas)**
    *   Allows users to input activity data: date (current), activity type, duration, and calories burned.
    *   Automatically saves data to a local CSV file using Pandas for persistent storage.

2.  **User Input Validation (Control Structures)**
    *   Ensures duration and calories are positive numbers.
    *   Verifies activity types are non-empty.

3.  **Data Analysis & Metrics (NumPy & Pandas)**
    *   **calculate_metrics():** Computes and displays key performance indicators:
        *   Total activities logged.
        *   Total calories burned.
        *   Average duration per activity.
        *   Most frequent activity type.
    *   Generates new metrics like "Calories per Minute."

4.  **Data Filtering (Pandas)**
    *   **filter_activities():** Filters the dataset based on activity type, date range, or a combination of both.

5.  **Data Visualization (Matplotlib & Seaborn)**
    *   **generate_report():** Compiles metrics and automatically launches four distinct, high-quality graphs:
        *   **Bar Chart:** Total time spent on each activity type.
        *   **Line Graph:** Trend of total calories burned over time.
        *   **Pie Chart:** Percentage distribution of different activity types.
        *   **Heatmap:** Correlation matrix between exercise duration and calories burned.

---

## Technical Specifications & Integration

This project was developed with specific focus on architectural requirements and module integration:

*   **OOP Design:** Encapsulates all functional logic within the `FitnessTracker` class for modularity and reusability.
*   **NumPy Integration:** Used for numerical analysis and rounding metrics.
*   **Pandas for Data Handling:** Used for efficient data loading (`read_csv`), storing (`to_csv`), cleaning, grouping, and filtering.
*   **Data Visualization:** Custom styling via Seaborn is used, ensuring all graphs feature proper titles, labels, and legends as required.
*   **Edge Case Handling:** Includes handling for scenarios such as empty datasets or missing CSV files.

---

## Setup and Usage Instructions

### Prerequisites

You must have Python installed. The following libraries are required and can be installed via pip:

```bash
pip install pandas numpy matplotlib seaborn