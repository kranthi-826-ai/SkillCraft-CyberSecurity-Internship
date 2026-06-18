def encrypt_decrypt_image(input_file, output_file, key):
    with open(input_file, "rb") as file:
        data = bytearray(file.read())

    for i in range(len(data)):
        data[i] ^= key

    with open(output_file, "wb") as file:
        file.write(data)

    print(f"Output saved as {output_file}")


print("=== Image Encryption Tool ===")

key = int(input("Enter Key (0-255): "))

encrypt_decrypt_image("photo.jpeg", "encrypted_photo.jpeg", key)

encrypt_decrypt_image("encrypted_photo.jpeg", "decrypted_photo.jpeg", key)

print("Encryption and Decryption Completed")
