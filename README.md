# Port Status Checker

## Description

Port Status Checker is a Python application that determines whether a specific port on a target system is open or closed. It uses Python's socket programming to establish a connection and reports the port status, helping users understand basic network communication and service availability.

## Features

* Checks the status of a specified port.
* Accepts a hostname or IP address as input.
* Displays whether the port is open or closed.
* Uses Python socket programming.
* Simple and easy-to-use command-line interface.

## Technologies Used

* Python 3
* Socket Module

## Requirements

* Python 3.x

## How to Run

1. Save the program as `port_status_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

   ```
   python port_status_checker.py
   ```
5. Enter the target IP address or hostname and the port number when prompted.

## Sample Input

```
Enter Host/IP: localhost
Enter Port Number: 80
```

## Sample Output

```
Port 80 is OPEN.
```

or

```
Port 80 is CLOSED.
```

## Project Structure

```
Port-Status-Checker/
│── port_status_checker.py
└── README.md
```

## Future Enhancements

* Scan multiple ports simultaneously.
* Display the service name running on open ports.
* Generate a scan report.
* Add a graphical user interface (GUI).
* Support concurrent scanning for faster results.

## Author

A. Pranavi Sri
