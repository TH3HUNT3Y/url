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

# Example usage
print(is_valid_url("http://www.example.com")) # prints True
print(is_valid_url("example.com")) # prints False