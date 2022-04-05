import random

def get_question(n, t):
  return a[n][t]

a = [[0 for i in range(2)] for i in range(10)]

a[0][0] = ["Which sport is also known as football?","Soccer","BasketBall","BaseBall","Cricket ","Soccer"]
a[0][1] = ["How many continents are there?","1","3","7","20","7"]

a[1][0] = ["Which state has cities named San Francisco and Hollywood?","California","Utah","Hawaii","Montana","California"]
a[1][1] = ["Which product Tesla produce?","Ice cream","Televisions","Hair brushes","Electric cars","Electric cars"]

a[2][0] = ["What gas makes voices sound higher when inhaled?","Oxygen","Nitrogen","Sulfur Hexafluoride","Helium","Helium"]
a[2][1] = ["What American holiday falls on july 4?","Thanksgiving Day","Independence Day","Christmas Day","New Years Day","Independence Day"]

a[3][0] = ["Which candy bar shares its name with galaxy?","Snickers","3 Musketeers","Milky Way","Almond Joy","Milky Way"]
a[3][1] = ["What is the capital of Englad?","London","Washinton D.C","Rome","Moscow","London"]

a[4][0] = ["Which one of the following is not an ivy league Unvirsity?","Harvard","Princeton","Columbia","Hogwarts","Hogwarts"]
a[4][1] = ["What video game system does sony produce?","Xbox","Atari","Game Boy","PlayStation","PlayStation"]

a[5][0] = ["What is the name of the Super mario bors?","Tim and Eric","Batman and Robin","Sonic and Tails","Mario and Luigi","Mario and Luigi"]
a[5][1] = ["Which princess lost a glass slipper?","Posh Snow White","Cinderella","Mulan","Belle","Cinderella"]

a[6][0] = ["Which American car company makes Mustang cars?","Ford","Toyota","Volkswagen","Nissan","Ford"]
a[6][1] = ["Which pop culutre franchise has characters names Luke Skywalker and Darth Vader?","Harry Potter","Star Wars","Star Trek","James Bond","Star Wars"]

a[7][0] = ["how many moons does jupiter have?","16","79","23","54","79"]
a[7][1] = ["Name of the first man to set foot on the moon?","Neil Armstrong","Loren Acton","James Adamson","Viktor M. Afanasyev","Neil Armstrong"]

a[8][0] = ["What is the closest galaxy to ours ?","Whirilpool Galaxy","Andromeda Galaxy","Sombrero Galaxy","Black Eye Galaxy","Andromeda Galaxy"]
a[8][1] = ["What year was Nintendo founded?","1900","1919","1889","1856","1889"]

a[9][0] = ["What is the number of countries in Africa?","50","48","41","54","54"]
a[9][1] = ["Who was the first man to travel into space twice?","Vladimir Titov","Michael Collins","Gus Grissom","Yuri Gagarin","Gus Grissom"]



balance = [0, 100, 500, 1000, 5000, 32000, 64000, 125000, 250000,500000, 1000000, ]
level = 0   
correct_answer = ""
q = []
acceptable_answers = ["a", "b", "c", "d", "50","audience", "friend", "finish"]
help_50_avail = True
help_friend_avail = True
help_audience_avail = True

print (" Welcome to Who wants to b e a Millionare \n")
player = input(" What is your name? ")

print ("\n Lets start! there are 10 questions you have to answer all of them correctly to win 1 million dollar \n you have 3 life lines \n type 50 to elimante 2 wrong answers \n type friend to request help from a friend \n and type audience to request audience help \n") 
      
 
def ask_question(Qlevel):
  qnum = int (random.random() * 2)
  global q
  q = get_question(Qlevel, qnum)
  to_return = q[0]
  to_return += "\n A. " + q[1] 
  to_return += "\n B. " + q[2] 
  to_return += "\n C. " + q[3]
  to_return += "\n D. " + q[4]
  global correct_answer
  correct_answer = q[5]
  return to_return


def check_answer(Qlevel):
  answer = input("\n Your Answer is : ")
  global correct_answer, q, help_friend_avail, help_50_avail, help_audience_avail
  if not (answer in acceptable_answers): 
    print ("Enter a valid answer.")
    check_answer(Qlevel)
  
#//////////////////////////////////////////////////// Call Friend //////////////////////////////////////////////////
  elif (answer == "friend"):
    if (help_friend_avail == True):
      help_friend_avail = False
      if (random.random() < 0.7): 
        
        print ("\n Your friend believes the right answer is " + correct_answer)
        check_answer(Qlevel)
    else:
      print ("\n You have already used this lifeline. ")
      check_answer(Qlevel)

#//////////////////////////////////////////////////// 50:50 Answer //////////////////////////////////////////////////
        
  elif (answer == "50"):
    if (help_50_avail == True):
      help_50_avail = False
      w = 0 
      while True:
        if w == 2:
          break
        i = int (random.random()*4 + 1)
        if (correct_answer != q[i] and q[i] != ""):
          w += 1
          q[i] = ""

      print ("\n we have removed two wrong answers:")
      temp = [" A. ", " B. ", " C. ", " D. "]
      for i in range(1,5):
        if (q[i] != ""):
          print (temp[i-1] + q[i] ),
      print ("")
      check_answer(Qlevel)
      
    else:
      print ("\n You already used this lifeline.")
      check_answer(Qlevel)

#//////////////////////////////////////////////////// Audience //////////////////////////////////////////////////    

  elif (answer == "audience"):
    if (help_audience_avail == True):
      help_audience_avail = False
      while True: 
        w = random.random()
        if (w > 0.40):
          w = int (w*100)
          break

      if (random.random() < 0.8):
        audience_answer = correct_answer

      print ("\n The majority (%s%%) of the audience think that the correct answer is %s" % (w, audience_answer))
      check_answer(Qlevel)
    else:
      print ("\n You already used this lifeline.")
      check_answer(Qlevel)

  elif (answer == "finish"):
    print ("\n you chose to end the "+player+". You won $%s. Congratulations!" % (balance[Qlevel]))
    quit()

  elif (answer == "a" or answer == "b" or answer == "c" or answer == "d"):
    if (correct_answer == q[ord(answer)-96]):
      if (Qlevel == 9):
        print("Congrats!,"+ player+ " you have won 1 Million dollar!" ) 
      else:
        print("\n you got the answer right, "+player+"!\n now you have $%s.\n Lets go to the next question \n" % (balance[Qlevel+1]))
        print (ask_question(Qlevel+1))
        check_answer(Qlevel+1)
      
    else:
      print("\n your answer was incorrect.\n The right answer is " + correct_answer)
      print(" Thank you for playing the game!")

      user_choice = input("\n\n Would you like to to try again? (y/n)  ")
      if (user_choice == "y" or user_choice=="Y"):
        help_audience_avail = True
        help_50_avail = True
        help_friend_avail = True
        print (ask_question(0))
        check_answer(0)

print (ask_question(0))
check_answer(0)
    


