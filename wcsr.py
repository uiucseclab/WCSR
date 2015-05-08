import os
import sys




# KEY EXCHANGE MECHANISMS
KEM1 = "A key exchange (sometimes also referred to as a \"key establishment\") is the process of swapping cryptographic keys between two parties. This allows the use of a cryptographic algorithm. Key exchanges are necessary if parties want their communication to be done through encrypted messages. In order to do so, however, each must be equipped to encrypt messages to be sent and decrypt messages received. The way in which the communicators are \"equipped\" depends on the encryption technique used."

KEM2 = "The problem now is how to exchange the keys or other information needed such that no one else has a copy, as well as ensuring that a key received actually belongs to its supposed owner. This is where the various key exchange mechanisms come in."

KEM3 = "Some definitions to know beforehand:"

KEM4 = "RSA stands for Rivest, Shamir, and Adelman, the inventors of the technique (not that exciting, we know). The RSA algorithm is based on the difficulty of factoring large numbers into two prime numbers. Based on the product of two large prime numbers, two sets of numbers (the public and private keys) are developed."

KEM5 = "DSA stands for Digital Signature Algorithm. There are two phases for key generation: the first phase is a choice of algorithm parameters, and the second phase computes public and private keys for a single user."

KEM6 = "Diffie-Hellman (DH) key exchange method allows two parties that have no prior knowledge of each other to jointly establish a shared secret key over an insecure channel, which is then used to encrypt subsequent communications via a symmetric key cipher. Authentication is not supported."

KEM7 = "Ephemeral Diffie-Hellman uses temporary public keys, meaning each instance or run of the protocol uses a different public key. The temporariness of the public keys allows for Perfect Forward Secrecy, which means that a compromise of the server\'s long term signing key does NOT jeopardize the privacy of past sessions."

# Ratings
keyx = {"RSA":3, "DH_RSA":4, "DH_DSA":4, "DHE_RSA":5, "DHE_DSA":5, "ECDH_RSA":7, "ECDH_ECDSA":8, "ECDHE_RSA":9, "ECDHE_ECDSA":10, "none":0}

keyfact = {"RSA":"A random value chosen by the client is encrypted with the server public key. The server public key must be an RSA key and the server certificate must not prohibit encryption.", "DH_RSA":"A static Diffie-Hellman key exchange. The server public key must be a Diffie-Hellman key and the certificate issued by a Certification Authority that was using a RSA key.", "DH_DSA":"A static Diffie-Hellman key exchange. The server public key must be a Diffie-Hellman key and the certificate issued by a Certification Authority that was using a DSA key.", "DHE_RSA":"An ephemeral Diffie-Hellman key exchange. The server dynamically generates a DH public key and sends it to the client, and also signs what it sends. The server public key must be of type RSA, and its certificate appropriate for signatures.", "DHE_DSA":"An ephemeral Diffie-Hellman key exchange. The server dynamically generates a DH public key and sends it to the client, and also signs what it sends. The server public key must be of type DSA, and its certificate appropriate for signatures.", "ECDH_RSA":"An elliptic curve Diffie-Hellman key exchange. The server public key must be an elliptic curve Diffie-Hellman key, in a certificate issued by a Certification Authority that used a RSA key.", "ECDH_ECDSA":"An elliptic curve Diffie-Hellman key exchange. The server public key must be an elliptic curve Diffie-Hellman key, in a certificate issued by a Certification Authority that used an elliptic curve digital signature algorithm public key.", "ECDHE_RSA":"The server sends a dynamically generated elliptic curve Diffie-Hellman key and signs it with its own key (to be a RSA type). This is equivalent to the ephemeral Diffie-Hellman key exchange with a DSA-type server public key, but both the Diffie-Hellman part and the signature part are with elliptic curves.", "ECDHE_ECDSA":"The server sends a dynamically generated elliptic curve Diffie-Hellman key and signs it with its own key (to be elliptic curve digital signature algorithm type). This is equivalent to the ephemeral Diffie-Hellman key exchange with a DSA-type server public key, but both the Diffie-Hellman part and the signature part are with elliptic curves."}


