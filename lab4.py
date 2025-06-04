class Node:
    def __init__(self, product_id, name, sales):
        self.product_id = product_id
        self.name = name
        self.sales = sales
        self.left = None
        self.right = None


class ProductQueue:
    def __init__(self):
        self.root = None
        self.ids = set()

    def insert(self, product_id, name, sales):
        if product_id in self.ids:
            print(f"Товар з ID {product_id} вже існує.")
            return
        new_node = Node(product_id, name, sales)
        self.ids.add(product_id)

        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, node, new_node):
        if new_node.sales <= node.sales:
            if node.left:
                self._insert(node.left, new_node)
            else:
                node.left = new_node
        else:
            if node.right:
                self._insert(node.right, new_node)
            else:
                node.right = new_node

    def del_max(self):
        if not self.root:
            print("Черга порожня.")
            return None

        if not self.root.right:
            max_node = self.root
            self.root = self.root.left
            self.ids.remove(max_node.product_id)
            return max_node

        parent = None
        current = self.root
        while current.right:
            parent = current
            current = current.right

        if parent:
            parent.right = current.left

        self.ids.remove(current.product_id)
        return current

    def peek(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right

        return current

    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append((node.product_id, node.name, node.sales))
            self.in_order(node.right, result)

    def display(self):
        result = []
        self.in_order(self.root, result)
        return result


pq = ProductQueue()

pq.insert("A1", "Хліб", 10)
pq.insert("B2", "Молоко", 25)
pq.insert("C3", "Сік", 8)
pq.insert("D4", "Яблука", 15)
pq.insert("E", "Печиво", 30)

print("Усі товари за зростанням:")
for id, name, sales in pq.display():
    print(f"ID: {id}, Назва: {name}, Продажі: {sales}")

top = pq.peek()
if top:
    print(f"\nНайпопулярніший товар: {top.name} (ID: {top.product_id}, Продажі: {top.sales})")

removed = pq.del_max()
if removed:
    print(f"\nВидалено найпопулярніший товар: {removed.name} (ID: {removed.product_id})")

print("\nОновлений список товарів:")
for id, name, sales in pq.display():
    print(f"ID: {id}, Назва: {name}, Продажі: {sales}")
