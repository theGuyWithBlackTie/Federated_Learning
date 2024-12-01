from flwr.client import NumPyClient

import pandas as pd

class AmazonSentimentClient(NumPyClient):
    def __init__(self, data: pd.DataFrame, labels: list):
        self.data_frame = data
        self.local_labels = labels

    def get_local_labels(self):
        """
        Method for the `server` to query for the local labels.
        Returns:
            List of local labels
        """
        return self.local_labels
    
    def receive_global_label_mapping(self, global_label_mapping):
        """
        Receive global labels mapping from the server
        Args:
            global_label_mapping: Dictionary mapping global labels to indices
        """
        self.global_label_mapping = global_label_mapping