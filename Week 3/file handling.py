def read_file(file_path):
    """ Read the data from the file. File is present in python language.
    We have to make sure that code is according to the predefined
    format. So, go and do fun with coding. Happy Coding!
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Content:")
            print(contents)
            word_count = len(contents.split())
            print("Number of words: ", word_count)
    except FileNotFoundError:
        print("Error: The file ", file_path, "was not found.")
    except Exception as e:
        print("An error occurred while reading the file: ", e)

def write_to_file(file_path):
    
    #Function to write user input to a file and handle exceptions.
    
    try:
        user_input = input("Enter the text in the file: ")
        with open(file_path, 'w') as file:
            file.write(user_input)
        print("Data successfully written to ", file_path)
    except Exception as e:
        print("An error occurred while writing to the file:", e)

# Read from 'data.txt' and count words
read_file('data.txt')

# Write user input to 'output.txt'
write_to_file('output.txt')
