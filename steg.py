#!/usr/bin/env python

from PIL import Image
import cv2
from Crypto.Cipher import AES
import hashlib
import getpass
import sys

def encryp():

	print("Starting Encrypion")
	key = raw_input("Enter key : ")
	message = raw_input("Enter message you want to encrypt : ")

	if len(message) % 16 != 0 :
		new_message = len(message) + ( 16 -  (len(message) % 16))
		message = message.ljust(new_message)

	binary = []
	key = hashlib.md5(key)
	k = key.hexdigest()
	cipher = AES.new(k)
	encrypted_data = cipher.encrypt(message)
	encrypted_data = encrypted_data.encode('hex')
	for i in range(len(encrypted_data)):
		a1 = encrypted_data[i]
		b1 = ord(a1)
	 	d1 = format(b1, '08b')
		binary.append(d1)
	#print(binary)
	writeHash(binary)


def writeHash(binary):

	path = raw_input("Enter full path pf the image: ")

	path = str(path)

	print("Writing Hash Into the Image")

	joined = ''.join(binary)

	count = 0
	aa = len(joined)
	img = Image.open(path)
	img.save(path+".png")
	lastImage = cv2.imread(path+".png")

	if aa == 255:
		lastImage[-1][-1][2] = 255
		lastImage[-1][-1][1] = 0
		lastImage[-1][-1][0] = 0

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa == (255 * 2):
		lastImage[-1][-1][2] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][0] = 0

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa == (255 * 3):
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa == (255 * 4):
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 255
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0

	elif aa == (255 * 5):
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 255
		lastImage[-1][-2][1] = 255
		lastImage[-1][-2][2] = 0


	elif aa == (255 * 6):
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 255
		lastImage[-1][-2][1] = 255
		lastImage[-1][-2][2] = 255


	elif aa < 255 :
		lastImage[-1][-1][0] = aa - 255
		lastImage[-1][-1][1] = 0
		lastImage[-1][-1][2] = 0

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa < (255 * 2) :
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = aa - (255 * 2)
		lastImage[-1][-1][2] = 0

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa < (255 * 3 ):
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = aa - (255 * 3 )

		lastImage[-1][-2][0] = 0
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa < (255 * 4) :
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] =  255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = aa - 255
		lastImage[-1][-2][1] = 0
		lastImage[-1][-2][2] = 0


	elif aa < (255 * 5) :
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 255
		lastImage[-1][-2][1] = aa - 255
		lastImage[-1][-2][2] = 0


	elif aa < (255 * 6) :
		lastImage[-1][-1][0] = 255
		lastImage[-1][-1][1] = 255
		lastImage[-1][-1][2] = 255

		lastImage[-1][-2][0] = 255
		lastImage[-1][-2][1] = 255
		lastImage[-1][-2][2] = aa - (255 * 6 )


	elif aa > (255 * 6):
		print("Message is too big")
		sys.exit()


	for i in range(len(lastImage)):
		for j in range(len(lastImage[i])):
			for x in range(len(lastImage[i][j])):

				if count == len(joined):
					cv2.imwrite(path+'.png', lastImage)
					#print(lastImage[0][0])
					return
				if  ( int(lastImage[i][j][x]) % 2) == 0 and ( int(joined[count]) % 2) == 0:
					pass
				if ( int(lastImage[i][j][x]) % 2) != 0 and ( int(joined[count]) % 2) != 0:
					pass
				if ( int(lastImage[i][j][x]) % 2) == 0 and ( int(joined[count]) % 2) != 0:
					#if lastImage[i][j][x] == 0:
					lastImage[i][j][x] += 1
					#else:
						# lastImage[i][j][x] -= 1
				if ( int(lastImage[i][j][x]) % 2) != 0 and ( int(joined[count]) % 2) == 0:
					#if lastImage[i][j][x] == 255:
					lastImage[i][j][x] -= 1
					#else:
						#lastImage[i][j][x] -=1
					
				count += 1

def decrypt():
	print("Decrypting")

	path = raw_input("Enter full path of image : ")
	path = str(path)
	img = cv2.imread(path)
	binary = ""
	list = []



	"""
	lenght = img[-1][-1][2]
	if lenght == 255:
		a = img[-1][-1][1]
		a = int(a)
		lenght += a
	if img[-1][-1][1] == 255:
		b = img[-1][-1][0]
		b = int(b)
		lenght += b
	"""
	lenght = 0
	lenght = int(img[-1][-1][0])
	lenght += int(img[-1][-1][1])

	lenght += int(img[-1][-1][2])

	lenght += int(img[-1][-2][0])
	lenght += int(img[-1][-2][1])
	lenght += int(img[-1][-2][2])
	#print(lenght)
	count = 0

	for i in range(len(img)):
	    for j in range(len(img[i])):
	        for x in range(len(img[i][j])):
	            if count == lenght:
	                break
	            count += 1
	            if img[i][j][x] % 2 == 0:
	                binary = binary+"0"
	            elif img[i][j][x] % 2 != 0:
	                binary = binary+"1"

	#print(binary)

	a = 8
	b = 0
	for i in range(len(binary) / 8):
	    list.append(binary[b:a])
	    b = a
	    a += 8

	liste = []

	for i in range(len(list)):
		a = str(list[i])
		doc = int(a, 2)
		char = chr(doc)
		liste.append(char)

	word = ""
	word = ''.join(liste)

	password = getpass.getpass("Enter password : ")
	password = str(password)
	deneme = word.decode('hex')
	key = hashlib.md5(password)
	k = key.hexdigest()
	cipher = AES.new(k)
	dencrypted_data = cipher.decrypt(deneme)
	print(dencrypted_data)

option = input("Decrypt (0) or Encryp (1): ")
if option == 0:
	decrypt()
if option == 1:
	encryp()
