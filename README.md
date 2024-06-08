# OilSpillDetection

Detecting oil spills in the sea is crucial for protecting the environment and responding to ecological disasters, preventing harm to marine life and coastal ecosystems. This project aims to develop a Python algorithm to assist in detecting oil spills on the ocean surface by identifying affected areas based on satellite images.

## Features

- Request the size of the grid squares in square meters.
- User input for each grid square, identifying water ('A') or oil ('O').
- Store the user input data in a list.
- Analyze the data to detect the presence of oil spills.
- Print the analyzed data, indicating the presence of oil and its positions in the list.
- Calculate the total area of oil spills based on the user input data.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/OilSpillDetection.git
    ```
2. Navigate to the project directory:
    ```bash
    cd OilSpillDetection
    ```
3. Run the Python script:
    ```bash
    python3 oil_spill_detection.py
    ```

## Code Structure

The project consists of several functions to obtain user input, process data, and generate output:

- `get_square_size()`: Requests and returns the size of the squares in square meters.
- `get_number_of_squares()`: Requests and returns the number of squares the user wants to analyze.
- `capture_square_values(total_squares)`: Captures the values of each square (water or oil) and stores them in a list.
- `display_squares(values)`: Prints the captured values of the squares.
- `analyze_oil_spills(values, square_area)`: Analyzes the data to detect oil spills and calculates the total area of the spills.

## Example Usage

```plaintext
Enter the size of the square in m²: 10
Enter the number of squares: 5
Enter the value of square 1 (A for water, O for oil): O
Enter the value of square 2 (A for water, O for oil): A
Enter the value of square 3 (A for water, O for oil): O
Enter the value of square 4 (A for water, O for oil): A
Enter the value of square 5 (A for water, O for oil): O

Square values:
Square 1: O
Square 2: A
Square 3: O
Square 4: A
Square 5: O

Oil spills detected at positions: [0, 2, 4]
Total area of oil spills: 30.00 m²
