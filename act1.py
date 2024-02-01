from cryptography.fernet import Fernet

d = Fernet(b'm7xHfFq2wV3k2KytB0LEM4uHA8LuUmYNBuhnJc7kdTU=')
print("MENSAJE: ", d.decrypt(b'gAAAAABluw65Ecz8hr3FUSZp8Os92bsSWJnaRLmDby10fGGh_Ye2n2Kf8VQpHftm8UjiCmAPF9ZSoY_NJD--yu7xZ4q5H9kA1w=='))
