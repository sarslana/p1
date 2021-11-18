#
#p_9. You are given a list of dates in the format Dec 11 and a month in the format Dec as arguments.
# Each date represents a video that was uploaded on that day. Return the number of uploads for a given month.

#Examples
#upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept") ➞ 2
#upload_count(["Sept 22", "Sept 21", "Oct 15"], "Oct") ➞ 1

my_list = ["Sept 22", "Sept 21", "Oct 15", "Dec 30", "Jan 20", "May 05"]
print(my_list)
new_list= "".join(my_list)
print([new_list])

def upload_count():
    i= new_list.count("Sept")
    print (i)
upload_count()


#new_list= {i:myList.count(i) for i in myList}
from collections import Counter
#return my_dict = dict(Counter(my_list))
#my_list.count()