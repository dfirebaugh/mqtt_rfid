from lib.acl import AccessControlList

acl = AccessControlList('acl')
acl.clear()

users = [
    '5AA12E81',
    '5AA12E82',
    ]

acl.add_many(users)
