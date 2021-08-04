import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def inputter():
    name=input("Enter the name of the excel sheet:")
    sheet=name+'.xlsx'
    return sheet

df=pd.read_excel(inputter())

Name=df['SYMBOL \n'].tolist()
Open=df['OPEN \n'].tolist()
High=df['HIGH \n'].tolist()
Low=df['LOW \n'].tolist()

n=len(Name)
threshold=float(input("Enter the level of accuracy of the threshold difference between values:"))


def buying(n,Open,Low,Name,threshold):
    for i in range(n):
        if abs(Open[i]-Low[i])<threshold:
            print("Buy",Name[i])
        else:
            continue
    x=Open
    y=Low
    plt.scatter(x,y)
    for j,label in enumerate(Name):
        plt.text(x[j],y[j],label)
    plt.xlabel("Opening prices")
    plt.ylabel("All day low prices")
    X=np.linspace(-5,5,100)
    Y=X
    plt.plot(X,Y,'-r',label='Equalising Line')
    plt.grid()
    plt.title("Buying stocks grid")
    plt.show()
    print("Use this graph to determine the location of each and every stock with its proximity to the equalising line")
    main()


def selling(n,Open,High,Name,threshold):
    for i in range(n):
        if abs(Open[i]-High[i])<threshold:
            print("Sell",Name[i])
        else:
            continue
    x=Open
    y=High
    plt.scatter(x,y)
    for j,label in enumerate(Name):
        plt.text(x[j],y[j],label)
    plt.xlabel("Opening prices")
    plt.ylabel("All day high prices")
    X=np.linspace(-5,5,100)
    Y=X
    plt.plot(X,Y,'-r',label='Equalising Line')
    plt.grid()
    plt.title("Selling stocks grid")
    plt.show()
    print("Use this graph to determine the location of each and every stock with its proximity to the equalising line")
    main()

def main():
          
    choice=input("""  WELCOME TO THE  INTRADAY ADVISORY PROGRAM  \n
    Choose an option for the task you want to do  \n     (1)View Buying Stocks Information  (2)View Selling Stocks Information (3)End""")
    if choice=='1':
        buying(n,Open,Low,Name,threshold)
    elif choice=='2':
        selling(n,Open,High,Name,threshold)
    elif choice=='3':
        print("Alright, thanks fo rusing this program, all the best for your endeavours in the stock market!")    
    else:
        print("Please enter 1 or 2 or 3")
        main()
    

main()