# CONNECTION ENCRYPTION
CE = "Encryption schemes are used to encrypt plaintext using a pseudo-random encryption key, and output ciphertext that can only be read if decrypted. Encryption protects the confidentiality of a message, preventing unauthorized recipients from reading the message. There are two categories of Encryption schemes: symmetric key, where the encryption and decryption schemes are the same; and public key encryption, where the encryption key is publicly available, but the decryption key is private."

# Ratings
encrypt = {"AES_128_GCM":10, "AES_256_CBC":9, "AES_128_CBC":8, "RC4_128":7, "DES":1, "3DES": 2, "none":0}

encryptfact = {"AES_128_GCM":"Advanced Encryption Standard with Galois Counter Mode - a high performance encryption scheme, offering both pipelining and parallelization", "AES_256_CBC":"Advanced Encryption Standard with Cipher Block Chaining is a mode of operation for a block cipher, where a sequence of bits are encrypted as a single block with a cipher key applied to the entire block.", "AES_128_CBC":"AES-CBC is a mode of operation for a block cipher, where a sequence of bits are encrypted as a single block with a cipher key applied to the entire block. AES_128_CBC uses fewer bits than AES_256_CBC, which makes this scheme less secure.", "RC4_128":"Insecure due to its small key size", "DES":"AVOID (INSECURE) - DData Encryption Standard is a symmetric key encryption algorithm developed in the 1970\'s. It has become obsolete and insecure due to its small key size. It is not recommended for usage for protecting sensitive information, and doesn\'t provide adequate security level against modern threats.", "3DES": "LEGACY - Triple Data Encryption Standard is a symmetric key block cipher. Essentially, it applies the DES algorithm three times per data block. "}


# MESSAGE AUTHENTICATION
MA = "Message Authentication assures integrity and authenticity of a message. The algorithm accepts a secret key as input, and an arbitrary length message to be authenticated, and outputs a MAC value. The receiver of the message has the secret key as well, and is able to check the integrity and authenticity of the message by seeing if any changes were made to the message content."

# Ratings
msg = {"SHA-1":3, "SHA-256":8, "SHA-384":9, "SHA-512":10, "MD5":1, "HMAC-MD5":3, "HMAC-SHA-1":6, "none":0}

msgfact = {"SHA-1":"LEGACY", "SHA-256":"NGE (SECURE)", "SHA-384":"NGE (SECURE)", "SHA-512":"NGE (SECURE)", "MD5":"AVOID (INSECURE)", "HMAC-MD5":"LEGACY", "HMAC-SHA-1":"ACCEPTABLE"}


# CERTIFICATE AUTHORITIES
CA1 = "Digital certificates are issued by Certificate Authorities (CAs) who are trusted third parties that certify the ownership of a public key to the owner of the certificate. Certificates are typically used to make secure connections over the Internet. The client software uses the CA certificates to verify the CA signature on the server certificate before establishing a secure connection. This ensures that the public key contained in the certificate belongs to the entity described in the certificate."

CA2 = "There are over 650 certificate issuers that can be accepted by Microsoft\'s Internet Explorer and Mozilla\'s Firefox client software browsers. Having such a large variety of certificate authorities and certificate issuers could cause issues in the security and reliability of the certificates."

CA3 = "Best SSL Certificate Providers: VeriSign, GeoTrust, Comodo, DigiCert, Thawte, GoDaddy, Network Solutions"

CA4 = "Controversial Certificate Authorities: DigiNotar, VeriSign (hacked in 2011), Etisalat (Emirates Telecommunications Corporation)"




