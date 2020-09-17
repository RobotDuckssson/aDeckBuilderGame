
confused = True
months = ["February", "March", "April", "May", "June", "July", "August", "September"]
confusedQuota = 100
noLongerConfused = ""

for m in months:
    confusedQuota -= 33
    if confusedQuota == 1:
        confused = False
        noLongerConfused = m

print("No longer confused since "+ noLongerConfused)