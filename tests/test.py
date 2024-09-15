import sys
from os import path
from domain.entities.base_entity_test import test_base_entity_id_generation, test_base_entity_id_uniqueness
from domain.entities.score_entity_test import test_score_creation, test_score_from_dict, test_score_validation, \
    test_score_serialization

sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))


def run_test(test_func):
    try:
        test_func()
        print(f"PASS: {test_func.__name__}")
    except AssertionError as e:
        print(f"FAIL: {test_func.__name__} - {str(e)}")
    except Exception as e:
        print(f"ERROR: {test_func.__name__} - {str(e)}")


if __name__ == '__main__':
    tests = [
        test_base_entity_id_generation,
        test_base_entity_id_uniqueness,
        test_score_creation,
        test_score_from_dict,
        test_score_validation,
        test_score_serialization
    ]

    for test in tests:
        run_test(test)
