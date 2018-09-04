#Variant Examples to Work through

#4.1: Parity, Complete in O(1) time

#Q1: Right propagate rightmost bit (0101000 > 01011111)
def right_prop(x):
    #we know x&x-1 will remove the lowest bit so we can use that here 
    #for the example x-1 = 0100111 so if we use an | bitwise operator we can get all the 1s from both
    return x|x-1

#Q2: Compute X mod a power of 2 "77 mod 64 = 13"
def mod_pow2(x, mod):
    '''x: input number
    mod: power of 2 to do modulus on'''
    #after doing some examples and research found that 77: 001001101 % 64:001000000 = 13: 001101
    #and then 77 % 8: 001000 = 5: 101 
    #mod power of 2 seems to truncate the input until after the input bit. 
    #to do this we use mod-1 to create 00111 for mod=8 and use an &
    return x&mod-1

#Q3: Test if x is a power of 2
def test_pow2(x):
    #For this to be true x needs to only have 1 bit value equal to 1. 
    #continuing use of x&x-1 removing the right most/lowest value bit. If we assume a powr of 2
    #x&x-1 will be 0 for only power of 2 numbers
    return x&x-1 == 0

#4.4 Closest Integer with the same weight

#Q1: Solve the example with Q(1) time and space. 
def closest_int_same_weight(x):
    #we want to swap the lowest value bit in constant time which means no loops. I know XOR is good at swaps.
    #if we use x&~(x-1) we can extract the lowest significant bit. 
    #Got stuck for a while so examine stack overflow. Primary find was formula for least non set bit: ~x&(x+1). 
    lns = lowest_notset(x)
    lsb  = LSB(x)
    if(lns > lsb): #Use lns and swap with the bit to the right. 
        ind = len(bin(lns))-2
        x^=(1<<ind)|(1<<(ind+1)) #based on epi formula which works on indices
    else: #other wise use lsb and swap with the bit to the left
        ind = len(bin(lsb))-2
        x^=(1<<ind)|(1<<(ind+1)) #based on epi formula which works on indices
    return x

#4.11 Rectangle Intersection

#Q1: Given 4 points in a plane how would you check if they are a rectangle. 

def is_rect(p1,p2,p3,p4)
    '''Assumes a point object with point.x and point.y designating the coordinates of the point
    
    Args:p1,p2,p3,p4 are point objects
    
    Returns: True or False if the points create a rectangle'''
    #The brute force method is to calculat distances between all the points


#Q2: Given 2 rectangles not necessarily aligned with X and Y how do you determin if there is an intersection. 

#assume Rect object of 4 points p1,p2,p3,p4 as defined by point objects above. 
def do_intersect(r1,r2):
    #brute force is make a bounded zone using lines from r1 and loop through the points in r2 to determine if they are inside r1. 
        
