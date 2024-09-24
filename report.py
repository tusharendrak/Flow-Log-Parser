def generate_report(tagged_data, port_protocol_counts, output_file):
    """
    Generate the report with tag counts and port/protocol combination counts.
    
    Args:
    tagged_data (dict): A dictionary of tag counts.
    port_protocol_counts (dict): A dictionary of port/protocol combination counts.
    output_file (str): Path to the output file.
    """
    try:
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the header for the tag counts section
            file.write("Tag Counts:\n")
            file.write("Tag,Count\n")
            
            # Write each tag and its count
            for tag, count in tagged_data.items():
                file.write(f"{tag},{count}\n")
            
            # Write the header for the port/protocol combination counts section
            file.write("\nPort/Protocol Combination Counts:\n")
            file.write("Port,Protocol,Count\n")
            
            # Write each port/protocol combination and its count
            for (port, protocol), count in port_protocol_counts.items():
                file.write(f"{port},{protocol},{count}\n")
    except Exception as e:
        # Raise an exception if there is an error writing the output file
        raise Exception(f"Error writing output file: {e}")