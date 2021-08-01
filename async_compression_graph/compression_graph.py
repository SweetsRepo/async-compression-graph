"""
"""

class CompressionGraph():
    """
    """
    def __init__(self):
        self.compression_algorithm_callback = None
        self.decompression_algorithm_callback = None
        self.max_num_of_children = None

    async def add(self, data):
        """
        Adds a new node containing data to the graph
        Arguments:
            data: Varying type of data needing to be stored
        Return:
            None
        """
        pass
        # if node.children == max_num_of_children:
        #   compress and set compressed node in place

    async def remove(self, node):
        """
        Reference to node to remove from the graph
        """
        pass

    async def _bfs(self, node):
        """
        Performs a breadth first search throughout the graph
        Arguments:
            node: Reference to the node to start the search from
        Return:
            result: Reference to node (See Notes)
        Notes:
            Dependent on calling context the node returned by this function may
            be any of the following:
              * Node to use as parent when inserting new data
              * Node to (un)compress
              * Node to remove from the data structure
            Also since this is technically a tree and we only care about
            children from the start mode down, we don't need to keep track of
            what we've already visited
        """
        pass
        # for child in node.children:
        #   if type(child) == CompressedNode:
        #       begin uncompression in subprocess, dump result into queue
        #       tasks.append(asyncio.create_task(self._uncompress, node))
        # done, pending = await asyncio.wait(tasks)
        # for result in done:
        #   for result_node in result:
        #       # Using a yield here will allow the data stucture to be treated 
        #       # as an iterable
        #       yield result_node.data
        # Continue on and proccess all the rest of the data


    async def _compress(self, node):
        """
        Node to compress all children nodes into a single CompressedNode
        Arguments:
            node: Reference to the parent node who's children should be
                  compressed
        Return:
            result: Reference to the CompressedNode
        Notes:
            Compression algorithm applied to the children may vary with options
            set at the graph level.
        """
        pass

    async def _uncompress(self, node):
        """
        Node to uncompress all children nodes out of into local buffer
        Arguments:
            node: Reference to the parent node who's children should be
                  uncompressed
        Return:
            result: Reference to the parent of the no uncompressed node
        Notes:
            Compression algorithm applied to the children may vary with options
            set at the graph level.
        """
        pass

class CompressedNode():
    """
    """
    def __init__(self):
        self.parent = None
        self.children = None
        self.zipped = None

class UncompressedNode():
    """
    """
    def __init__(self):
        self.data = None
        self.children = []
        self.parent = None

class TransitoryNode():
    """
    Node to handle transition from compressed wth children to uncompressed but
    still need to point at children? Would be more memory efficient to create
    this, but runtime will take a hit from compressing/uncompressing more
    frequently. Alternative is to leave Compressed node as parent to all
    uncompressed children and then prune the children when they're no longer
    needed.
    """
    pass
