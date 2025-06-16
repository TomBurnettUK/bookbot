import sys
from stats import get_word_count, get_character_counts, character_dict_to_list

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  text = get_book_text(filepath)
  
  char_counts = get_character_counts(text)
  char_count_list = character_dict_to_list(char_counts)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {get_word_count(text)} total words")
  print("--------- Character Count -------")
  
  for item in char_count_list:
    print(f"{item["char"]}: {item["num"]}")

  print("============= END ===============")

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
main()

