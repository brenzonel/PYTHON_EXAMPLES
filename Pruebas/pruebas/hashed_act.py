import hashlib
import string
import random

#pwd cracking simulator
def simulate_password_cracking(hashed_pwd, pwd_list):
    for pwd in pwd_list:
        #pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()
        #if pwd_hash == hashed_pwd:
        #    return pwd
        if hashlib.sha256(pwd.encode()).hexdigest() == hashed_pwd:
            return f"Password found: {pwd}"
    return "Password not found"

#def of pwd to hash
def hash_pwd(pwd):
    hashed_pwd  = hashlib.sha256(pwd.encode()).hexdigest()
    return hashed_pwd

#pwd random
def gen_random_pwd(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(characters) for i in range(length))
    return pwd

#var 
random_pass = gen_random_pwd()
print("Random password: ", random_pass)

#var in hash manual
#str_val = hashlib.sha256(b'Cosasdepython').hexdigest()
#print(str_val)
#dd392f44600af8a5761c0496ad5665caa9d29fbd225820094a6f643127227bf0

#car in hash with def
#str_pwd = "mi_contra_perrillo"
hashed_str_pwd = hash_pwd(random_pass)
#print(random_pass)
print(hashed_str_pwd)

#example
#hashed_pwd_to_crack = 'dd392f44600af8a5761c0496ad5665caa9d29fbd225820094a6f643127227bf0'
hashed_pwd_to_crack = hashed_str_pwd
common_pwd = ['123456', 'password', 'qwerty', 'letmein', '12345678', 'hola', random_pass]

result = simulate_password_cracking(hashed_pwd_to_crack, common_pwd)
print(result)

