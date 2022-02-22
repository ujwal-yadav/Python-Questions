import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real;
        self.imaginary=imaginary;
        
    def __add__(self, no):
        real=self.real+no.real;
        fr = "{:.2f}".format(real)
        img=self.imaginary+no.imaginary;
        fi= "{:.2f}".format(img)
        if float(fi)<0:
            s="%s%si" %(fr,fi)
        else:
            s="%s+%si" %(fr,fi)
        return s
       
    def __sub__(self, no):
        real=self.real-no.real;
        fr = "{:.2f}".format(real)
        img=self.imaginary-no.imaginary;
        fi= "{:.2f}".format(img)
        if float(fi)<0:
            s="%s%si" %(fr,fi)
        else:
            s="%s+%si" %(fr,fi)
        return s
        
    def __mul__(self, no):
        real=(self.real*no.real)-(self.imaginary*no.imaginary);
        fr = "{:.2f}".format(real)
        img=(self.imaginary*no.real)+(no.imaginary*self.real);
        fi= "{:.2f}".format(img)
        if float(fi)<0:
            s="%s%si" %(fr,fi)
        else:
            s="%s+%si" %(fr,fi)
        return s
        
    def __truediv__(self, no):
        deno=no.real**2+no.imaginary**2
        real=((self.real*no.real)+(self.imaginary*no.imaginary))/deno;
        fr = "{:.2f}".format(real)
        img=((self.imaginary*no.real)-(no.imaginary*self.real))/deno;
        fi= "{:.2f}".format(img)
        if float(fi)<0:
            s="%s%si" %(fr,fi)
        else:
            s="%s+%si" %(fr,fi)
        return s
    def mod(self):
        real=math.sqrt((self.real**2)+(self.imaginary**2));
        fr = "{:.2f}".format(real)
        img=(0);
        fi= "{:.2f}".format(img)
        s="%s+%si" %(fr,fi)
        return s
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
