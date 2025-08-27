def modify_content(content):
    """Modify the file content in some way.
    For example, convert text to uppercase."""
    return content.upper()


def main():
    try:
        # Ask user for input filename
        input_file = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified file saved as '{output_file}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
