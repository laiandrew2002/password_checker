import requests
import hashlib
import sys

def request_api_data(query_char):
  url = "https://api.pwnedpasswords.com/range/" + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f"Error fetching: {res.status_code},")
  return res


def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(":") for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0
  

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
  first_5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first_5_char)
  count = get_password_leaks_count(response, tail)
  return count


def main(argv):
  for filePath in argv:
    with open(filePath, mode="r") as file:
      passwords = file.readlines()
      for password_text in passwords:
        password = password_text.rstrip("\n")
        count = pwned_api_check(password)
        if count:
          print(f"{password} was seen {count} times. Please do not use this password.")
        else:
          print(f"{password} was not seen, it's safe to use!")
  return "password check done!"

if __name__ == "__main__":
  # please enter the file path/file name after executing the script
  # Example: python3 password_checker.py password.txt
  sys.exit(main(sys.argv[1:]))