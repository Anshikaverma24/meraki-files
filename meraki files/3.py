# Question 3

# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki 
# file mein nayi line mein daalo. Aapki list yeh rahi:

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

li=open("file-question3.txt","r")
file=li.read()
print(file)
li.close()