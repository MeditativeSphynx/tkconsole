import pickle
import hashlib

import yaml
from faker import Faker


def generate_fake_data():
    f = Faker()
    hash_data = list()
    hashes = list()

    for _ in range(0, 100):
        fake_password = f.password()
        pwd_hash = hashlib.md5(fake_password.encode()).hexdigest()
        hash_data.append(f'{pwd_hash}:{fake_password}')
        hashes.append(pwd_hash)
