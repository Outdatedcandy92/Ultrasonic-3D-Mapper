# 3D mapping using ultrasonic sensor

This project involves reading data from an Arduino via a serial connection, storing the data in a file, and then plotting the data in 3D using Python.

## Components

1. **Arduino**: Sends data via serial communication.
    - Ultrasonic Sensor
    - 2 Servo Motors
2. **Python Script (`test.py`)**: Reads data from the serial port and stores it in `data.txt`.
3. **Python Script (`graph.py`)**: Reads the stored data from `data.txt` and plots it in 3D using nearest interpolation.

## Requirements

- Python 3.x
- `pyserial` library
- `numpy` library
- `matplotlib` library
- `scipy` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required libraries using pip:
    ```sh
    pip install pyserial numpy matplotlib scipy
    ```

## Usage

### Running the Data Logger

1. Connect your Arduino to your computer.
2. Ensure the Arduino is sending data to the correct COM port.
3. Run the `run.py` script to start reading and storing data:
    ```sh
    python run.py
    ```
4. The script will store the data in `data.txt`.

### Plotting the Data

1. Once you have collected enough data, run the `graph.py` script to plot the data in 3D:
    ```sh
    python graph.py
    ```

## Files

- `run.py`: Script to read data from the Arduino and store it in `data.txt` and then graph it.
- `graph.py`: Script to read data from `data.txt` and plot it in 3D.
- `data.txt`: File where the data is stored.

## Example

An example of the data format in `data.txt`:


