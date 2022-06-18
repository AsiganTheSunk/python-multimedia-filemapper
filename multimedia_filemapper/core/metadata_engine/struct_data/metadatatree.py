from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.metadata_engine.struct_data.metadatanode import MetadataNode


class MetadataTree:
    def __init__(self):
        self.nodes = []
        self.node_count = -1

    def get_nodes(self):
        return self.nodes

    def get_node_count(self):
        return self.node_count

    def add_node_count(self):
        self.node_count += 1

    def get_node_fflag_by_index(self, index):
        return self.nodes[index].get_metadata().get_fflag()

    def add_node(self, basename=str, metadata=None, parent_basename=None, new_basename=None, new_parent_basename=None):
        """
        :param basename: node basename
        :param metadata: metadata_engine
        :param parent_basename: node parent_basename
        :type basename: str
        :type metadata: Metadata
        :type parent_basename: str
        :return node
        :rtype list of Nodes
        """
        self.add_node_count()
        if metadata is None:
            metadata = Metadata()

        node = MetadataNode(basename, self.node_count, metadata, new_basename, new_parent_basename)
        node.parent_basename = parent_basename

        # print(f'[ADDED]: basename: {node.basename} with parent_basename: {node.parent_basename}')
        if parent_basename is not None:
            _parent_node = self.search(parent_basename)
            _parent_node[-1].add_child(node)
            # print(f'search for parent_node: {_parent_node} with {parent_basename}')
            # print(f'[PARENT]: ID({str(pnode[len(pnode) - 1].identifier)}) - {str(pnode[len(pnode) - 1].basename)}')
            # print(f'[_CHILD]: COUNT({str(len(pnode[len(pnode) - 1].children))}) - '
            #      f'ID({str(node.identifier)}) :: {str(node.basename)}')
        self.nodes.append(node)
        return node

    def update_parent_node_by_index(self, index, parent):
        """
        :param index: node identifier
        :param parent: new parent basename
        :type index: int
        :type parent: str
        """

        tnode = pnode = MetadataNode
        for node in self.get_nodes():
            if node.identifier == index:
                pnode = self.search(basename=node.parent_basename)[0]
                for child in pnode.children:
                    if child.basename == node.basename:
                        tnode = child
                        pnode.remove_child(child_basename=child.basename)
                tnode.set_parent_basename(parent)
                node.set_parent_basename(parent)
                new_parent = self.search(basename=parent)[0]
                new_parent.add_child(child=tnode)

    def search(self, basename=str, parent_basename=None):
        """
        :param basename: node basename
        :param parent_basename: node parent_basename
        :type basename: str
        :type parent_basename: str
        :return node
        :rtype list of Nodes
        """
        node = None
        nodelist = []
        if parent_basename is None:
            for item in self.nodes:
                if item.basename == basename:
                    nodelist.append(item)
            return nodelist
        else:
            for item in self.nodes:
                if item.basename == basename and item.parent_basename == parent_basename:
                    node = item
            return [node]

    def tree(self):
        """
        :return: print list of nodes with depth
        """
        subtrees = self.nodes[0].children
        for i, val in enumerate(subtrees):
            self.subtree(subtrees[i].basename, deep=1)

    def subtree(self, basename=str, parent_basename=None, deep=int):
        """
        :param basename: node basename
        :param parent_basename: node parent_basename
        :param deep: depth of the node in the tree
        :type basename: str
        :type parent_basename: str
        :type deep int
        :return: print list of nodes with depth
        """
        if parent_basename is None:
            nodelist = self.search(basename)
            print('--' + str(basename))
            for i, val in enumerate(nodelist):
                self.subtree(nodelist[i].basename, nodelist[i].parent_basename,
                             deep=deep)
        else:
            node = self.search(basename, parent_basename)[0]
            string = '--' * int(deep)
            print (str(string) + ': index: (' + str(
                node.identifier) + ') - [basename]: ' + str(
                node.basename))  # + ' [parent]: ' + str(node.parent_basename))
            if node.children is not []:
                for child in node.children:
                    self.subtree(child.basename, child.parent_basename,
                                 deep=deep + 1)

    def display(self):
        '''
        :return: print list of nodes
        '''
        for _node_item in self.nodes:
            print(f'[ Node ID ]: ({_node_item.identifier})')
            print(f'>: Original Parent: {_node_item.parent_basename}')
            print(f'>: :: Original Child: {_node_item.basename}')
            print(f'>: Updated Parent: {_node_item.new_parent_basename}')
            print(f'>: :: Updated Child: {_node_item.new_basename}')

    @staticmethod
    def _fix_paths(list_of_very_paths):
        fixed_l = []
        for index, items in reversed(list_of_very_paths):
            item = ''
            for sub_item in items:
                item += '\\' + str(sub_item)

            fixed_l.append((index, item[1:]))
        return fixed_l

    def get_abs_paths(self):
        nodes = self.nodes
        l = []
        for node_index in range(len(self.nodes)-1, -1, -1):
            l2 = self.get_path(nodes[node_index], [nodes[node_index].basename])
            print(f'l2: {l2}')
            l.append((node_index, l2))
        return self._fix_paths(l)

    def get_path(self, node, list_of_paths):
        if node.parent_basename is not None:
            list_of_paths = [node.parent_basename] + list_of_paths
            # print('pre:search', node.parent_basename, node.basename)
            search_index = 0
            for index, search_item in enumerate(self.search(node.parent_basename)):
                if search_item.parent_basename is not None:
                    if search_item.parent_basename in node.basename:
                        search_index = index
                else:
                    break
                # print(search_item.basename, search_item.parent_basename)
            return self.get_path(self.search(node.parent_basename)[search_index], list_of_paths)
        return list_of_paths
