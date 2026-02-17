#  Caesar Cipher Tool

A simple and interactive Python program that encrypts and decrypts text using the classic Caesar Cipher technique. The program shifts the letters of your message by a specified amount to create a secret code.

##  Overview
The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

This program allows you to:
1.  **Encode** a message (shift letters forward).
2.  **Decode** a message (shift letters backward to reveal the original text).

##  Features
- **Dual Functionality:** Supports both encryption (`encode`) and decryption (`decode`).
- **Character Preservation:** Symbols, numbers, and spaces are kept as-is; only letters are shifted.
- **Continuous Execution:** The program runs in a loop, allowing you to process multiple messages without restarting the script.
- **Input Handling:** Automatically handles upper/lower case inputs for the direction and message.

##  How to Run
### Prerequisites
- You must have **Python 3** installed on your system.

### Steps
1.  Save the code in a file named `main.py` (or any name you prefer).
2.  Open your terminal or command prompt.
3.  Navigate to the folder where you saved the file.
4.  Run the command:
    ```bash
    python main.py
    ```

##  Usage Guide
When you run the program, follow these prompts:

1.  **Select Mode:**
    - Type `encode` to encrypt a message.
    - Type `decode` to decrypt a message.
2.  **Enter Message:**
    - Type the text you want to process.
3.  **Enter Shift:**
    - Type the number of positions you want to shift the letters.
4.  **Continue or Exit:**
    - When asked `Do you want to continue the program:`, type `yes` to go again or `no` to exit.

##  Example Output

```text
welcome
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here is the encoded result: mjqqt btwqi
Do you want to continue the program:
yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
Here is the decoded result: hello world
Do you want to continue the program:
no
exiting