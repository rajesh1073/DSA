class stack:
    def __init__(self,size):
        self.stk=[None]*size
        self.size=size
        self.top=-1
        print("Stack is Ready!")
        return
    
    def push(self,ele):
        self.ele=ele
        if self.top==self.size-1:
            print("Stack is Full.!")
        else:
            self.top+=1
            self.stk[self.top]=ele
            print(f"{ele} Pushed.!")
        return
    
    def peek(self):
        if self.top==-1:
            print("Empty stack to display peek.!")
        else:
            print(f"Peek element is:{self.stk[self.top]}")
        return
    
    def allelements(self):
        if self.top==-1:
            print("There is no elements in the stack.!")
        else:
            print("Stack elements are: ")
            for i in range(self.top,-1,-1):
                print(self.stk[i])
        return   

    def pop(self):
        if self.top==-1:
            print("Empty stack.!")
        else:
            print(f"Popped element is: {self.stk[self.top]}")
            self.top-=1
        return


size=int(input("Enter the stack size: "))
stk=stack(size)


while True:
    print("1.push")
    print("2.pop")
    print('3.peek')
    print("4.showing all elements")
    print("5.exit")
    
    choice=int(input("Enter the choice: "))
    if choice==1:
        ele=int(input("enter the element: "))
        stk.push(ele)
    elif choice==2:
        stk.pop()
    elif choice==3:
        stk.peek()
    elif choice==4:
        stk.allelements()
    elif choice==5:
        print("Quit the Stack Operation.")
        break
else:
    print("Enter valid input.!")
    
        
        
        
        
        
        
        
        
        