from textnode import *
import os
import shutil
import block


"""
    The purpose of this function is to recursively copy the
    contents of the source directory into the destination
    directory
"""


def recursive_copy(source: str, destination: str):
    everything_in_src = list(os.scandir(source))

    for item in everything_in_src:
        if item.is_file():
            shutil.copy(item.path, destination)
        elif item.is_dir():
            new_folder_path = f"{destination}/{item.name}"
            os.mkdir(new_folder_path)
            recursive_copy(f"{source}/{item.name}", new_folder_path)


"""
    The purpose of this function is to recursively delete
    objects in a directory.
"""


def recursive_delete(dest: str):
    # Delete all files in the destination directory
    everything_in_dest = list(os.scandir(dest))

    for item in everything_in_dest:
        if item.is_file():
            os.remove(item)
        elif item.is_dir():
            recursive_delete(item)
            os.rmdir(item)


"""
    The purpose of this function is to copy all the files
    from the source directory to the destination directory.
    All files in the destination directory are deleted
    before copying files from source directory.
"""


def directory_hard_copy(source: str, destination: str):
    # Delete all the files in the destination directory
    recursive_delete(destination)

    # Recursively copy everything from the source directory
    recursive_copy(source, destination)


"""
    This function is used to extract the title from
    and input markdown file.
"""


def extract_title(first_line: str) -> str:
    title = first_line.removeprefix("# ")
    return f"{title.strip()}"


"""
    This function is used to generate a page out of a markdown
    file into a viewable page on a browser using template.html.
"""


def generate(from_path: str, template_path: str, dest_path: str):
    print(f"""
Generating page from {from_path} to {dest_path} using {template_path}
""")

    # Storage for markdown and template lines
    lines_markdown = []
    lines_template = []
    with open(from_path, 'r') as markdown:
        lines_markdown = markdown.readlines()

    with open(template_path, 'r') as template:
        lines_template = template.readlines()

    # Convert the markdown into html
    converted_markdown = block.markdown_to_html_node(
        '\n'.join(lines_markdown)
    )
    converted_markdown = converted_markdown.to_html()

    # Extract the title
    title = extract_title(lines_markdown[0])

    # Replace Title and Content template variables in template.html
    lines_template = "\n".join(lines_template)
    lines_template = lines_template.replace(
        "{{ Title }}",
        title
    )
    lines_template = lines_template.replace(
        "{{ Content }}",
        converted_markdown
    )

    # Copy the contents of lines_template into public/index.html
    with open(dest_path, "w") as destination:
        destination.write(lines_template)


"""
    This function will recursively generate html pages and place them
    in their appropriate directories.

    dir_path_content - Path to content folder
    template_path - Where to get template
    test_dir_path - place to store generated html
"""


def generate_pages_recursively(
    dir_path_content: str,
    template_path: str,
    dest_dir_path: str
):
    print(f"DIRCTORY PATH CONTENT: {dir_path_content}")
    print(f"DESTINATION DIRECTORY PATH: {dest_dir_path}")
    # First we need to check if content exists
    if os.path.exists(dir_path_content) is False:
        raise FileNotFoundError("Content directory does not exist!")

    # Create an iterator to contain the content directory
    content_dir = os.scandir(dir_path_content)

    # Iterate through the iterator recursively
    for item in content_dir:
        # Get the item's path
        path = item.path

        # Get the item's relative path
        path = path.split(dir_path_content)[1]

        # TO DO: check for empty content folder

        # Build the destination path
        dest_path = dest_dir_path + path

        # Recurse if the object is a directory
        if item.is_dir():
            # Make the directory in destination
            print(f"MAKING DIRECTORY: {dest_path}")
            os.mkdir(dest_path)

            # Recurse through the folder
            generate_pages_recursively(
                f"{dir_path_content}{path}",
                template_path,
                dest_path
            )
        elif item.is_file():
            """
                If the item is a file, the generated html page
                will have to be generated in the current
                directory.
            """

            # replace .md with .html in the file's path
            dest_path = dest_path.replace(".md", ".html")
            print(f"generating file: {dest_path}")
            generate(item.path, template_path, dest_path)


def main():
    directory_hard_copy("static", "public")
    generate_pages_recursively(
        "content/",
        "template.html",
        "public/"
    )


main()
