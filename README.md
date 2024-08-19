# Illumio-Project

## Environment info

1. Python version - `3.10.0`
2. Modules used 
    - `csv`
    - `defaultdict` from `collections` module

## How to compile/run the program

1. Navigate to home directory of the project.
2. Open terminal and run the following command `python parse_flow_log_data.py flow_log_sample.txt lookup_table_sample.txt output_test.txt`. 
3. You can run the program with different input files by changing the arguments passed above. The arguments are as follows

    - 'flow_log', type=str, help='Input flow_log file name with extension'
    - 'lookup_table', type=str, help='Input lookup_table file name with extension'
    - 'output_file_name', type=str, help='Output file name with extension'
    - ###### Note that the files provided to the program should be in the inputDir/. The output of the program would be stored in outputDir/.

## Tests and Analysis

### Tested the program with different input file sizes

| flow_log size | lookup_table size | output_file |
|---------------|-------------------|-------------|
| 4 KB          | 11 mappings       |[output_Sample.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/outputDir/output_Sample.txt) |
| 10 MB         | 10000 mappings    |[output_Large-Both.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/outputDir/output_Both.txt) |
| 4 KB          | 10000 mappings    |[output_Large-Lookup.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/outputDir/output_Large-Lookup.txt) |
| 10 MB         | 11 mappings       |[output_Large-FlowLog.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/outputDir/output_Large-FlowLog.txt) |

### Analysis

![Worst-case analysis](Readme-references/image.png)

- Overall, in the worst-case scenario where `flow_log` file size is `10 MB` and `lookup_table` file has `10000 mappings`, the program ran in less than `0.2 seconds`.

- This affirms the program is capable of performing efficiently even with large file sizes and data structures.

## Assumptions

1. The program only supports the default log format, which assumes the records in `flow_log` are in the following format:

2. Only version 2 logs are considered [{Line 32 in parse_flow_log_data.py}](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L32).

3. A record from `flow_log` is considered in the "Port/Protocol Combination Counts" only if the corresponding `(dstport, protocol)` exists in the `lookup_table`  [{Line 46 in parse_flow_log_data.py}](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L46).
    - For example, the record 
    `2,123456789012,eni-9h8g7f6e,172.16.0.100,203.0.113.102,110,49156,6,12,9000,1620140761,1620140821,ACCEPT,OK`, if the `(49156, 6)` key is not present in the `lookup_table`,
    this record will be ignored for "Port/Protocol Combination Counts" in the output file.

4. The `protocol` field is derived from the `protocol_mapping.csv` file which is referenced from aws documentation`https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html` -> `http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml`.

## Files submitted

### Input Files

1. [inputDir/data.csv](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/data.csv) - a sample flow_log data file in csv format to better understand the data.
2. [inputDir/flow_log_sample.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/flow_log_sample.txt) - a sample flow_log data file in text format which is provided to the program.
3. [inputDir/flow_log_size-10mb.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/flow_log_size-10mb.txt) - a sample flow_log data file which is 10 MB in size. Used to test program in worst-case scenario.
4. [inputDir/lookup_table_maxMappings.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/lookup_table_maxMappings.txt) - a sample lookup_table file which has 10000 mappings. Used to test program in worst-case scenario.
5. [inputDir/lookup_table_sample.txt](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/lookup_table_sample.txt) - a sample lookup_table file which is provided to the program.
6. [inputDir/protocol_mapping.csv](https://github.com/Bhavik-20/Illumio-Project/blob/main/inputDir/protocol_mapping.csv) - a lookup file for mapping protocol (int) to protocol name. Referenced from aws documentation`https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html` -> `http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml`.

### Output Files

Please refer to [Tested the program with different input file sizes](README.md#tested-the-program-with-different-input-file-sizes) section of this README file to learn about the different output files.