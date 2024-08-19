# Illumio-Project

## Environment info

1. Python version - 3.10.0
2. Modules used 
- `csv`
- `defaultdict` from `collections` module

## How to compile/run the program

1. Navigate to home directory of the project.
2. Open terminal and run the following command `python parse_flow_log_data.py`. 

## Tests and Analysis

Tested the program with different input file sizes

| flow_log size | lookup_table size | output_file |
|---------------|-------------------|-------------|
| 4 KB          | 11 mappings       |[output_Sample.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/outputDir/output_Sample.txt) |

## Assumptions

1. The program only supports the default log format, which assumes the records in `flow_log` are in the following format:

2. Only version 2 logs are considered [{Line 32 in parse_flow_log_data.py}](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L32).

3. A record from `flow_log` is considered in the "Port/Protocol Combination Counts" only if the corresponding `(dstport, protocol)` exists in the `lookup_table`  [{Line 45 in parse_flow_log_data.py}](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L45).
- For example, the record 
`2,123456789012,eni-9h8g7f6e,172.16.0.100,203.0.113.102,110,49156,6,12,9000,1620140761,1620140821,ACCEPT,OK`, if the `(49156, 6)` key is not present in the `lookup_table`,
 this record will be ignored for "Port/Protocol Combination Counts" in the output file.