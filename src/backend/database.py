"""
Database configuration and setup for Mergington High School API
"""

from argon2 import PasswordHasher

# Use in-memory storage for demonstration
activities_data = {}
teachers_data = {}

# Mock collection classes to mimic MongoDB interface
class MockCollection:
    def __init__(self, data_store):
        self.data_store = data_store
    
    def find(self, query=None):
        if not query:
            return [{"_id": k, **v} for k, v in self.data_store.items()]
        
        results = []
        for k, v in self.data_store.items():
            if self._matches_query({"_id": k, **v}, query):
                results.append({"_id": k, **v})
        return results
    
    def find_one(self, query):
        if isinstance(query, dict) and "_id" in query:
            key = query["_id"]
            if key in self.data_store:
                return {"_id": key, **self.data_store[key]}
        return None
    
    def count_documents(self, query):
        return len(list(self.find(query)))
    
    def insert_one(self, doc):
        if "_id" in doc:
            key = doc.pop("_id")
            self.data_store[key] = doc
        return type('MockResult', (), {'acknowledged': True})()
    
    def update_one(self, query, update):
        if "_id" in query:
            key = query["_id"]
            if key in self.data_store:
                if "$push" in update:
                    for field, value in update["$push"].items():
                        if field not in self.data_store[key]:
                            self.data_store[key][field] = []
                        self.data_store[key][field].append(value)
                if "$pull" in update:
                    for field, value in update["$pull"].items():
                        if field in self.data_store[key] and isinstance(self.data_store[key][field], list):
                            if value in self.data_store[key][field]:
                                self.data_store[key][field].remove(value)
                return type('MockResult', (), {'modified_count': 1})()
        return type('MockResult', (), {'modified_count': 0})()
    
    def aggregate(self, pipeline):
        # Simple implementation for getting unique days
        if len(pipeline) >= 2 and pipeline[0].get("$unwind") and pipeline[1].get("$group"):
            all_days = set()
            for activity in self.data_store.values():
                if "schedule_details" in activity and "days" in activity["schedule_details"]:
                    all_days.update(activity["schedule_details"]["days"])
            return [{"_id": day} for day in sorted(all_days)]
        return []
    
    def _matches_query(self, doc, query):
        for key, condition in query.items():
            if key == "_id":
                if doc.get("_id") != condition:
                    return False
            elif "." in key:
                # Handle nested queries like "schedule_details.days"
                parts = key.split(".")
                current = doc
                for part in parts:
                    if isinstance(current, dict) and part in current:
                        current = current[part]
                    else:
                        return False
                
                if isinstance(condition, dict):
                    if "$in" in condition:
                        if not isinstance(current, list):
                            return False
                        if not any(item in condition["$in"] for item in current):
                            return False
                    elif "$gte" in condition:
                        if current < condition["$gte"]:
                            return False
                    elif "$lte" in condition:
                        if current > condition["$lte"]:
                            return False
                else:
                    if current != condition:
                        return False
            else:
                if key not in doc:
                    return False
                doc_value = doc[key]
                if isinstance(condition, dict):
                    if "$gte" in condition and doc_value < condition["$gte"]:
                        return False
                    if "$lte" in condition and doc_value > condition["$lte"]:
                        return False
                else:
                    if doc_value != condition:
                        return False
        return True

activities_collection = MockCollection(activities_data)
teachers_collection = MockCollection(teachers_data)

# Methods
def hash_password(password):
    """Hash password using Argon2"""
    ph = PasswordHasher()
    return ph.hash(password)

def init_database():
    """Initialize database if empty"""

    # Initialize activities if empty
    if activities_collection.count_documents({}) == 0:
        for name, details in initial_activities.items():
            activities_collection.insert_one({"_id": name, **details})
            
    # Initialize teacher accounts if empty
    if teachers_collection.count_documents({}) == 0:
        for teacher in initial_teachers:
            teachers_collection.insert_one({"_id": teacher["username"], **teacher})

# Initial database if empty
initial_activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Mondays and Fridays, 3:15 PM - 4:45 PM",
        "schedule_details": {
            "days": ["Monday", "Friday"],
            "start_time": "15:15",
            "end_time": "16:45"
        },
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        "difficulty": "Beginner"
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 7:00 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Morning Fitness": {
        "description": "Early morning physical training and exercises",
        "schedule": "Mondays, Wednesdays, Fridays, 6:30 AM - 7:45 AM",
        "schedule_details": {
            "days": ["Monday", "Wednesday", "Friday"],
            "start_time": "06:30",
            "end_time": "07:45"
        },
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:30 PM",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Basketball Team": {
        "description": "Practice and compete in basketball tournaments",
        "schedule": "Wednesdays and Fridays, 3:15 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Wednesday", "Friday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art techniques and create masterpieces",
        "schedule": "Thursdays, 3:15 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Thursday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"],
        "difficulty": "Beginner"
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:30 PM",
        "schedule_details": {
            "days": ["Monday", "Wednesday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging problems and prepare for math competitions",
        "schedule": "Tuesdays, 7:15 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Tuesday"],
            "start_time": "07:15",
            "end_time": "08:00"
        },
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 3:30 PM - 5:30 PM",
        "schedule_details": {
            "days": ["Friday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"],
        "difficulty": "Intermediate"
    },
    "Weekend Robotics Workshop": {
        "description": "Build and program robots in our state-of-the-art workshop",
        "schedule": "Saturdays, 10:00 AM - 2:00 PM",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "10:00",
            "end_time": "14:00"
        },
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "oliver@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Science Olympiad": {
        "description": "Weekend science competition preparation for regional and state events",
        "schedule": "Saturdays, 1:00 PM - 4:00 PM",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "13:00",
            "end_time": "16:00"
        },
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Sunday Chess Tournament": {
        "description": "Weekly tournament for serious chess players with rankings",
        "schedule": "Sundays, 2:00 PM - 5:00 PM",
        "schedule_details": {
            "days": ["Sunday"],
            "start_time": "14:00",
            "end_time": "17:00"
        },
        "max_participants": 16,
        "participants": ["william@mergington.edu", "jacob@mergington.edu"],
        "difficulty": "Advanced"
    },
    "Manga Maniacs": {
        "description": "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        "schedule": "Tuesdays, 7:00 PM - 8:00 PM",
        "schedule_details": {
            "days": ["Tuesday"],
            "start_time": "19:00",
            "end_time": "20:00"
        },
        "max_participants": 15,
        "participants": [],
        "difficulty": "Beginner"
    }
}

initial_teachers = [
    {
        "username": "mrodriguez",
        "display_name": "Ms. Rodriguez",
        "password": hash_password("art123"),
        "role": "teacher"
     },
    {
        "username": "mchen",
        "display_name": "Mr. Chen",
        "password": hash_password("chess456"),
        "role": "teacher"
    },
    {
        "username": "principal",
        "display_name": "Principal Martinez",
        "password": hash_password("admin789"),
        "role": "admin"
    }
]

