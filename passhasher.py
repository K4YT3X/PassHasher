#!/usr/bin/env python3
import binascii
import getpass
import hashlib


class PassHasher:

	def __init__(self):
		pass

	def get_password(self):
		print('Recruiting new password')
		pass1 = getpass.getpass(prompt='Enter Password:')
		pass2 = getpass.getpass(prompt='Confirm Password: ')
		if pass1 != pass2:
			raise Exception('Passwords don\t match')
		return pass1

	def ntlm(self, plaintext):
		hash = hashlib.new('md4', plaintext.encode('utf-16le')).digest()
		return binascii.hexlify(hash).decode('utf-8')

	def sha1(self, plaintext):
		print('Hashing using SHA1')
		return hashlib.sha1(plaintext.encode('utf-8')).hexdigest()

	def sha224(self, plaintext):
		print('Hashing using SHA224')
		return hashlib.sha224(plaintext.encode('utf-8')).hexdigest()

	def sha256(self, plaintext):
		print('Hashing using SHA256')
		return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()

	def sha384(self, plaintext):
		print('Hashing using SHA384')
		return hashlib.sha384(plaintext.encode('utf-8')).hexdigest()

	def sha512(self, plaintext):
		print('Hashing using SHA512')
		return hashlib.sha512(plaintext.encode('utf-8')).hexdigest()


hasher = PassHasher()
print(hasher.ntlm(hasher.get_password()))

# while True:
# 	exec(input('>>> '))
