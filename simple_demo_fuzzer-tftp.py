# simple fuzzer script to demonstrate network fuzzing, using python + tftp.
# Meant to be iterated upon. Used to teach basic network fuzzing using python. Lots of room for improvements. Ideally, one improvement at a time(i.e. De Bruijn sequence/pattern gen, recreate_packet function, error checking, etc)
# Goal is to be very clear in purpose and verbose


import socket
import sys


fuzzing_data = "A"
test_packet = "A"
test_data = "A"

# Create Packet Structure
# Make Packet header
def make_header():
	print("Please select a header option:(1 - 5)\n")
	print(" 1. x00x01\n 2. x00x02\n 3. x00x03\n 4. x00x04\n 5. x00x05\n 6. x00x06\n")
	print("Your selection: ")
	global header
	header = 0
	x = 0
	while x < 1:
		header_selection = raw_input()
		header_selection = int(header_selection)
		if isinstance(header_selection, int):
			if header_selection > 0 and header_selection < 7:
				x = x + 1
			else:
				print("Invalid Choice, Please Try Again.")

	if header_selection == 1:
		header = "\x00\x01"
	elif header_selection == 2:
		header = "\x00\x02"
	elif header_selection == 3:
		header = "\x00\x03"
	elif header_selection == 4:
		header = "\x00\x04"
	elif header_selection == 5:
		header = "\x00\x05"



# Create fuzzing data
# De Brujin sequence
def make_fuzzing_data():
	print("Create your fuzzing data")

	z = 0

	while (z < 1):
		print("Would you like the default? (100 As sequentially)")
		print("Your answer( y/n ): ")

		default_answer = raw_input()

		global fuzzing_data

		if  default_answer == "y":
			fuzzing_data = "A"*100
			default_yes = 1
			z = z + 1

		elif default_answer == "n":
			print("Select letter or sequence to be repeated: ")
			input1 = raw_input()
			z = z + 1
			print("How many times would you like it repeated? i.e. fuzz_string * $number")
			try:
				input2 = int(input("Enter a number to multiply the previously supplied number by: "))
			except ValueError:
				print("That's not a number. Please enter a proper number. An INTEGER.")

		elif default_answer != "y" or "n":
			print("Please enter either 'y' or 'n' \n")

	# Combine the data into the request packet
	try:
		input1
	except NameError:
		input1 = 100
		input2 = "A"
	fuzzing_data = input1 * input2

#	print(fuzzing_data)

def print_result():
	print("Fuzz data is currently {}".format(test_packet))

def recreate_packet():
	make_fuzzing_data()
	make_header()
	global test_data
	test_data = header + fuzzing_data
	print_result()
	make_socket()

def make_socket( packet_data ):
	# Get host
	print("Please Enter IP:\n")
	target = raw_input()
	
	# Get Port
	print("Please Enter Port:")
	target_port = int(raw_input())
	
	test_data = packet_data
	# Make Socket to send UDP Packet
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	except socket.error:
		print("Failed to make a socket")
	
	# Send it off
	s.sendto(test_data, (target, target_port))



make_fuzzing_data()
# print("\n"+fuzzing_data+"\n")
make_header()
test_data = header + fuzzing_data
# print(header, fuzzing_data)
# print(test_packet)
print_result()

make_socket(test_data)
print("Packet sent to target. Good Luck.")

