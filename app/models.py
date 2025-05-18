from datetime import datetime


class Model:
    def __init__(self, model_id, description):
        self.model_id = model_id
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.state = "created"
        self.versions = []
        self.metadata = {
            "request_count": 0,
            "error_count": 0,
            "last_accessed": None,
        }

    def update_state(self, state):
        valid_states = ["created", "active", "inactive", "archived"]
        if state not in valid_states:
            raise ValueError(f"Invalid state. Allowed states: {valid_states}")
        self.state = state
        self.updated_at = datetime.now()

    def add_version(self, version):
        self.versions.append(version)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "model_id": self.model_id,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "state": self.state,
            "versions": self.versions,
            "metadata": self.metadata,
        }
    