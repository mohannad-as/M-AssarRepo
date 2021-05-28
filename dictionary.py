import json

def main():
    
 jfile=open('dict_json.json','r')
 translator=json.load(jfile)
 while(1):
   state=input("Choose 'u' for Translator and 'd' for Developer and 'e' to exit : ")
 
   if state == 'e':
     break
   elif state == 'u' :
     user(translator)
     break
   elif state == 'd' : 
     develpoer(translator)
     break 
   else :
     print("Please Enter 'e or 'd' or 'u' !!  ")
 
def user(translator) :
    result=''
    while(1):
        result = input("Enter An English Word: !|write exit to end|!")
        if result=='exit':
           break
        print(translator[result])
def develpoer(translator):
    while(1):
        En= input("Enter The ENglish word : !|write exit to end|!")
        if En == 'exit' :
              break
        Ar = input ("Enter The Arabic  Word:")
    translator[En]=Ar
    file = open ("dict_json.json",'w')
    json.dump(translator,file)

    
main()