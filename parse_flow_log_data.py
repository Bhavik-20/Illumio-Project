import csv
from collections import defaultdict

# Function to parse the protocol mapping file into a dictionary
def parse_protocol_mapping(file_path):
    protocol_mapping = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            protocol_mapping[int(row['Decimal'].strip())] = row['Keyword'].strip().lower()
    return protocol_mapping

# Function to parse the lookup table into a dictionary
def parse_lookup_table(file_path):
    lookup = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (int(row['dstport'].strip()), row['protocol'].strip().lower())
            lookup[key] = row['tag']
    return lookup

# Function to process the flow logs and generate counts
def process_flow_logs(log_file_path, lookup_table, protocol_mapping):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            version = parts[0].strip()
            if version == '2':
                dstport = int(parts[6].strip())
                protocol_number = int(parts[7].strip())

                # Get the protocol name from the protocol mapping
                protocol = protocol_mapping.get(protocol_number, "unknown").lower()

                # Create the key for lookup
                key = (dstport, protocol)
                tag = lookup_table.get(key, "Untagged")

                # Increment the counters
                tag_counts[tag] += 1
                if tag != "Untagged":
                    port_protocol_counts[(dstport, protocol)] += 1

    return tag_counts, port_protocol_counts

# Function to write the results to an output file
def write_output(tag_counts, port_protocol_counts, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

# Main function to execute the script
def main():
    protocol_mapping_file = 'inputDir/protocol_mapping.csv'
    lookup_table_file = 'inputDir/lookup_table_sample.txt'
    flow_log_file = 'inputDir/flow_log_sample.txt'

    # lookup_table_file = 'inputDir/lookup_table_maxMappings.txt'
    # flow_log_file = 'inputDir/flow_log_size-10mb.txt'

    output_file = 'outputDir/output_Sample.txt'

    protocol_mapping = parse_protocol_mapping(protocol_mapping_file)
    lookup_table = parse_lookup_table(lookup_table_file)
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_file, lookup_table, protocol_mapping)
    write_output(tag_counts, port_protocol_counts, output_file)

if __name__ == "__main__":
    main()
