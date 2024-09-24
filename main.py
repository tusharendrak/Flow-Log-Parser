import sys
from parser import parse_flow_logs
from lookup import load_lookup_table
from report import generate_report

def main(flow_log_file, lookup_table_file, output_file):
    """
    Main function to process flow logs and generate a report.

    Args:
        flow_log_file (str): Path to the flow log file.
        lookup_table_file (str): Path to the CSV lookup table file.
        output_file (str): Path to the output file where the results will be saved.
    """
    try:
        # Load the lookup table
        lookup_dict = load_lookup_table(lookup_table_file)
        
        # Parse the flow logs and apply tags based on the lookup table
        tagged_data, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_dict)
        
        # Generate and save the report
        generate_report(tagged_data, port_protocol_counts, output_file)
    
    except Exception as e:
        # Print any errors that occur during processing
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <flow_log_file> <lookup_table_file> <output_file>")
        sys.exit(1)

    # Extract arguments
    flow_log_file = sys.argv[1]
    lookup_table_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Run the main function with the provided arguments
    main(flow_log_file, lookup_table_file, output_file)