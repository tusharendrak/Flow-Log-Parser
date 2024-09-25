# Flow Log Parser (Illumio Technical Assessment)

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

### File Structure:

├── main.py                # Entry point of the program

├── parser.py              # Contains logic to parse flow logs

├── lookup.py              # Loads and processes the lookup table

├── report.py              # Generates the output report

├── flow_logs.txt          # Example flow log file

├── lookup_table.csv       # Example lookup table

├── README.md              # The documentation

└── output_report.txt      # Output report (generated)

## Testing and Analysis

### Manual and Unit Tests
- **Test 1: Basic Functionality**: Verified that the program correctly parses a flow log file and maps tags based on a lookup table.
- **Test 2: Handling Blank Lines**: Ensured that blank lines in the flow log file are skipped without causing errors.
- **Test 3: Insufficient Columns**: Confirmed that lines with fewer than 14 columns are ignored.
- **Test 4: Protocol Mapping**: Checked that protocol numbers are correctly mapped to their respective names (TCP, UDP, ICMP) and that unknown protocols default to 'unknown'.
- **Test 5: Case Insensitivity**: Verified that protocol matching in the lookup table is case insensitive.
- **Test 6: Large Files**: Tested the program with flow log files up to 10 MB to ensure performance and correctness.
- **Test 7: Lookup Table Size**: Ensured that the program can handle lookup tables with up to 10,000 entries.
  
### Exception Handling
- FileNotFoundError: Raised when any of the input files (flow log or lookup table) are not found.
- MalformedDataError: Raised when a flow log entry or lookup table entry has incorrect data (e.g., missing fields).
- GenericException: Any other unhandled exception will be caught, and an appropriate error message will be displayed.

### Analysis
- **Performance**: The program performs efficiently with flow log files up to 10 MB and lookup tables with up to 10,000 entries. The use of dictionaries for tag and port/protocol counts ensures fast lookups and updates.
- **Robustness**: The program handles various edge cases, such as blank lines, lines with insufficient columns, and unknown protocols. Detailed error messages are provided for missing or incorrectly formatted input files.
- **Scalability**: While the current implementation is designed for files up to 10 MB, the program can be scaled to handle larger files with minor optimizations, such as using more efficient data structures or parallel processing.
- **Efficient Lookups**: A Python dictionary is used to store the lookup table, enabling O(1) average time complexity for each tag lookup. This ensures that even with a large number of mappings (up to 10,000), performance remains optimal.

### Future Improvements
- **Enhanced Protocol Mapping**: Extend the protocol mapping to include more protocols beyond TCP, UDP, and ICMP.
- **Configurable Limits**: Allow users to configure the maximum file size and lookup table size through command-line arguments or a configuration file.
- **Parallel Processing**: Implement parallel processing to handle larger flow log files more efficiently.
- **Logging**: Add logging to provide more insights into the program's execution and help with debugging.
