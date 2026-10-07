import unittest

from my_set import MySet


class TestMySet(unittest.TestCase):
    def test_new_set_is_empty(self):
        values = MySet()

        self.assertTrue(values.is_empty())
        self.assertEqual(len(values), 0)
        self.assertEqual(list(values), [])

    def test_add_returns_true_for_new_values_and_false_for_duplicates(self):
        values = MySet()

        self.assertTrue(values.add("apple"))
        self.assertTrue(values.add("banana"))
        self.assertFalse(values.add("apple"))

        self.assertEqual(len(values), 2)
        self.assertFalse(values.is_empty())
        self.assertIn("apple", values)
        self.assertIn("banana", values)

    def test_remove_returns_true_for_existing_values_and_false_for_missing_values(self):
        values = MySet()
        values.add("apple")

        self.assertTrue(values.remove("apple"))
        self.assertFalse(values.remove("apple"))
        self.assertNotIn("apple", values)
        self.assertEqual(len(values), 0)
        self.assertTrue(values.is_empty())

    def test_colliding_values_are_stored_and_removed_independently(self):
        values = MySet(capacity=1)
        values.add("apple")
        values.add("banana")

        self.assertEqual(set(values), {"apple", "banana"})
        self.assertTrue(values.remove("apple"))
        self.assertIn("banana", values)
        self.assertNotIn("apple", values)

    def test_resize_preserves_values(self):
        values = MySet(capacity=2, load_factor=0.75)
        items = ["apple", "banana", "cherry"]

        for item in items:
            values.add(item)

        self.assertEqual(values.capacity, 4)
        self.assertEqual(set(values), set(items))
        self.assertEqual(len(values), len(items))

    def test_clear_removes_all_values_and_keeps_capacity(self):
        values = MySet(capacity=4)
        values.add("apple")
        values.add("banana")

        values.clear()

        self.assertTrue(values.is_empty())
        self.assertEqual(len(values), 0)
        self.assertEqual(list(values), [])
        self.assertEqual(values.capacity, 4)

    def test_iteration_yields_each_value_once(self):
        values = MySet()
        items = {1, 2, 3, 4}

        for item in items:
            values.add(item)

        self.assertEqual(set(values), items)
        self.assertEqual(len(list(values)), len(items))


if __name__ == "__main__":
    unittest.main()
