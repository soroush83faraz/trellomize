import bcrypt
import base64
import json

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Encode the hashed password to a Base64 string
    encoded_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
    return encoded_hashed_password

def save_hashed_password(encoded_hashed_password, filename='passwords.json'):
    data = {'hashed_password': encoded_hashed_password}
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_hashed_password(filename='passwords.json'):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data['hashed_password']

def check_password(password, encoded_hashed_password):
    # Decode the Base64 string to get the original hashed password
    hashed_password = base64.b64decode(encoded_hashed_password)
    # Verify the password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    password = "saeed@@2"
    encoded_hashed_password = hash_password(password)
    
    save_hashed_password(encoded_hashed_password)
    print(f"Encoded hashed password saved: {encoded_hashed_password}")

    loaded_encoded_hashed_password = load_hashed_password()
    print(f"Encoded hashed password loaded: {loaded_encoded_hashed_password}")

    entered_password = "saeed@@3"
    if check_password(entered_password, loaded_encoded_hashed_password):
        print("Password is correct!")
    else:
        print("Password is incorrect!")
