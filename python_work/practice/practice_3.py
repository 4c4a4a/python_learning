#3-4
guests = ['LT', 'ZH', 'LJJ']
message1 = f"Dear {guests[0]}, {guests[1]} and {guests[2]}, I'd like to invite you to come to my dinner."
print(message1)
#3-5
print(f"{guests[1]} is busy.")
guests.remove('ZH')
guests.append('TSL')
message2 = f"Dear {guests[0]}, {guests[1]} and {guests[2]}, I'd like to invite you to come to my dinner."
print(message2)
#3-6
print("I find another big table.")
guests.insert(0, 'LXC')
guests.insert(2, 'DL')
guests.append('CRY')
message3 = f"Dear {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]} and {guests[5]}, I'd like to invite you to come to my dinner."
print(message3)
#3-7
print("Sorry, I can only invite two guests to my dinner.")
guests1 = guests.pop()
print(f"Sorry, {guests1}, I cant invite you.")
guests.pop()
guests.pop()
guests.pop()
print(f"Dear {guests[0]}, you are still be invited by me.")
del guests[0]
del guests[0]
print(guests)
#3-8
spots = ['shanghai', 'beijing', 'hunan', 'guangdong', 'japan']
print(spots)
print(sorted(spots))
print(spots)
print(sorted(spots, reverse=True))
print(spots)
spots.reverse()
print(spots)
spots.reverse()
print(spots)
spots.sort()
print(spots)
spots.sort(reverse=True)
print(spots)
#3-9
print(f"I have invited {len(spots)} guests to my dinner.")



