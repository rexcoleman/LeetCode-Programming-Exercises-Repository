from random import choice


class RandomizedSet:

    def __init__(self):
        # Initialize data structure
        self.dict = {}
        self.list = []
    def insert(self, val: int) -> bool:
        # Inserts a value to the set.
        # Returns true if the set did not already contain the specified element.
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Removes a value from the set.
        # Returns true if the set contained the specified element.
        if val in self.dict:
            # Move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # Delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        # Get a random element from the set
        return choice(self.list)

    def visualizeSelf(self):
        # Visualize the contents of self.dict and self.list
        print("self.dict: ")
        for key, value in self.dict.items():
            print(f"{key}: {value}")
        print("\nself.list", self.list, "\n")





if __name__ == '__main__':

    obj = RandomizedSet()
    obj.insert(1)
    print("Insert 1")
    obj.visualizeSelf()
    obj.remove(2)
    print("Remove 2")
    obj.visualizeSelf()
    obj.insert(2)
    print("Insert 2")
    obj.visualizeSelf()
    a = obj.getRandom()
    print(f"Get Random: {a}")
    obj.visualizeSelf()
    obj.remove(1)
    print("Remove 1")
    obj.visualizeSelf()
    obj.insert(2)
    print("Insert 2")
    obj.visualizeSelf()
    a = obj.getRandom()
    print(f"Get Random: {a}")
    obj.visualizeSelf()