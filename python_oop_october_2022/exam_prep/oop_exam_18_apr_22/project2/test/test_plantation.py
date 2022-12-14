from exam_prep.oop_exam_18_apr_22.project2.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(3)

    def test_correct_init(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_with_incorrect_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.incorrect_plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_when_worker_is_already_hired_raise_value_error(self):
        self.plantation.workers = ['Test']
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Test')
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_correctly(self):
        self.plantation.workers = ['Worker1']
        result = self.plantation.hire_worker('Worker2')
        self.assertEqual(self.plantation.workers, ['Worker1', 'Worker2'])
        self.assertEqual("Worker2 successfully hired.", result)

    def test_len_method(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants = {'Worker1': ['plant1', 'plant2'], 'Worker2': ['plant1']}
        result = len(self.plantation)
        self.assertEqual(3, result)

    def test_planting_when_worker_is_not_hired_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('W', 'P')
        self.assertEqual("Worker with name W is not hired!", str(ve.exception))

    def test_planting_when_the_plantation_is_full_raise_value_error(self):
        self.plantation.workers = ['W']
        self.plantation.plants = {'Worker1': ['plant1', 'plant2'], 'Worker2': ['plant1']}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('W', 'P')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_existing_worker(self):
        self.plantation.workers = ['W', 'Worker2']
        self.plantation.plants = {'W': ['plant1'], 'Worker2': ['plant1']}
        result = self.plantation.planting('W', 'P')
        self.assertEqual({'W': ['plant1', 'P'], 'Worker2': ['plant1']}, self.plantation.plants)
        self.assertEqual("W planted P.", result)

    def test_planting_with_a_new_worker(self):
        self.plantation.workers = ['W', 'Worker2']
        self.plantation.plants = {'Worker2': ['plant1']}
        result = self.plantation.planting('W', 'P')
        self.assertEqual({'Worker2': ['plant1'], 'W': ['P']}, self.plantation.plants)
        self.assertEqual("W planted it's first P.", result)

    def test_str_method(self):
        result = str(self.plantation)
        self.assertEqual('Plantation size: 3\n', result)
        self.plantation.plants = {'W': ['P'], 'W2': ['P2']}
        self.plantation.workers = ['W', 'W2']
        result2 = str(self.plantation)
        self.assertEqual("Plantation size: 3\nW, W2\nW planted: P\nW2 planted: P2", result2)

    def test_repr_method(self):
        result = repr(self.plantation)
        self.assertEqual('Size: 3\nWorkers: ', result)
        self.plantation.plants = {'W': ['P'], 'W2': ['P2']}
        self.plantation.workers = ['W', 'W2']
        result2 = repr(self.plantation)
        self.assertEqual("Size: 3\nWorkers: W, W2", result2)


if __name__ == '__main__':
    main()