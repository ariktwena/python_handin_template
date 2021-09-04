import os

def get_file_names(folderpath, out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

    dir_list = os.listdir(folderpath)

    print(dir_list)

    output_file = "./data/" + out

    with open(output_file, 'w') as file_object:
        for file_name in dir_list:
            entry = str(file_name) + "\n"
            file_object.write(entry)


def get_all_file_names(folderpath,out='output_files.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    output_file = "./data/" + out

    # Walk giver en tuple retur som vi unpacker
    for folder, sub_folder, files in os.walk(folderpath):
        print(f'Currently looking at folder: {folder}')
        print('\n')
        print('The subfolders are:')
        for sub_fold in sub_folder:
            print(f'\t Subfolder: {sub_fold}')
        print('\n')
        print('The files are:')
        with open(output_file, 'a') as file_object:
                for file_name in files:
                    print(f'\t File: {file_name}')
                    entry = str(file_name) + "\n"
                    file_object.write(entry)
        print('\n')

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

    for file_name in file_names:
        # Open the file
        with open(file_name) as f_obj:
            content = f_obj.readlines()

        # csv.reader
        for line in content[:1]:
            print(line)

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

    for file_name in file_names:
        # Open the file
        with open(file_name) as f_obj:
            content = f_obj.readlines()

        # csv.reader
        for line in content[::]:
            if '@' in line:
                print(line)

def write_headlines(md_files, out='output_md.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""

    output_file = "./data/" + out

    for file_name in md_files:
        # Open the file
        with open(file_name) as f_obj:
            content = f_obj.readlines()

        # csv.reader
        for line in content[:1:]:
            if line[0] == '#' and line[1] == ' ':
                print(line)
                with open(output_file, 'a') as file_object:
                    entry = str(line) + "\n"
                    file_object.write(entry)


if __name__ == "__main__":
    print("Utils is being run as main")

else:
    print("Utils is being imported into another module")