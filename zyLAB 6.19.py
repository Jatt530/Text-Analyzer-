# Type all other functions here
def main():
   usrStr= input("Enter a sample text:")
   print("You entered:", usrStr)
   print_menu(usrStr)   #calls print menu
   
   
def print_menu(usrStr):
   while True:             #Must loop this or else it will not print menu again when done
      menuOp = input('''MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option:
''')                   #This is where we call everything
      if menuOp== "c":
         get_num_of_non_WS_characters(usrStr)
      if menuOp== "w":
         get_num_of_words(usrStr)
      if menuOp== "f":
         fix_capitalization(usrStr)
      if menuOp== "r":
         replace_punctuation(usrStr)
      if menuOp== "s":
         shorten_space(usrStr)
      if menuOp== "q":         
         break        #if user hits q it will break out of loop and be done since everything else is a function
print()  #Newline


def get_num_of_non_WS_characters(usrStr):
   Amnt_whitespaces=0  #Whitespace counter
   for letters in usrStr:
      if (letters.isspace())==True:   #This is saying if there is white space it goes on
         Amnt_whitespaces= Amnt_whitespaces + 1
   non = (len(usrStr)-Amnt_whitespaces)  #Len of string - white spaces gives us non-white spaces
   print("Number of non-whitespace characters:", non)
   return non         #'return' allows these to be stored


def get_num_of_words(usrStr):
   num_words=len(usrStr.split())  #.split() splits string into a list then len counts how many entries in the list
   print("Number of words:", num_words)
   return num_words        #'return' allows these to be stored


def shorten_space(usrStr):
   short=" ".join(usrStr.split())   #I could not figure out how to do this part so I read up on stack overflow and it says that .split() splits string into a list (as we know) then .join puts everything back together with no white space.
   print("Edited text:", short)
   print()
   return short        #'return' allows these to be stored


def fix_capitalization(usrStr):
   letters_capitalized = 0
   new_string =""           #holds results
   punc_before = usrStr[0]  
   if usrStr[0].islower():   #if 1st character is lowercase 
      new_string= new_string + usrStr[0].upper() #makes 1st character capitalized
      letters_capitalized = letters_capitalized + 1 #therefore we add 1 to the capitalization counter
   for letter in usrStr[1:]:
      if letter.islower() and (punc_before=="!" or punc_before=="." or punc_before=="?" or punc_before == ""):   #if conitions not met it moves to else
         new_string+=letter.capitalize()   #if punctuations above come up the first letter of the word after will be capitalized
         letters_capitalized = letters_capitalized + 1 #adds to letters capitalized count
      else:
         new_string= new_string +letter    #goes here and adds "letter" to the new string if the above is not true 
      if letter != " ":                    #after going through either if or else it goes here and if letter isn't equal to space then punc_before gets redefined as letter
         punc_before = letter  
   print("Number of letters capitalized:", letters_capitalized, "\n")     
   print("Edited text:", new_string, "\n\n")
   return new_string,letters_capitalized   #'return' allows these to be stored


def replace_punctuation(usrStr,exclamationCount = 0, semicolonCount = 0):#if we put semicolons and exclamations below we would have to pass an arguement to them.
   for punc in usrStr:
      if punc == ";":
         semicolonCount= semicolonCount+1  #adds to count
         usrStr = usrStr.replace(";",",") #replaces everything in the string with ("0ld","new")
      if punc == "!":
         exclamationCount= exclamationCount+1  #adds to count
         usrStr= usrStr.replace("!",".") #replaces everything in the string with ("0ld","new")         
   print("Punctuation replaced")
   print("exclamationCount:", exclamationCount)
   print("semicolonCount:", semicolonCount)
   print("Edited text:", usrStr)
   return usrStr


if __name__ == '__main__':   #calls main function
   main()

   
