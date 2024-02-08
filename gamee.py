print("Welcome to the quize game show\n\n")

print(">press 7 to start the game..!!\n\n")

i=int(input(">To quite press 0\n>"))

if i == 7:
    print("Here the game starts:\n\n")
elif i == 0:
    print("Exiting from the game.")
else:
    print("You have entered an invalid input.")


 
if i == 7:
    ans1=input("1.What is the capital of France?\na. Rome\nb. Berlin\nc. Paris\nd. Madrid\n>")
    if ans1 == 'c':
        point1=5
        print("you have got = "+str(point1)+ " points\n")
    else:
        point01=0
        print("you have got = "+str(point01)+ " points\n")
    ans2=input("2.Which planet is known as the 'Red Planet'?\na. Venus\nb. Mars\nc. Jupiter\nd. Saturn\n>")
    if ans2 == 'b':
        point2=5
        print("you have got = "+str(point2)+ " points\n")
    else:
        point02=0
        print("you have got = "+str(point02)+ " points\n")
    ans3=input("3.Who wrote the play 'Romeo and Juliet'?\na. Charles Dickens\nb. William Shakespeare\nc. Jane Austen\nd. Mark Twain\n>")
    if ans3=='b':
        point3=5
        print("you have got = "+str(point3)+ " points\n")
    else:
        point03=0
        print("you have got = "+str(point03)+ " points\n")
    ans4=input("4.What is the largest mammal on Earth?\na. Elephant\nb. Blue Whale\nc. Giraffe\nd. Gorilla\n>")
    if ans4=='b':
        point4=5
        print("you have got = "+ str(point3)+ " points\n")
    else:
        point04=0
        print("7.you have got = "+ str(point04)+ " points\n")
    ans5=input("5.In which year did the first manned moon landing occur?\na. 1969\nb. 1975\nc. 1982\nd. 1990\n>")
    if ans5=='a':
        point5=5
        print("you have got = "+ str(point5) + " points\n")
    else:
        point05=0
        print("you have got = "+ str(point05) + " points\n")
    ans6=input("6.What is the powerhouse of the cell?\na. Nucleus\nb. Ribosome\nc. Mitochondria\nd. Endoplasmic reticulum\n>")
    if ans6==  'c':
        point6=5
        print("you have got = "+str(point6)+ " points\n")
    else:
        point06=0
        print("you have got = "+str(point06)+ " points\n")
    ans7=input("7.Who painted the Mona Lisa?va. Vincent van Gogh\nb. Leonardo da Vinci\nc. Pablo Picasso\nd. Michelangelo\n>")
    if ans7=='b':
        point7=5
        print("you have got = "+str(point7)+ " points\n")
    else:
        point07=0
        print("you have got = "+str(point07)+ " points\n")
    ans8=input("8.Which element has the chemical symbol 'O'?\na. Oxygen\nb. Gold \nc. Silver\nd. Iron\n>")
    if ans8==  'a':
        point8=5
        print("you have got = "+str(point8)+ " points\n")
    else:
        point08=0
        print("you have got = "+str(point08)+ " points\n")
    ans9=input("9.What is the capital of Japan?\na. Seoul\nb. Tokyo\nc. Beijing\nd. Bangkok\n>")
    if ans9=='b':
        point9=5
        print("you have got = "+str(point9+ " points\n"))
    else:
        point09=0
        print("you have got = "+str(point09)+ " points\n")
    ans10=input("10.Which programming language is often used for web development?\na. Java\nb. Python\nc. HTML\nd. Ruby\n>")
    if ans10=='c':
        point10=5
        print("you have got = "+str(point010)+ " points\n")
    else:
        point010=0
        print("you have got = "+str(point010)+ " points\n")

        print("Thank you for you perticipation.")


