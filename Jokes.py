import jokes

def tell_joke():
    # Fetch a random joke
    joke = jokes.get_joke()
    
    return joke

# Call the function and print the joke
print(tell_joke())
