def parse_flow_logs(flow_log_file, lookup_dict):
    """
    Parse the flow log file and map each flow to a tag based on the lookup table.
    
    Args:
    flow_log_file (str): Path to the flow log file.
    lookup_dict (dict): Dictionary containing the (dstport, protocol) -> tag mapping.
    
    Returns:
    tuple: Two dictionaries - 
        1. Tagged data count by tags, including untagged logs.
        2. Count of matches for each port/protocol combination.
    """
    tag_counts = {}
    port_protocol_counts = {}
    
    try:
        with open(flow_log_file, 'r') as file:
            for line in file:
                columns = line.split()
                if len(columns) < 14:
                    continue  # Ignore lines with insufficient data
                
                dstport = columns[5].strip()
                protocol_number = columns[7].strip()
                
                # Map the protocol number to its corresponding protocol name (e.g., '6' -> 'tcp', '17' -> 'udp', '1' -> 'icmp').
                # If the protocol number is not found, default to 'unknown'.
                protocol = {'6': 'tcp', '17': 'udp', '1': 'icmp'}.get(protocol_number, 'unknown')
                
                key = (dstport, protocol)
                
                # Tag lookup
                tag = lookup_dict.get(key, 'Untagged')  # Default to 'Untagged' if not found
                
                # Update tag count
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
                
                # Update port/protocol combination count
                port_protocol_counts[key] = port_protocol_counts.get(key, 0) + 1
    
    except FileNotFoundError:
        raise Exception(f"Flow log file '{flow_log_file}' not found.")
    except Exception as e:
        raise Exception(f"Error processing flow log file: {e}")
    
    return tag_counts, port_protocol_counts
