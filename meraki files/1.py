# Question 1

# Iss text ko people1-exercise.txt ke naam ki file mein save karo. Ab apne code 
# se iss file ko kholo aur fir, uske saare contents ko print karo.

file_data = open("people1-exercise.txt","r")

file=file_data.read()

print (file)

file_data.close()


