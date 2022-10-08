import googletrans as gt
import termcolor as tc 
import sys

def translate(text,lang='en'):
    try:
        trans = gt.Translator()
        src = trans.detect(text).lang
        result = trans.translate(text,src=src,dest=lang)
        print(tc.colored(f'[+] Translated Text : {result.text}','green'))
    except:
        print(tc.colored("[x] Error while Translation !!!",'red'))
    
def take_input():
    try:
        if  len(sys.argv) < 2 :
            inp = input(tc.colored('[*] Enter the Text to Translate : ','green'))
        else:
            if (len(sys.argv[1].split('.')) <= 3) and ( 'txt' in sys.argv[1].split('.')):
                with open(sys.argv[1], encoding = 'utf-8') as f:
                    inp = f.read()
                    inp = inp.replace("\n","  ")
                    print(inp)
            else:
                inp = str(sys.argv[1])
            
        dest_lang = input(tc.colored('[*] Enter a Language in which you want to Convert : ','yellow')).lower()
        dest_code = None
        for i,j in gt.LANGUAGES.items():
            if j == dest_lang:
                dest_code = i
                break
    except:
        print(tc.colored("[x] Error While taking input ",'red'))
    
    try:
        translate(text=inp,lang=dest_code)
    except:
        print(tc.colored("[x] Errored Input !!! ",'red'))

if __name__ == '__main__':
    take_input()
   
    
'''
Requirements :- 
    termcolor==1.1.0
    googletrans==4.0.0rc1


Usage :-
    1. pip install {Requirements}
    
    2. run the file 

'''
