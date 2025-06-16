def get_word_count(text):
  return len(text.split())

def get_character_counts(text):
  char_dict = {}

  for char in text:
    char = char.lower()
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  
  return char_dict

def character_dict_to_list(dict):
  char_list = []
  
  for key in dict:
    if key.isalpha():
      char_list.append({"char": key, "num": dict[key]})

  char_list.sort(reverse=True, key=sort_on)
  return char_list

def sort_on(dict):
  return dict["num"]