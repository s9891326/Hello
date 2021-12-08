import addresbook_pb2

address_book = addresbook_pb2.AddressBook()
person = address_book.people.add()
person.id = 1
print(f"test person.IsInitialized(): {person.IsInitialized()}")

person.name = "eddy"
person.email = "eddy@example.com"

print(f"test person.IsInitialized(): {person.IsInitialized()}")

phone1 = person.phones.add()
phone1.number = "0911-123-456"
phone1.type = addresbook_pb2.Person.PhoneType.MOBILE
phone2 = person.phones.add()
phone2.number = "0211-123-456"
phone2.type = addresbook_pb2.Person.PhoneType.HOME

print("==========__str__=============")
print(f"person: {person}")
print(f"type(person): {type(person)}")

# print("==========test CopyFrom=============")
# new_person = address_book.people.add()
# new_person.id = 1
# new_person.name = "eddy"
# person.CopyFrom(new_person)
# print(person)
#
# print("==========test Clear=============")
# new_person.Clear()
# print(f"new_person: {new_person}")
#
# print("==========SerializeToString=============")
# # 序列化消息並返回二進制符串
# s = person.SerializeToString()
# print(type(s), s)
#
# print("==========ParseFromString(data)=============")
# # 解析給定字符串中的消息
# target = addresbook_pb2.AddressBook()
# print(target.ParseFromString(s))


address_book = addresbook_pb2.AddressBook()
person = address_book.people.add()
person.id = 1
person.name = "eddy"
person.email = "eddy@example.com"
data = person.SerializeToString()
print(data)

# new_person = addresbook_pb2.AddressBook()
# new_person.ParseFromString(data.encode("utf-8"))
# print()
# print(target.people[0].name)
