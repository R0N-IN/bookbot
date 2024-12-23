def count_words(str_text):
    return len(str_text.split())

def count_chars(str_text):
    lowered_str_text = str_text.lower() 
    alphabet = {}

    for char in lowered_str_text: 
        try: 
            alphabet[char] += 1
        except:
            alphabet[char] = 1  
    histogram_list = []

    #Converts dictionary in a list of dictionaries 
    for key, value in alphabet.items(): 
        if key.isalpha():
            histogram_list.append({"char": key, "count" : value})
    return histogram_list    

def sort_on(dict):
    return dict["count"]

def print_report(words_count, char_count, book_name):
    print(f"--- Begin report of {book_name} ---") 
    print(f"{words_count} words found in the document\n")
    
    char_count.sort(reverse = True, key = sort_on)
    
    for item in char_count: 
        print (f"The '{item["char"]}' character was found {item["count"]} times")
    print("\n--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_words_count = count_words(file_contents)
    file_char_count = count_chars(file_contents)
    
    print_report(file_words_count,file_char_count,f.name)

main()
