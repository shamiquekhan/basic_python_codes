class TreeNode:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.left = None
        self.right = None

class UserProfileManager:
    def __init__(self):
        self.root = None

    def insert(self, username, name, email):
        new_node = TreeNode(username, name, email)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if username < current.username:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:  # username >= current.username
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def update(self, username, new_name=None, new_email=None):
        node = self._find_node(username)
        if node:
            if new_name is not None:
                node.name = new_name
            if new_email is not None:
                node.email = new_email
            print(f"Updated profile for '{username}': {node.name} ({node.email})")
        else:
            print(f"Error: Username '{username}' not found.")

    def _find_node(self, username):
        current = self.root
        while current:
            if username == current.username:
                return current
            elif username < current.username:
                current = current.left
            else:
                current = current.right
        return None

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.username, node.name, node.email))
            self._inorder_traversal(node.right, result)

    def list_all_sorted(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Example usage:
manager = UserProfileManager()

# Inserting users
manager.insert('alice', 'Alice Smith', 'alice@example.com')
manager.insert('bob', 'Bob Johnson', 'bob@example.com')
manager.insert('charlie', 'Charlie Brown', 'charlie@example.com')

# Updating user
manager.update('bob', new_name='Bob Johnson Jr.')

# Listing all users sorted by username
print("\nAll users sorted by username:")
users_sorted = manager.list_all_sorted()
for username, name, email in users_sorted:
    print(f"Username: {username}, Name: {name}, Email: {email}")
