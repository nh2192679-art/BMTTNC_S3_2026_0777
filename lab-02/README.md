# LAB-02: Caesar Cipher Flask API

## Project Structure

```
lab-02/
└── ex01/
    ├── api.py
    ├── requirements.txt
    ├── postman_collection.json
    └── cipher/
        ├── __init__.py
        └── caesar/
            ├── __init__.py
            ├── alphabet.py
            └── caesar_cipher.py
```

## Description

This project implements a **Caesar Cipher encryption and decryption API** using Flask.

## Features

- **Encrypt**: Convert plaintext to ciphertext using Caesar cipher
- **Decrypt**: Convert ciphertext back to plaintext
- **REST API**: POST endpoints for encryption and decryption
- **Postman Collection**: Ready-to-use API testing collection

## Installation

Navigate to the project directory:

```bash
cd lab-02/ex01
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Start the Flask server:

```bash
python api.py
```

The API will be available at `http://127.0.0.1:5000`

### API Endpoints

#### Encrypt

```bash
POST /api/caesar/encrypt
Content-Type: application/json

{
  "plain_text": "HUTECH",
  "key": 3
}
```

**Response:**
```json
{
  "encrypted_message": "KXWHFK"
}
```

#### Decrypt

```bash
POST /api/caesar/decrypt
Content-Type: application/json

{
  "cipher_text": "KXWHFK",
  "key": 3
}
```

**Response:**
```json
{
  "decrypted_message": "HUTECH"
}
```

## Testing

Import `postman_collection.json` into Postman for easy API testing.

## Author

Student ID: 0777
