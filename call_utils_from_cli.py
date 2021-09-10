from modules import utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Different functions')
    parser.add_argument('-op', '--operation', help='Write "getFolders", "getFiles", "printLine", "printEmail"')
    parser.add_argument('-p', '--path', help='Path to the file')
    parser.add_argument('-o', '--outputfile', help='The output file. Use data/example.csv data/output.txt before the file, and seperate the files with a space " "')
    parser.add_argument('-f', '--filenames', nargs='+', type=str, help='An array of file names seperated by " "')
    parser.add_argument('-m', '--mdfilenames', nargs='+', type=str, help='An array of md file names seperated by " "')

    args = parser.parse_args()
    print('Operation:', args.operation)
    print('Path:', args.path)
    print('Output File:', args.outputfile)
    print('File names:', args.filenames)
    print('MD file names:', args.mdfilenames)

    if args.operation == 'getFiles' and args.path != None and args.outputfile != None:
        utils.get_file_names(args.path, args.outputfile)
    elif args.operation == 'getFolders' and args.path != None and args.outputfile != None:
        utils.get_all_file_names(args.path, args.outputfile)
    elif args.operation == 'printLine' and args.filenames != None:
        utils.print_line_one(args.filenames)
    elif args.operation == 'printEmail' and args.filenames != None:
        #python3 call_utils_from_cli.py -f ./data/example.csv ./data/output.txt
        #python3 call_utils_from_cli.py -f data/example.csv data/output.txt
        utils.print_emails(args.filenames)
    elif args.mdfilenames != None and args.outputfile != None:
        utils.write_headlines(args.filenames)
    else:
        print("Please fill the infos you want.")


    