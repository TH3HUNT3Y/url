import re

def is_valid_url(url):
    # Regular expression to match a valid URL
    pattern = r'^(http|https|ftp|ftps)://[a-zA-Z0-9-.]+\.[a-zA-Z]{2,3}(/\S*)?$'

    # Check if the given URL matches the pattern
    match = re.match(pattern, url)

    # Return True if the URL is valid, False otherwise
    if match:
        return True
    else:
        return False

# Open the text file containing the URLs
with open("urls.txt", "r") as file:
    # Read each line in the file
    for line in file:
        # Strip leading/trailing whitespace and newline characters
        url = line.strip()

        # Print the result of the is_valid_url() function
        print(f"{url}: {is_valid_url(url)}")
