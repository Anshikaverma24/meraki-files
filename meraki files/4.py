# Question 4

# Iss text ko question3.txt ke naam ki file mein save karo. Iss file mein dhyaan se
# dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai
# jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo: 1. Delhi mein rehne 
# waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye.
# 2.Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam 
# "shimla.txt" hona chaiye 3. Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag 
# file mein daale. Iss file ka naam "others.txt" hona chaiye

# Aapko aisa code likhna hai, jo aisi file mein kitni bhi lines pe chal paye.


file=open("question3.txt","w")
delhi=open("delhi.txt","r")
name=input("Enter name")
city=input("Enter city")
if city =="delhi":
    delhi=open("delhi.txt","a")
    s=delhi.write(name)
elif city=="shimla":
    shimla=open("shimla.txt","a")
else:
    print(name,city)