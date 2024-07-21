# Data Types / Object Types 

-Numbers : 1234, 3+4j, 3.14, 01b2232, Decimal(), Fractional() 

- Strings : 'span' , 'Bob's', b'a\x01c', u'sp\xc4m'

- List : [1,[2,"string",3],4, 5.6] , list(range(10))

- Tuple : (1,2,"string"), tuple('span'), namedtuple()

- Dictionary : {'food': "Aloo Paratha", 'rup' : "68" } , dict(hours=10)

- Set : set("abc") set( 'a','b','c')

- files : open("file_Name.txt") open(r'c://home/file.bin', "wb")

- Boolen : True , False 

- None : None

- functiom, module, Classes 
- Advanced Pthon - Decorators, Genarators, iterators, MetaPrograming 

# Basic Methods()
- slice() :-
    - ex:- chai = "Masala_chai" -- Chai.slice[0] = M, chai.slice[0:4] = Masa ,chai.slice[0:6:2] = Msl (jumps on 2 char ) 
- strip() :-
    - ex:- chai = "   Masala_chai   " -- chai.strip() = 'Masala_chai' ( This method will remove the spaces from string. )
- replace() :-
    - ex:- chai.replace("Masala", "Ginger") = 'Ginger_chai'
- split() :-
    - ex:- chai =  "lemon, Masala, ginger, Mint" 
        - chai.split() = [ "lemon," , "Masala, " , "ginger, " , "Mint," ] --  If we use the split function without argument then this will print with comma "," by removing the space.
        - chai.split(",") -- ['lemon', ' Masala', ' ginger', ' Mint'] this will print string to list without comma ",".
- Find() :- 
    - chai = "Masala chai"  
    print(chai.find("chai")) -- 7 ( starting position of chai word).
- count() :- 
    - chai = "Masala chai chai chai" 
    print(chai.count("chai)) -- 3 ( this will check the dupliactes words in string.)
- Format() :-
    - chai_variety = "Masala chai"  
    quantity = 2  
    order = "I ordered {} cups of {}" 
    order.format(quantity,chai_variety)  
    ands:- 'I ordered 2 cups of Masala chai'
- Join() :- 
    - chai = chai = ["lemon" , "masala", "mint" ,  "ginger" ]
    print("".join(chai)) = lemonmasalamintginger  
    print(" ".join(chai)) = lemon masala mint ginger  
    This works for strings also:=  
    chai = "lemon masala mint ginger"  
    print("".join(chai))  
    lemon masala mint ginger  
    print(" ".join(chai))  
    l e m o n   m a s a l a   m i n t   g i n g e r

- if user want to print the string with double quotes then use \ in the initial of the sentence.
    - ex:- "He said, \"Masala chai is awesome" "  
    output :- he said, "Masala chai is awesome".    

- Row String() :- 
    - ex:- use "r" at te initial of string to convert that string to row string 
    path = r"c:\user\desktop"  
    print(path)  
    output = c:\user\desktop




    
