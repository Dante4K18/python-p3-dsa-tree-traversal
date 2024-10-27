class Tree:
  def __init__(self, root):
    self.root = root

  def get_element_by_id(self, id):
    stack = [self.root]

    while stack:
      node = stack.pop()
      if node.get('id') == id:
        return node
      stack.extend(node.get('children', []))

    return None
