import subprocess

# Executes the espeak command in the shell
def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

print("** TTS (TEXT TO SPEECH) - espeak ** \n")
while True:
    print("Insert the text: (0 to quit)")
    a = input("-> ")
    if a == "0":
        print("Program closed.")
        break
    
    # tts using espeak
    c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
    execute_unix(c)

    # create wav file
    # w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
    # execute_unix(w)

