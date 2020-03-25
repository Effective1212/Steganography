# Steganography
My Steganography script


There is much to needed to improve this script but it can decrypt encrypt in my custom way with max limit and unique save because I couldn't figure out how...
Used crypting algorithms

MD5 AES
Requirements

(Python 2.7)

OpenCV 2 Image hashlib sys getpass Cyripto
How it works

To encrypt user user enters key and message wanted to hide and image path. Key goes throug MD5 hash in order to become fixed size that AES encription accepts. Message gets added spases to fit the AES as well since it takes fixed size bits as password and message.

The image gets transformes into PNG format no matter the original state.

After this process we have a AES hash and lenght of the chars is calculated and writen into images last pixels colors to help me decrypt it later. Since I am using only one pixels color hash can not be longer than 765.

The hash characters are turn into decimal values and those values into binary values. Each binary value is writen into the image as closest color values to odd or even way. 1 for odd 0 for even.

The image is saved with .png extention no matter what since other formats (as far as I know) does not support or keep some color values.

To decrypt user enters the path of the image. The last pixels color is read and determined the lenght of the hash that is writen in the image (if there is) bu even there isn't anything in it, script will extract a binary code and turn it into decimal and character depending on the last pixels color values.

After that user enters key and that again goes through MD5 and to AES. If the extracted hash is right it will give proper outpu if not it will give error and stop.
To Do

Optimize the script Improve input and output methods from user Add proper explantion into script Expand max limit Improve method of crypting Write more detailed "How it works section"
