import csv

def load_lookup_table(lookup_file):
    """
    Load the lookup table from a CSV file into a dictionary.
    The dictionary is keyed by (dstport, protocol) and maps to tags.
    
    Args:
    lookup_file (str): Path to the lookup CSV file.
    
    Returns:
    dict: A dictionary mapping (dstport, protocol) to tag.
    """
    lookup_dict = {}
    try:
        with open(lookup_file, 'r') as file:
            reader = csv.DictReader(file)
            # Normalize fieldnames by stripping whitespace
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            
            # Check if the required columns are present
            required_columns = {'dstport', 'protocol', 'tag'}
            if not required_columns.issubset(reader.fieldnames):
                missing_columns = required_columns - set(reader.fieldnames)
                raise ValueError(f"Missing columns in lookup file: {', '.join(missing_columns)}")
            
            for row in reader:
                port = row['dstport'].strip()
                protocol = row['protocol'].strip().lower()  # case insensitive
                tag = row['tag'].strip()
                lookup_dict[(port, protocol)] = tag
    except FileNotFoundError:
        raise Exception(f"Lookup file '{lookup_file}' not found.")
    except ValueError as ve:
        raise Exception(f"Error reading lookup file: {ve}")
    except Exception as e:
        raise Exception(f"Unexpected error reading lookup file: {e}")
    
    return lookup_dict