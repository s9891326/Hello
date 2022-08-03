import uuid

from data_spec_validator.spec import INT, DIGIT_STR, ONE_OF, Checker, CheckerOP, validate_data_spec
from data_spec_validator.decorator import dsv


class SomeSpec:
	field_a = Checker([INT])
	field_b = Checker([DIGIT_STR], optional=True)
	field_c = Checker([DIGIT_STR, INT], op=CheckerOP.ANY)


print(uuid.uuid1())

some_data = dict(field_a=4, field_b='3', field_c=1, field_dont_care=[5, 6])
validate_data_spec(some_data, SomeSpec)  # return True

some_data = dict(field_a=4, field_c='1')
validate_data_spec(some_data, SomeSpec)  # return True

some_data = dict(field_a=4, field_c=1)
validate_data_spec(some_data, SomeSpec)  # return True

some_data = dict(field_a='4', field_c='1')
validate_data_spec(some_data, SomeSpec)  # raise Exception

some_data = dict(field_a='4', field_c='1')
validate_data_spec(some_data, SomeSpec, nothrow=True)  # return False


class AnotherSpec:
	field = Checker([ONE_OF], extra={ONE_OF: [1, '2', [3, 4], {'5': 6}]})


another_data = dict(field=[3, 4])
validate_data_spec(another_data, AnotherSpec)  # return True

another_data = dict(field='4')
validate_data_spec(another_data, AnotherSpec)  # raise Exception


