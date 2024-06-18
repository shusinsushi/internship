def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src:
        data = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(data)

source = input("Enter the name of the source file: ")
destination = input("Enter the name of the destination file: ")

copy_file_contents(source, destination)
print(f"Contents of {source} have been copied to {destination}.")