while(1):
	os.system('clear')
	print "Welcome!"

	print "Select a task"
	print "\t (1) Rate your connection"
	print "\t (2) Learn more"
	print "\t (3) Exit"

	main1 = raw_input("Your choice: ")



	# RATE YOUR CONNECTION
	if (main1 == "1"):
		os.system('clear')
		print "Rate your connection\n"
		print "Which key exchange mechanism does your connection use?"
		ki = 1
		for key in keyx:
			print "\t(" + str(ki) + ") " + key
			ki += 1
		yourkey = input("Your choice: ")
		print "\n"
		keyscore = keyx.values()[yourkey-1]


		print "Which encryption scheme does your connection use?"
		ei = 1
		for key in encrypt:
			print "\t(" + str(ei) + ") " + key
			ei += 1
		yourencrypt = input("Your choice: ")
		print "\n"
		encryptscore = encrypt.values()[yourencrypt-1]


		print "Which message authenticatoin does your connection use?"
		mi = 1
		for key in msg:
			print "\t(" + str(mi) + ") " + key
			mi += 1
		yourmsg = input("Your choice: ")
		print "\n"
		msgscore = msg.values()[yourmsg-1]
		

		totalscore = keyscore + encryptscore + msgscore
		print "Your connection security score is " + str(totalscore) + " out of 30"
		pause = raw_input()



	# LEARN MORE
	elif (main1 == "2"):
		while(1):
			os.system('clear')
			print "Learn more\n"
			print "What would you like to learn more about?"
			print "\t (1) Key Exchange Mechanisms"
			print "\t (2) Connection Encryption"
			print "\t (3) Message Authentication"
			print "\t (4) Certificate Authorities"
			print "\t (5) Return"

			learn1 = raw_input("You choice: ")

			if (learn1 == "1"):
				print KEM1 + "\n"
				print KEM2 + "\n"
				print KEM3 + "\n"
				print "\t" + KEM4 + "\n"
				print "\t" + KEM5 + "\n"
				print "\t" + KEM6 + "\n"
				print "\t" + KEM7 + "\n"
				while(1):
					print "Which would you like to learn more about?"
					ki = 1
					for key in keyfact:
						print "\t(" + str(ki) + ") " + key
						ki += 1
					print "\t(" + str(ki) + ") Return"
					yourkey = input("Your choice: ")

					if(yourkey == ki):
						break
					else:
						print keyfact.keys()[yourkey-1]
						print keyfact.values()[yourkey-1]
					pause = raw_input()
					os.system('clear')


			elif (learn1 == "2"):
				print CE + "\n"
				while(1):
					print "Which would you like to learn more about?"
					ei = 1
					for key in encryptfact:
						print "\t(" + str(ei) + ") " + key
						ei += 1
					print "\t(" + str(ei) + ") Return"
					yourencrypt = input("Your choice: ")

					if(yourencrypt == ei):
						break
					else:
						print encryptfact.keys()[yourencrypt-1]
						print encryptfact.values()[yourencrypt-1]
					pause = raw_input()
					os.system('clear')


			elif (learn1 == "3"):
				print MA + "\n"
				while(1):
					print "Which would you like to learn more about?"
					mi = 1
					for key in msgfact:
						print "\t(" + str(mi) + ") " + key
						mi += 1
					print "\t(" + str(mi) + ") Return"
					yourmsg = input("Your choice: ")

					if(yourmsg == mi):
						break
					else:
						print msgfact.keys()[yourmsg-1]
						print msgfact.values()[yourmsg-1]

					pause = raw_input()
					os.system('clear')
			elif (learn1 == "4"):
				print CA1 + "\n"
				print CA2 + "\n"
				print CA3 + "\n"
				print CA4 + "\n"
				pause = raw_input()
				os.system('clear')
			elif (learn1 == "5"):
				break
			else:
				"Try again"
				print "\n"
				pause = raw_input()
				os.system('clear')



	# EXIT
	elif (main1 == "3"):
		os.system('clear')
		print "Bye-bye!\n"
		break

	else:
		print "\n"
		print "Please try again."
		print "\n"
