# Flow Log Parser with Tag Mapping

## Overview
This program parses flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a CSV file with three columns: `dstport`, `protocol`, and `tag`. The combination of `dstport` and `protocol` determines the tag applied to each flow log row.

The output is a summary file that contains:
- The count of matches for each tag, including unmatched logs (referred to as "Untagged").
- The count of matches for each port/protocol combination.

## Assumptions

### Log Format
- The program only supports default log format (as shown in the example in the problem statement).
- The flow logs must be in the version 2 format, as no other versions are supported.
- The logs should have at least 14 fields (as shown in the provided example). Lines with fewer fields will be skipped.

### Protocol Mapping
- Protocol is assumed to be either TCP or UDP based on the protocol number (6 for TCP, 17 for UDP).
- Any unknown protocol will default to 'Untagged'.

### Case Insensitivity
- Matching for protocol in the lookup table is case insensitive.
- Ports are handled as strings to ensure consistent matching (although ports are numerical values).

### File Size
- The program is designed to handle flow log files up to 10 MB.
- The lookup file can have up to 10,000 entries.

### Error Handling
- If any input files are missing or incorrectly formatted, the program will raise a detailed exception message.
- If a flow log entry cannot be parsed (due to missing fields or invalid data), that entry will be skipped.

### Performance Considerations
- The program avoids loading large files into memory at once by processing files line-by-line.
- Lookup operations are O(1) on average due to the use of Python dictionaries.

### Default Libraries
- No non-default libraries are used. The program runs purely on Python's standard libraries, ensuring compatibility on local machines without extra dependencies.

## Input/Output

### Input Files
- **Flow Log File (Plain text)**: This file contains flow log entries in a space-separated format.
- **Lookup Table (CSV)**: This file contains mappings of `dstport`, `protocol`, and `tag`.

### Output File
The output is written to a specified file and contains two sections:
- **Tag Counts**: The count of each tag, including untagged entries.
- **Port/Protocol Combination Counts**: The count of occurrences for each port and protocol combination.


### Example Input:
Flow Log:
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
...

### Lookup Table:
dstport,protocol,tag
25,tcp,sv_P1
443,tcp,sv_P2
23,tcp,sv_P1
110,tcp,email
993,tcp,email
...

### Example Output:
Tag Counts:
Tag,Count
sv_P2,1
sv_P1,2
email,3
Untagged,9

Port/Protocol Combination Counts:
Port,Protocol,Count
22,tcp,1
23,tcp,1
25,tcp,1
110,tcp,1
443,tcp,1
993,tcp,1
...

## Installation and Running the Program

### Prerequisites:
- Python 3.x (Tested on Python 3.8 and above).
- No additional libraries required.

### How to Run:
1. Clone the repository or download the source files.
2. Place the flow log file and the lookup table CSV file in the same directory as the code files.
3. Run the program using the following command:
   ```bash
   python main.py <flow_log_file> <lookup_table_file> <output_file>

### Where:

<flow_log_file>: Path to the flow log file.
<lookup_table_file>: Path to the CSV lookup table file.
<output_file>: Path to the output file where the results will be saved.

Example Run:
python main.py flow_logs.txt lookup_table.csv output_report.txt

File Structure:
.
├── main.py                # Entry point of the program
├── parser.py              # Contains logic to parse flow logs
├── lookup.py              # Loads and processes the lookup table
├── report.py              # Generates the output report
├── exceptions.py          # Custom exceptions for error handling
├── utils.py               # Utility functions (if necessary)
├── flow_logs.txt          # Example flow log file
├── lookup_table.csv       # Example lookup table
├── output_report.txt      # Output report (generated)
└── README.md              # This documentation

## Testing

Test Cases:
Happy Path: Tested the program with a properly formatted flow log file and a valid lookup table.

Result: The output file is generated with accurate tag counts and port/protocol counts.
Missing Lookup Entry: Tested for flows where no tag is found in the lookup table.

Result: Such flows are correctly tagged as "Untagged".
Insufficient Fields in Flow Log: Tested with log lines that have fewer than 14 fields.

Result: The lines with insufficient data are skipped.
File Not Found: Tested by providing incorrect file paths for the flow log or lookup table.

Result: The program raises a descriptive error message.
Case Insensitivity: Tested to ensure protocol matching is case insensitive.

Result: Protocol matching works regardless of case (e.g., TCP or tcp).
Invalid Lookup Table: Tested with an incorrectly formatted lookup table (missing columns).

Result: The program raises an exception due to missing data.

## Performance Test:
The program was tested with a flow log file of approximately 10 MB and processed the data efficiently, demonstrating its ability to handle logs within the specified limits.
Exception Handling
FileNotFoundError: Raised when any of the input files (flow log or lookup table) are not found.
MalformedDataError: Raised when a flow log entry or lookup table entry has incorrect data (e.g., missing fields).
GenericException: Any other unhandled exception will be caught, and an appropriate error message will be displayed.
Performance and Scaling Considerations
Line-by-Line Processing: The flow log file is processed line-by-line, minimizing memory usage, which is important for handling larger files up to the specified limit (10 MB).

Efficient Lookups: A Python dictionary is used to store the lookup table, enabling O(1) average time complexity for each tag lookup. This ensures that even with a large number of mappings (up to 10,000), performance remains optimal.

Parallel Processing: In a high-throughput scenario, the program can be scaled by using parallel processing or threading (though not implemented here). This can be achieved by processing chunks of the flow log file in parallel.

## Future Improvements
Support for Additional Protocols: Currently, only TCP and UDP are supported. Future updates could add support for other protocols.
Custom Log Formats: The program could be enhanced to support custom log formats or flow log versions.
Batch Processing: Implement batch processing for environments handling larger files or continuous data streams.