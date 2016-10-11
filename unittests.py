import unittest
from hashmap import hashmap

class hashmapTest(unittest.TestCase):
    def testConstructor(self):
        hm = hashmap(10)
        self.failUnless(hm)

    def testConstructorZeroSize(self):
        self.failUnlessRaises(ValueError, hashmap, 0)

    def testConstructorTypeSize(self):
        self.failUnlessRaises(TypeError, hashmap, "foo")

    def testSet(self):
        hm = hashmap(10);
        self.assertTrue(hm.set("foo",1))

    def testSetNonStringKeys(self):
        hm = hashmap(10)
        self.assertFalse(hm.set(1,1))
        self.assertFalse(hm.set(6.2,1))
        
    def testDelete(self):
        hm = hashmap(10)
        hm.set("foo", 1)
        self.assertEqual(hm.delete("foo"), 1)

    def testDeleteNull(self):
        hm = hashmap(10)
        hm.set("foo", 1)
        self.assertFalse(hm.delete("bar"))

    def testFull(self):
        hm = hashmap(2)
        hm.set("foo", 1)
        hm.set("bar", 2)
        self.assertFalse(hm.set("baz", 3))

    def testLoad(self):
        hm = hashmap(4)
        hm.set("foo", 1)
        self.assertEqual(hm.load(), 0.25)
        hm.set("bar", 2)
        self.assertEqual(hm.load(), 0.5)

    def testLoadDelete(self):
        hm = hashmap(10)
        hm.set("foo", 1)
        hm.delete("foo")
        self.assertEqual(hm.load(), 0.00)

if __name__ == "__main__":
    unittest.main()

