import math

points = [(2,3),(4,7),(1,5),(8,6),(9,2)]

#Öklid -> d = √(x₂-x₁)²+(y₂-y₁)²
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)


distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)

#min num
minNum = min(distances)
print("Minimum distance: ",minNum)