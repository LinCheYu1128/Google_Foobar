import base64
from itertools import cycle

encryption_key      = 'jonathan871128'
encrypted_message   = 'EUgdFBcLBB1LEBELEh8NHQsAAE9NTh9UXl1eXQsIGwRTSFtOH1JCRVddBwoKRlhIRgteUV5DRktN\nT1RBUwEPDUpSVVhQVA9IQkFTCQIGUVJHVF9dBBtJQU5IRhtWW15SWV0OSEJBUxoADFpeRUIVGFBP\nSRIVDgRJFBcWV11XTU9UQVMfCAAZEEw='

def decrypt(encrypted_message, encryption_key):
    base64_decoded              = base64.b64decode(encrypted_message)
    decrypted_message           = [''] * len(base64_decoded)
    encryption_key_iterator     = cycle(encryption_key)
    for i, c in enumerate(base64_decoded):
        decrypted_message[i] += chr(ord(c) ^ ord(encryption_key_iterator.next()))
    return ''.join(decrypted_message)

decrypted_message = decrypt(encrypted_message, encryption_key)
print(decrypted_message)
"""<encrypted>b'EUgdFBcLBB1LEBELEh8NHQsAAE9NTh9UXl1eXQsIGwRTSFtOH1JCRVddBwoKRlhIRgteUV5DRktN\nT1RBUwEPDUpSVVhQVA9IQkFTCQIGUVJHVF9dBBtJQU5IRhtWW15SWV0OSEJBUxoADFpeRUIVGFBP\nSRIVDgRJFBcWV11XTU9UQVMfCAAZEEw='</encrypted>"""