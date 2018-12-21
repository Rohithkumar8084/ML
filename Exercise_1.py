# Create a class for a message queue
class queue :
  # implement the functions
  def pop(self):
    # pop the front of the queue
    pass

  def push(self, s):
    # insert element at the back of the queue
    pass

  def find(self, s):
    # returns the first element which s is a part of
    pass

  def find_all(self, s):
    # return a list of all the elements that s is a part of
    return []

  def find_last(self, s):
    # returns the last string that s is a part of
    pass
  
test_strings = ["aa", "Aaak", "abc", "auiuo", "tskta"]

def test_case1( q ):
  # this tests push, pop functions
  
  q.push(test_strings[0])
  q.push(test_strings[1])
  q.push("aBB")
  q.pop()
  q.push(test_strings[2])
  q.push("tst")
  q.pop()
  q.push(test_strings[3])
  q.push(test_strings[4])

  for msg in test_strings:
    if q.pop() != msg:
      return print("FAIL") 

  return print("SUCCESS")

def test_case2( q ):
  # this tests find
  for msg in test_strings:
    q.push( msg )

  q.pop()

  if q.find("bc") == "abc" :
    print("SUCCESS")
  else :
    print("FAIL")

  if len(q.find_all("t")) == 1 :
    print("SUCCESS")
  else :
    print("FAIL")

  if len(q.find_all("a")) == 5 :
    print("SUCCESS")
  else :
    print("FAIL")
  
  if q.find_last("k") == test_strings[4] :
    print("SUCCESS")
  else :
    print("FAIL")

msg_q = queue()

test_case1( msg_q )
test_case2( msg_q )