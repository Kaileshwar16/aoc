# Open the file
f = open("input9.txt", "r")
lines = f.readlines()
f.close()

# 1. Read the tiles into a list
tiles = []
for line in lines:
    # Split "7,1" into ["7", "1"]
    parts = line.strip().split(',')
    
    # Convert to integers
    x = int(parts[0])
    y = int(parts[1])
    
    # Add to our list
    tiles.append([x, y])

max_area = 0

# 2. Check every pair using two loops
# i goes from the first item to the end
for i in range(len(tiles)):
    # j goes from the NEXT item to the end (avoids duplicates)
    for j in range(i + 1, len(tiles)):
        
        # Get the two tiles
        tile1 = tiles[i]
        tile2 = tiles[j]
        
        x1 = tile1[0]
        y1 = tile1[1]
        
        x2 = tile2[0]
        y2 = tile2[1]

        # Calculate width and height
        # abs() makes sure the number is positive
        # + 1 accounts for the grid (inclusive)
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        
        area = width * height
        
        if area > max_area:
            max_area = area

print("Largest area found:", max_area)
