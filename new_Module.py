from stringcolor import cs 
""" not work in window """

# mini code to handle using the module stringcolor

def print_color(string , color="red"):
    print(cs(string , color))
    print(cs("Hello, World!", "cyan"))
    
color = input('your color: ')
text = input('your text: ')

print_color(text , color=color)    

