# When working with strings, another common task is to remove a prefix.
# Consider a URL with the common prefix https://. We want to remove this prefix,
# so we can focus on just the part of the URL that users need to enter into an address bar.
# Here’s how to do that:

nostarch_url = "https://nostarch.com"

# Enter the name of the variable followed by a dot, and then the method removeprefix().
# Inside the parentheses, enter the prefix you want to remove from the original string.
print(nostarch_url.removeprefix("https://"))


