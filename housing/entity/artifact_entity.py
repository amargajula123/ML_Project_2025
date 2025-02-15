from collections import namedtuple

# this "artifact_entity.py" is for related to "output" 

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["train_file_path","test_file_path","is_ingested","message"])