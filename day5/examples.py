from data_structures_two import PhoneBookList, PhoneBookDict

print "Using PhoneBookList:"
b = PhoneBookList()
b.add_contact('sam', '90834')
b.add_contact('austin', '9084')
b.add_contact('esther', '89032')
b.add_contact('claire', '0834')
b.add_contact('maggie', '97634')
b.add_contact('james', '9763')

# test search
print 'James : ', b.search('james')
print 'Jane: ', b.search('ruth')
print 'Esther: ', b.search('esther')

print "\nUsing PhoneBookDict:"
b = PhoneBookDict()
b.add_contact('sam', '90834')
b.add_contact('austin', '9084')
b.add_contact('esther', '89032')
b.add_contact('claire', '0834')
b.add_contact('maggie', '97634')
b.add_contact('james', '9763')

# test search
print 'James : ', b.search('james')
print 'Jane: ', b.search('ruth')
print 'Esther: ', b.search('esther')
