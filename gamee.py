print("Welcome to the quize game show\n\n")

print(">press 7 to start the game..!!\n\n")

i=int(input(">To quite press 0\n>"))

if i == 7:
    print("Here the game starts:\n\n")
elif i == 0:
    print("Exiting from the game.")
else:
    print("You have entered an invalid input.")



sum = 0;
 
if i == 7:
    ans1=input("1.What is the capital of France?\na. Rome\nb. Berlin\nc. Paris\nd. Madrid\n>")
    if ans1 == 'c':
        point1=5
        print("you have got = ",point1, " points")
        sum+=point1;
        print("Your total score is = ",sum,"points\n")
    else:
        point01=0
        print("you have got = ",point01," points")
        print("Your total score is = ",sum,"points\n")
    ans2=input("2.Which planet is known as the 'Red Planet'?\na. Venus\nb. Mars\nc. Jupiter\nd. Saturn\n>")
    if ans2 == 'b':
        point2=5
        print("you have got = ",point2," points")
        sum+=point2;
        print("Your total score is = ",sum)
    else:
        point02=0
        print("you have got = ",point02," points")
        print("Your total score is = ",sum,"points\n")
    ans3=input("3.Who wrote the play 'Romeo and Juliet'?\na. Charles Dickens\nb. William Shakespeare\nc. Jane Austen\nd. Mark Twain\n>")
    if ans3=='b':
        point3=5
        print("you have got = ",point3," points\n")
        sum+=point3;
        print("Your total score is = ",sum,"points\n")
    else:
        point03=0
        print("you have got = ",point03," points")
        print("Your total score is = ",sum,"points\n")
    ans4=input("4.What is the largest mammal on Earth?\na. Elephant\nb. Blue Whale\nc. Giraffe\nd. Gorilla\n>")
    if ans4=='b':
        point4=5
        print("you have got = ",point4," points\n")
        sum+=point4;
        print("Your total score is = ",sum)
    else:
        point04=0
        print("7.you have got = "+ str(point04)+ " points")
        print("Your total score is = ",sum,"points\n")
    ans5=input("5.In which year did the first manned moon landing occur?\na. 1969\nb. 1975\nc. 1982\nd. 1990\n>")
    if ans5=='a':
        point5=5
        print("you have got = ",point5," points")
        sum+=point5;
        print("Your total score is = ",sum)
    else:
        point05=0
        print("you have got = ",point05," points")
        print("Your total score is = ",sum,"points\n")
    ans6=input("6.What is the powerhouse of the cell?\na. Nucleus\nb. Ribosome\nc. Mitochondria\nd. Endoplasmic reticulum\n>")
    if ans6==  'c':
        point6=5
        print("you have got = ",point6," points")
        sum+=point6;
        print("Your total score is = ",sum)
    else:
        point06=0
        print("you have got = ",point06," points")
        print("Your total score is = "+ str(sum)+"points\n")
    ans7=input("7.Who painted the Mona Lisa?va. Vincent van Gogh\nb. Leonardo da Vinci\nc. Pablo Picasso\nd. Michelangelo\n>")
    if ans7=='b':
        point7=5
        print("you have got = ",point7," points")
        sum+=point7;
        print("Your total score is = ",sum)
    else:
        point07=0
        print("you have got = ",point07," points")
        print("Your total score is = ",sum,"points\n")
    ans8=input("8.Which element has the chemical symbol 'O'?\na. Oxygen\nb. Gold \nc. Silver\nd. Iron\n>")
    if ans8==  'a':
        point8=5
        print("you have got = ",point8," points")
        sum+=point8;
        print("Your total score is = ",sum)
    else:
        point08=0
        print("you have got = ",point08," points")
        print("Your total score is = ",sum,"points\n")
    ans9=input("9.What is the capital of Japan?\na. Seoul\nb. Tokyo\nc. Beijing\nd. Bangkok\n>")
    if ans9=='b':
        point9=5
        print("you have got = ",point9," points")
        sum+=point9;
        print("Your total score is = ",sum)
    else:
        point09=0
        print("you have got = ",point09," points")
        print("Your total score is = ",sum,"points\n")
    ans10=input("10.Which programming language is often used for web development?\na. Java\nb. Python\nc. HTML\nd. Ruby\n>")
    if ans10=='c':
        point10=5
        print("you have got = ",point10, " points")
        sum+=point10;
        print("Your total score is = ",sum)
    else:
        point010=0
        print("you have got = ",point010," points")
        print("Your total score is = ",sum,"points\n")

   
    print("you got ",sum,"out of 50(",sum,"/ 50)")
    print("Thank you for you perticipation.")
