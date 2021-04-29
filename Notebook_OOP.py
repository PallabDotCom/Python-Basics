'''Square Function'''
def compute_square_area(side_length):
    return pow(side_length,2)

result=compute_square_area(int(input("length of square: ")))
print(result)


'''Square Class'''
class Square:
    def __int__(self ,side_length):
        self.side_length =side_length

    def compute_square_area(self):
        return pow(self.side_length ,2)

if __name__== "__main__":
    Small_square = Square(2)
    print(Small_square.compute_square_area())

    Mid_square = Square(15)
    print(Mid_square.compute_square_area())

    Big_square = Square(100)
    print(Big_square.compute_square_area())

'''Email Class'''

class Email:
    def __init__(self, to, subject, body):
        self.to = to
        self.subject = subject
        self.body = body

    def send(self):
        print(f"sending email with subject: {self.subject} and body: {self.body} and to: {self.to}")


if __name__ == "__main__":
    greeting_email = Email("Raja@google.com", "Hey", "Hi,How are you?")
    greeting_email.send()

'''Email Class changes'''
class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

    def send(self,to):
        print(f"sending email with subject: {self.subject} and body: {self.body} and to: {to}")


if __name__ == "__main__":
    greeting_email = Email("Hey", "Hi,How are you?")
    greeting_email.subject="Greeting"
    greeting_email.send("Tony@sepora.ca")
    greeting_email.send("Amaya@walmart.ca")



'''Notebook - Most common magic methods'''
Most frequently used magic methods:



Addition (+): __add__(self, other)



Subtraction (-): __sub__(self, other)



Multiplication (*): __mul__(self, other)



Floor division (//): __floordiv__(self, other)



True division (/): __truediv__(self, other)



Modulo (%): __mod__(self, other)



Power (**): __pow__(self, other)



Less than (<): __lt__(self, other)



Greater than (>): __gt__(self, other)



Less than or equal (<=): __le__(self, other)



Greater than or equal(>=): __ge__(self, other)



Equals (==): __eq__(self, other)

Not equals (!=): __ne__(self, other)