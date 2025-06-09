
# IPv4 Address Validator (Python)

A lightweight and robust Python module for validating IPv4 addresses according to standard specifications.

## 🌟 Features

* **Strict Validation:** Ensures compliance with IPv4 octet ranges (0-255), correct number of octets, and dot separators.
* **Leading Zero Handling:** Correctly identifies invalid IP addresses with leading zeros (e.g., `192.168.01.1` is invalid, but `192.168.0.1` is valid).
* **Whitespace Robustness:** Strips leading/trailing whitespace before validation.
* **Clear Error Handling:** Raises `TypeError` for non-string inputs, adhering to professional Python API design.
* **Simple API:** A single, easy-to-use function.

## 🚀 Installation

No installation is needed! Simply download the `ip_validator.py` file and place it in your project directory.

## 🛠️ Usage

### 1. Import the function

```python
from ip_validator import is_valid_ipv4
