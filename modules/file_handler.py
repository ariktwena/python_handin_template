import csv
import argparse

def print_file_content(file):
    """Print a csv file

    :param file: str
        Local file in the working directory
    """

    # Open the file
    with open(file) as f_obj:
        content = f_obj.readlines()

    # csv.reader
    for line in content[:20]:
        print(line.strip().split(','))


def write_list_to_file(output_file, lst):
    """Save a txt file with tuple list data

    :param output_file: str
        File to create

    :param lst: list
        List of tuples
    """

    # write to file
    with open(output_file, 'w') as file_object:
        for tuple_item in lst:
            entry = tuple_item[0] + ' ' + str(tuple_item[1]) + '\n'
            #entry = str(tuple_item) + ";" + '\n'
            file_object.write(entry)
    
    # Open the file
    with open(output_file) as f_obj:
        content = f_obj.readlines()

    # csv.reader
    for line in content[::]:
        print(line.strip().split(','))


def write_list_to_file_with_strings(output_file, *lst):
    """Save a txt file with string list data

    :param output_file: str
        File to create

    :param lst: list
        List of strings
    """

    # write to file
    with open(output_file, 'w') as file_object:
        for string_item in lst:
            entry = string_item + '\n'
            file_object.write(entry)
    
    # Open the file
    with open(output_file) as f_obj:
        content = f_obj.readlines()

    # csv.reader
    for line in content[::]:
        print(line.strip().split(','))


def read_csv(file):
    """Print a csv file

    :param file: str
        Local file in the working directory
    """

    # Open the file
    data = open(file, encoding = 'utf-8')

    # csv.reader
    # You can seperate with ",", ";", "\t" etc. Look at the file and find the delimiter
    csv_data = csv.reader(data, delimiter = ',')

    # Reformat it into python list
    csv_data_list = list(csv_data)

    return csv_data_list


def read_csv_cli(path, output_file=None):
    """Print a csv file

    :param path: str
        Path to the local csv file

    :param output_file: str
        Name of the output file
    """
    # Open the file
    with open(path) as f_obj:
            content = f_obj.readlines()

    if output_file == None:
        
        # csv.reader
        for line in content[::]:
            print(line.strip().split(','))
    
    else:
        with open(output_file, 'w') as file_object:
            for line in content:
                file_object.write(line)



if __name__ == "__main__":
    print("file_handler is being run as main")

    parser = argparse.ArgumentParser(description='A program that saves data to a new csv file or show the data')
    parser.add_argument('path', help='Path to the file')
    parser.add_argument('-f', '--file', help='The output file. Use ../data/ before the file, for the data folder')

    args = parser.parse_args()
    print('Path:', args.path)
    print('Output File:', args.file)

    read_csv_cli(args.path, args.file)

else:
    print("file_handler is being imported into another module")