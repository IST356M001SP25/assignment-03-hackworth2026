'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
file_count = 0
line_count = 0

# Process files
# ...

# Increment file_count and line_count for each file read
file_count += 1
num_lines_in_file = 10  # Replace 10 with the actual number of lines in the file
line_count += num_lines_in_file

# Output summary information
print(f"{file_count} packages written to file.json")
