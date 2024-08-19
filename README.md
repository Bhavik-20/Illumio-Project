# Illumio-Project

## Assumptions

1. The program only supports the default log format, which assumes the records in `flow_log` are in the following format:

2. Only version 2 logs are considered [See line 32 in parse_flow_log_data.py](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L32).

3. A record from `flow_log` is considered in the "Port/Protocol Combination Counts" only if the corresponding `(dstport, protocol)` exists in the `lookup_table`  [See line 45 in parse_flow_log_data.py](https://github.com/Bhavik-20/Illumio-Project/blob/main/parse_flow_log_data.py#L45).
- Example: For the record `2,123456789012,eni-9h8g7f6e,172.16.0.100,203.0.113.102,110,49156,6,12,9000,1620140761,1620140821,ACCEPT,OK`, if the `(49156, 6)` key is not present in the `lookup_table`, this record will be ignored for "Port/Protocol Combination Counts" in the output file.