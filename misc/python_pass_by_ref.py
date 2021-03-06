# the code snippet is adapted from http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
#  The program is to verify whether python method is pass by value or by reference. 

def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list

outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after outer_list.append() inside the method, outer_list =', outer_list

def try_to_change_list_reference(the_list):
    print 'got', the_list
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print 'set to', the_list

outer_list = ['we', 'like', 'proper', 'English']

print 'before, outer_list =', outer_list
try_to_change_list_reference(outer_list)
print 'after try_to_change_list_reference(), outer_list =', outer_list

def try_to_change_string_reference(the_string):
    print 'got', the_string
    the_string = 'In a kingdom by the sea'
    print 'set to', the_string

outer_string = 'It was many and many a year ago'

print 'before, outer_string =', outer_string
try_to_change_string_reference(outer_string)
print 'after, outer_string =', outer_string

def try_to_change_string_letters(the_string):
    print 'got', the_string
    the_string = 'In a kingdom by the sea'
    print "python strings are immutable!!! There is no way to modify one letter in string. The only way is to return a new string"

outer_string = 'It was many and many a year ago'

print 'before, outer_string =', outer_string
try_to_change_string_reference(outer_string)
print 'after, outer_string =', outer_string
