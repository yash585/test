def encrypt(text,key):
  fi=""
  for a in text:
    a=a.upper()
    fi+=chr(((ord(a)+key-65)%26)+65)
  return fi
def decrypt(text,key):
  fi=""
  for a in text:
    a=a.upper()
    fi+=chr((ord(a)-key-65)%26+65)
  return fi

def exec(txt,k):
  c=int(input("choice::\nENCRYPT:0 DECRYPT:1\n::"))
  if c==0:
    int(c)
    f=encrypt(txt,k)
    print("Encrypted text:",f)
  elif c==1:
    int(c)
    f=decrypt(txt,k)
    print("Decrypted text:",f)
  else:
    print("Wrong choice\nEnter again:")
    exec(txt,k)

txt=input("Input the text ENCRYPTED/DECRYPTED::")
k=int(input("Enter key to ENCRYPT/DECRYPT:"))
k=k%26
exec(txt,k)
