# To ensure that no whitespace exists at the right side of a string, use the
# rstrip() method:
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())

favorite_language = favorite_language.rstrip()
print(favorite_language)

# You can also strip whitespace from the left side of a string using the
# lstrip() method, or from both sides at once using strip()
favorite_language = "  python "
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
print(favorite_language)
