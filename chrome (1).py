
import  serial                                      
import  pyautogui                                   
Ard_Ser=serial.Serial('com3',9600)                
while 1:
    inp=str(Ard_Ser.readline())                  
    print(inp)                                      
     
    if 'next' in inp:                               
        pyautogui.hotkey('ctrl', 'pgdn')            
        
    if 'previous' in inp:                           
        pyautogui.hotkey('ctrl', 'pgup')            

    if 'down' in inp:                               
        pyautogui.press('down')                     
        pyautogui.scroll(-100) 
         
    if 'up' in inp:                                 
        pyautogui.press('up')                       
        pyautogui.scroll(100)
        
    if 'change' in inp:                              
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
    inp = "";                                       
