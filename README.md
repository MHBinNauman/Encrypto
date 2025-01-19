# RSA and Caesar Cipher Encryption/Decryption

#### Demo Video:  [RSA and Caesar Cipher Demo](https://example.com)

## Description:

This project demonstrates the implementation of **RSA encryption/decryption** and **Caesar Cipher** techniques, two well-known cryptographic methods. It provides a **web-based interface** where users can input plaintext, apply these encryption/decryption algorithms, and view the results. The project aims to showcase the principles of both **public-key cryptography** (RSA) and **symmetric-key cryptography** (Caesar Cipher).

Key features include:
- **RSA Encryption and Decryption**: 
  - Users can encrypt and decrypt messages using RSA with automatic **key generation**.
  - Public and private keys are securely managed for encryption/decryption operations.
  
- **Caesar Cipher Encryption and Decryption**:
  - A customizable Caesar Cipher that allows users to set a **shift value** to encrypt and decrypt messages.
  
- **Web Interface**:
  - An intuitive and user-friendly web interface for **inputting plaintext** and **viewing results**.
  - Supports real-time encryption and decryption with **error handling** to validate inputs.

- **Error Handling & Input Validation**:
  - Robust error handling for incorrect inputs, ensuring smooth user experience with informative feedback.

- **Security**: 
  - The project uses modern cryptographic libraries and algorithms to ensure secure and efficient operations.

## Technologies Used:

- **Python**: For implementing the cryptographic algorithms.
- **Flask**: The web framework for serving the user interface and handling server-side logic.
- **HTML/CSS**: For building the web interface.
  
## Features:

- **RSA Encryption**:
  - Automatically generates public and private keys.
  - Encrypts and decrypts text based on the RSA algorithm using large prime numbers.

- **Caesar Cipher**:
  - Encrypts and decrypts messages using a customizable shift value.
  - Demonstrates simple substitution cipher, useful for understanding symmetric-key encryption.

- **Web Interface**:
  - **Text input fields** for plaintext and encrypted text.
  - **Buttons** for encrypting and decrypting text.
  - **Displays results** of the encryption/decryption, including generated keys and messages.

## How It Works:

1. **RSA Encryption**:
   - **Public Key** (`e`, `n`) is used for encryption, while the **Private Key** (`d`, `n`) is used for decryption.
   - Encryption: `ciphertext = plaintext^e mod n`
   - Decryption: `plaintext = ciphertext^d mod n`

2. **Caesar Cipher**:
   - Each character in the plaintext is shifted by a specified value (shift value).
   - Encryption: `ciphertext = (plaintext + shift) % 26`
   - Decryption: `plaintext = (ciphertext - shift) % 26`

## How to Use:

1. **RSA Encryption**:
   - Input plaintext in the provided text box.
   - Click **Encrypt** to generate the **public key** and **private key**.
   - View the encrypted message.

2. **RSA Decryption**:
   - After encryption, input the **private key** (comma-separated values).
   - Click **Decrypt** to view the original plaintext.

3. **Caesar Cipher Encryption**:
   - Enter the plaintext and choose a **shift value**.
   - Click **Encrypt** to see the encrypted message.

4. **Caesar Cipher Decryption**:
   - After encryption, input the **same shift value**.
   - Click **Decrypt** to retrieve the original plaintext.

## Project Structure:

- **`app.py`**: The core file running the Flask application. It handles the routes and logic for encrypting and decrypting messages using RSA and Caesar Cipher algorithms.
- **`Encryption_Decryption_Modules.py`**: Contains the implementation of the cryptographic algorithms for RSA and Caesar Cipher, including key generation, encryption, and decryption methods.
- **`templates/RSA.html`**: HTML template used to render the web interface, including input fields for encryption and decryption operations.
- **`static/style.css`**: CSS file for styling the web interface to improve the user experience.
- **`requirements.txt`**: List of required Python packages and dependencies, which can be installed using `pip install -r requirements.txt`.


