destination = input("")
distance = float(input("Distance in kilometers: "))
average_speed = float(input("Average speed in km/h: "))

print(f"Destination: {destination}")
print(f"Distance: {distance } km")
print(f"Average Speed: {average_speed} km/h\n")

print(f"Estimated Travel Time:{int(distance/average_speed)} hours")


