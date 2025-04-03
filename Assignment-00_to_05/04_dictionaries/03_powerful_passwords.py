import hashlib

def hash_password(password):
 return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
def login(email , password):
 if email in stored_logins:
  return stored_logins[email] == hash_password[password]
 return False

if __name__ == "__main__":
 email = input("Enter your email: ")
 password = input("Enter your password: ")

 if login(email,password):
  print("Login successful")
 else:
  print("Invalid email or password")
    
  