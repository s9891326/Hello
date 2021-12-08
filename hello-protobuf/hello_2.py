from share import addresbook_pb2

req = addresbook_pb2.OpenRestShareCardsReq()
# req.consume_type = 1
print(req)
print(req.consume_type)

if req.consume_type == addresbook_pb2.OpenRestShareCardsReq.ConsumeType.DIAMOND:
    print(123)
