# Documentation Auto-Updater

## Requirements

Python script that inserts and updates Google-style docstrings in Python files and logs the operations

### Input/Output

1. The program should accept a directory as input and scan all Python (.py) files in it, including those in subdirectories.
1. The program should update the Python files in place, adding or updating file-level docstrings as necessary.
1. The program should output a log file detailing its operations.

### Docstring Parsing and Writing

1. The program should use a Python parsing library, such as ast or parso, to parse the Python files. This allows it to understand the structure of the code and identify existing docstrings.
1. If a file does not have a docstring, the program should insert one at the beginning of the file. The docstring should provide a basic template that conforms to the Google style. The developer can then fill in the details.
1. If a file already has a docstring, the program should check whether it conforms to the Google style. If not, the program should update the docstring to match the Google style, preserving any existing content where possible.
1. The program should generate as much of the docstring content as possible based on the code. For example, it could list the functions, classes, and methods defined in the file, along with their arguments.

### Logging

1. The program should use the logging module to log its operations. It should record the start and end of the process, each file it processes, and any docstrings it adds or updates.
1. The program should write the log messages to a text file. It should also print them to the console so that the user can monitor the process.
1. The program should use the logging module's level system to control the verbosity of the log. The user should be able to set the log level (e.g., INFO, DEBUG) as a command-line argument.

### Error Handling

1. The program should handle any exceptions that occur during the parsing, writing, or logging processes. It should log the exceptions and continue with the next file.

### Additional Functionality

1. The program could provide a dry-run option that doesn't change any files but shows what changes would be made. This allows the user to preview the results before running the program for real.
1. The program could provide a backup option that saves the original versions of the files before making any changes. This allows the user to easily revert the changes if necessary.
1. The program could provide an interactive mode where it prompts the user for confirmation before making each change. This gives the user more control over the process.
1. The program could provide a way to ignore certain files or directories. The user could specify these as command-line arguments or in a configuration file.
1. The program could provide a way to add or update docstrings for individual functions, classes, or methods, not just files. This would require more sophisticated parsing and writing code.

## Tree structure

![Tree](./docs/tree.md)

## File functions

Here is a brief description of what each file might contain:

`__init__.py`: This is an empty file that indicates to Python that the directory should be treated as a package.
`docstring_parser.py`: This file contains the DocstringParser class, which is responsible for parsing Python files and identifying existing docstrings. It uses a Python parsing library like ast or parso.
`docstring_writer.py`: This file contains the DocstringWriter class, which is responsible for writing new docstrings and updating existing ones. It uses the information provided by the DocstringParser class.
`logger.py`: This file contains the Logger class, which is responsible for logging the operations of the program. It uses the logging module.
`utils.py`: This file contains additional functionality that doesn't fit neatly into the other classes. This might include error handling, the dry-run option, the backup option, and the interactive mode.
`main.py`: This is the main script that the user runs. It imports the classes from the doc_oct package and uses them to scan a directory, add or update docstrings, and log the operations. It also handles command-line arguments and controls the overall flow of the program.
`/logs/logs.txt`: This is the text file that the Logger class writes to. It's located in the same directory as main.py for convenience, but its location could be configurable.

Note that this is just one possible structure for the program. The exact structure would depend on the specifics of your implementation and your personal coding style.

### Docstrings

Here is a basic implementation of docstring_writer.py and docstring_parser.py. Note that this is a simplified example and doesn't cover all the requirements you mentioned. It would need to be expanded and adjusted to fit your specific needs.

The DocstringWriter class has a write_docstring method that writes a docstring to the beginning of a file.

The DocstringParser class uses the ast module to parse Python files. It has a get_docstring method that returns the docstring of a file, or None if the file does not have a docstring.

Note that this code does not check whether the docstrings conform to the Google style, and it does not generate docstring content based on the code in the file. Those features would require more complex code and possibly additional libraries.

### Logging configuration

Sure, here are basic implementations of logger.py and utils.py. Note that these are simplified examples and will need to be expanded to cover all the requirements you mentioned earlier.

The Logger class in logger.py uses the logging module to log messages to a text file and the console. It has a log method that logs a message at a specified log level.

The utils.py file contains two utility functions. scan_directory returns a list of all Python files in a directory, including those in subdirectories. backup_file creates a backup of a file by copying it to a new file with the same name but an additional .bak extension. These functions could be used in the main.py script to find the Python files to process and create backups before making any changes.

### `Main.py` - Create

Certainly, here's a simplified main.py that demonstrates how you might use the classes from the doc_oct package. This script scans a directory, reads each Python file, checks if it has a docstring, and if not, adds a generic docstring.
Note that this script does not handle some of the more advanced requirements you mentioned, such as updating existing docstrings, generating docstring content based on the code, or providing a dry-run option, interactive mode, or a way to ignore certain files. You would need to add more code and possibly modify the classes in the doc_oct package to implement those features.

### Dry Run Example

A dry run option would allow the program to simulate its operations without making any actual changes. This can be useful for testing or for previewing the results. Here's how you might create a DryRunWriter class in a new dry_run.py file:

The DryRunWriter class has the same interface as the DocstringWriter class, so it can be used in the same way in the main.py script. However, instead of actually writing the docstring to the file, it just logs what it would do.

Here's how you might modify the main.py script to use the DryRunWriter class:

In this version of the script, the main function takes an additional dry_run argument. If dry_run is True, the script uses a DryRunWriter instead of a DocstringWriter, and it doesn't create any backups. When you run the script, you can pass dry_run=True to simulate the operations without making any changes.
