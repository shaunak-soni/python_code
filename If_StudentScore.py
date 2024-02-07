#Find the Student rating based on the score entered by the user

score = int(input('Please Enter the Student Score to find the Rating: '))
if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'
    
print(rating)