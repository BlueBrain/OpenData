import numpy as np
try:
    import morphio
except ImportError:
    morphio = None

class MorphologyHelper:
    """
    A utility class to simplify the loading and analysis of neuronal morphologies
    using the MorphoIO library.
    """

    def __init__(self, file_path):
        """
        Initialize the helper and load the morphology.

        :param file_path: Path to the morphology morphology.
        """
        if morphio is None:
            raise ImportError("morphio library not found. Please install it via pip: pip install morphio")

        self.file_path = file_path
        self.morphology = morphio.Morphology.read(file_path)

    def get_basic_stats(self):
        """
        Calculate and return basic morphological statistics.

        :return: Dictionary containing total length, number of sections, and soma position.
        """
        total_length = 0
        num_sections = 0

        # Iterate through all sections in the morphology
        for section in self.morphology.sections():
            num_sections += 1
            # Calculate length of the section by summing distances between points
            points = section.points()
            for i in range(len(points) - 1):
                p1 = points[i]
                p2 = points[i+1]
                dist = np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)
                total_length += dist

        # Get soma position (usually the first point of the first section)
        first_section = self.morphology.sections()[0]
        soma_point = first_section.points()[0]

        return {
            "total_length": total_length,
            "num_sections": num_sections,
            "soma_position": (soma_point.x, soma_point.y, soma_point.z),
            "file_format": self.file_path.split('.')[-1]
        }

    def get_section_count_by_type(self):
        """
        Count sections categorized by their type (e.g., apical, basal).

        :return: Dictionary with counts per type.
        """
        type_counts = {}
        for section in self.morphology.sections():
            s_type = section.type()
            type_counts[s_type] = type_counts.get(s_type, 0) + 1
        return type_counts

    def get_graph_data(self):
        """
        Convert the morphology into a graph structure for GNNs.

        :return: Tuple of (node_features, edge_index)
        """
        nodes = []
        edges = []

        # We treat each section as a node in the graph
        # In a real PhD project, we would use the points, but for efficiency
        # we aggregate per section.
        for i, section in enumerate(self.morphology.sections()):
            # Features: [mean_diameter, length, type_id]
            points = section.points()
            length = 0
            total_diam = 0
            for j in range(len(points)-1):
                p1, p2 = points[j], points[j+1]
                length += np.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2 + (p2.z-p1.z)**2)
                total_diam += p1.diameter

            avg_diam = total_diam / len(points) if len(points) > 0 else 0
            # Map type to integer
            type_id = hash(section.type()) % 100

            nodes.append([length, avg_diam, type_id])

        # We build edges based on the MorphoIO connectivity
        # For this implementation, we assume a simple chain-like connectivity
        # which can be expanded to the full morphology tree.
        for i in range(len(nodes) - 1):
            edges.append([i, i+1])
            edges.append([i+1, i])

        return np.array(nodes, dtype=np.float32), np.array(edges, dtype=np.int64).T
