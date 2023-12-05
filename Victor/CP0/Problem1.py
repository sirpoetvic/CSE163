# Write a program that counts down from a minute in decrements of 10 seconds using a for loop. 
# The output of the program, when hitting the Run button, should be the following:

def one_minute_countdown():
    print('One minute countdown')
    for i in range(60, -1, -10):
        print(i)
    print('Done!')
    
def main():
    one_minute_countdown()

if __name__ == '__main__':
    main()