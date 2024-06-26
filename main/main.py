from matplotlib import pyplot as plt
import read_process as rp
import domain_extract as de

def main():
    """
    The main function that serves as the entry point for the program.
    
    This function checks the command line arguments passed to the program and performs the appropriate action based on the arguments.
    
    Parameters:
        None
    
    Returns:
        None
    """
    if len(plt.sys.argv) == 1:
        show_help()
    elif plt.sys.argv[1] in ['-h', '--help']:
        show_help()
    elif plt.sys.argv[1] in ['-v', '--view']:
        process()
    elif plt.sys.argv[1] in ['-c', '--config']:
        config_message()
    else:
        print("Invalid command. Use '-h' or '--help' for usage instructions.")
    input("Press enter to exit...")

def show_help():
    """
    Displays the help message for smartView.

    This function prints a message that provides information about smartView, the author, the Python version used, and a disclaimer about the term "smart". It also provides instructions on how to use smartView by specifying the command line arguments. Finally, it prompts the user to press enter to exit.

    Parameters:
        None

    Returns:
        None
    """
    print('''smartView
smartView is a tool that helps you to visualize the data coming from smart online database
liushuotong SDUW 2024

python version: 3.11.6

"smart" is not cleaver!!!
"smart" means Simple Modular Architecture Reseach Tools.

smartView -h/--help       show help message     
smartView -v/--view       process data and show result
smartView -c/--config     show config message

https://github.com/liushuotong
''')

    

def config_message():
    """
    Displays the configuration message for smartView.

    This function prints a message that provides information about the configuration of smartView, the author, the version, and the GitHub repository. It prompts the user to press enter to exit.

    Parameters:
        None

    Returns:
        None
    """
    print('''config message
smartView
liushuotong SDUW 2024
https://github.com/liushuotong
version: 1.0
''')


def process():
    fasta_location = input("Fasta file:")
    smart_txt = input("SMART file:")
    # basic data preprocessing: sequnences, len_sequences, results
    sequences = rp.read_fasta(fasta_location)
    len_sequences = rp.fasta_len(sequences)
    results = rp.smart_txt_read(smart_txt)
    '''smartView
    dataType_summary:
    +--------------------------------------------------------------------------------------------------------------+
    |      # liushuotong SDUW 2024.4.24                                                                            |
    |      # version 1.0                                                                                           |
    +--------------------------------------------------------------------------------------------------------------+
    |   sequences -> a dictionary containing the sequences                                                         |
    |   example:                                                                                                   |
    |   'id_name':'MSANIHUBILHLGHFJK'                                                                              |
    +--------------------------------------------------------------------------------------------------------------+
    |   len_dict -> a dictionary containing the sequence names as keys and their lengths as values                 |
    |    example:                                                                                                  |
    |   'id_name':'12'                                                                                             |
    +--------------------------------------------------------------------------------------------------------------+
    |   results -> a list of dictionaries, where each dictionary represents a protein and its associated features  |
    |   example:                                                                                                   |
    |   [{                                                                                                         |
    |       'USER_PROTEIN_ID': 'transcript:TraesCSU02G058300.1',                                                   |
    |       'SMART_PROTEIN_ID': 'uniprot|A0A1D5WM65|A0A1D5WM65_WHEAT',                                             |
    |       'NUMBER_OF_FEATURES_FOUND': 2,                                                                         |
    |       'FEATURES':[                                                                                           |
    |           {                                                                                                  |
    |               'DOMAIN': 'Pfam:Dimerisation',                                                                 |
    |               'START': 36,                                                                                   |
    |               'END': 84,                                                                                     |
    |               'EVALUE': 9.3e-12,                                                                             |
    |               'TYPE': 'PFAM',                                                                                |
    |               'STATUS': 'visible|OK'                                                                         |
    |           },{                                                                                                |
    |               'DOMAIN': 'Pfam:Methyltransf_2',                                                               |
    |               'START': 135,                                                                                  |
    |               'END': 364,                                                                                    |
    |               'EVALUE': 2.1e-60,                                                                             |
    |               'TYPE': 'PFAM',                                                                                |
    |               'STATUS': 'visible|OK'                                                                         |
    |           }]                                                                                                 |
    |   },{                                                                                                        |
    |               ......                                                                                         |
    |   }]                                                                                                         |
    +--------------------------------------------------------------------------------------------------------------+
    '''
    # domain data extraction
    de.extract_based_on_domain(results)
    de.split_fasta(sequences)


if __name__ == "__main__":
    main()