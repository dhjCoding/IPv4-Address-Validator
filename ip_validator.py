"""
ip_validator.py

A simple and robust IPv4 address validator.

This module provides a function to validate if a given string conforms to the
standards of a valid IPv4 address, adhering to common requirements like
octet range, format, and absence of leading zeros.
"""

def is_valid_ipv4(ip_address: str) -> bool:
    """
    Validates if a given string is a valid IPv4 address.

    An IPv4 address is considered valid if:
    1. It consists of four decimal numbers (octets) separated by dots.
    2. Each octet is an integer between 0 and 255, inclusive.
    3. No octet has leading zeros (e.g., '01' is invalid, but '0' is valid).
    4. There are no empty octets between dots or at the start/end.

    Args:
        ip_address (str): The string to be validated as an IPv4 address.

    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """
    if not isinstance(ip_address, str):
        # Professional practice: Raise TypeError for incorrect input type
        # rather than returning False, as it's an API misuse.
        raise TypeError("Input 'ip_address' must be a string.")

    # Remove any leading/trailing whitespace which would make it invalid
    ip_address = ip_address.strip()

    octets = ip_address.split('.')

    # Check if there are exactly four octets
    if len(octets) != 4:
        return False

    for octet in octets:
        # Check for empty octets (e.g., "192.168..1" or ".1.1.1.1" or "1.1.1.1.")
        if not octet:
            return False

        # Check for leading zeros (e.g., '01' is invalid, '0' is valid)
        if len(octet) > 1 and octet[0] == '0':
            return False

        # Check if the octet is a valid number and within range (0-255)
        try:
            num = int(octet)
            if not (0 <= num <= 255):
                return False
        except ValueError:
            # If conversion to int fails, it's not a valid number (e.g., "abc")
            return False

    return True

# --- Example Usage (for demonstration and basic testing) ---
if __name__ == "__main__":
    print("--- IPv4 Address Validation Examples ---")
    print("This section demonstrates the functionality of the is_valid_ipv4 function.\n")

    test_ips = [
        # Valid IPv4 Addresses
        ("192.168.1.1", True),
        ("0.0.0.0", True),
        ("255.255.255.255", True),
        ("10.0.0.1", True),
        ("127.0.0.1", True), # Loopback address
        ("1.1.1.1", True),

        # Invalid IPv4 Addresses
        ("192.168.1", False),           # Too few octets
        ("192.168.1.1.1", False),       # Too many octets
        ("256.0.0.0", False),           # Octet out of range (too high)
        ("-1.0.0.0", False),            # Octet out of range (too low)
        ("192.168.01.1", False),        # Leading zero in octet
        ("192.168..1", False),          # Empty octet
        ("abc.def.ghi.jkl", False),     # Non-numeric octets
        ("192.168.1.", False),          # Trailing dot/empty octet
        (".1.1.1.1", False),            # Leading dot/empty octet
        ("123.456.789.0", False),       # Multiple octets out of range
        ("1.2.3.4 ", False),            # Trailing space
        (" 1.2.3.4", False),            # Leading space
        ("1.2.3. 4", False),            # Internal space
        ("", False),                    # Empty string
        (" ", False),                   # Whitespace string
        ("  192.168.1.1  ", False)      # Spaces around valid IP (stripped, then invalid)
    ]

    for ip_str, expected_result in test_ips:
        try:
            actual_result = is_valid_ipv4(ip_str)
            status = "PASS" if actual_result == expected_result else "FAIL"
            print(f"Test '{ip_str}' (Expected: {expected_result}, Actual: {actual_result}) -> {status}")
        except TypeError as e:
            # Catch TypeErrors for non-string inputs
            if ip_str is None or not isinstance(ip_str, str): # Check explicitly for non-string types
                print(f"Test '{ip_str}' (Expected: TypeError, Actual: {e}) -> PASS (Correctly raised TypeError)")
            else:
                print(f"Test '{ip_str}' (Unexpected Error: {e}) -> FAIL")
        except Exception as e:
            print(f"Test '{ip_str}' (Unexpected Exception: {e}) -> FAIL")

    print("\n--- Additional Type Error Tests ---")
    # These will trigger the TypeError due to incorrect input type
    non_string_inputs = [
        (None, False),
        (123456789, False),
        (["1.1.1.1"], False),
        ({"ip": "1.1.1.1"}, False),
    ]

    for ip_str, expected_result in non_string_inputs:
        try:
            is_valid_ipv4(ip_str)
            print(f"Test '{ip_str}' (Expected TypeError, Actual: No Error) -> FAIL")
        except TypeError as e:
            print(f"Test '{ip_str}' (Expected TypeError, Actual: {e}) -> PASS (Correctly raised TypeError)")
        except Exception as e:
            print(f"Test '{ip_str}' (Unexpected Exception: {e}) -> FAIL")
