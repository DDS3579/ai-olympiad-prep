# WAP to check if a list contains a palindrom of elements

list1 = [1, 'abv','abv', 1]
if (list1 == list1[::-1]):
    print("Palindrom list")
else:
    print("not palindrome")

    # WAP TO ASK USE TO ENTER NAME OF 3 FAV MOVIES IN LIST
favMovies = []
favMovies.append(str(input("Enter you favourite movie: ")))
favMovies.append(str(input("Enter you favourite movie: ")))
favMovies.append(str(input("Enter you favourite movie: ")))
print(favMovies)