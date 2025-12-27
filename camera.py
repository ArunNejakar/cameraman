class CameraManager:
    def __init__(self):
        self.usage = {}

    def book_camera(self, camera, used_hours):
        """Record hours already used by a camera"""
        self.usage[camera] = used_hours

    def booking_decision(self, camera, requested_hours, capacity, priority):
        """Return booking decision based on usage, capacity, and priority"""
        used_hours = self.usage.get(camera, 0)
        total_hours = used_hours + requested_hours

        if total_hours <= capacity:
            return "APPROVE"
        elif priority.upper() == "HIGH" and total_hours <= capacity + 2:
            return "CONDITIONALLY_APPROVE"
        else:
            return "REJECT"

    def best_available_camera(self):
        """Return the camera with the least usage"""
        return min(self.usage, key=self.usage.get)


def run_camera_booking(
    camera="Camera-A",
    used_hours=3,
    requested_hours=2,
    capacity=8,
    priority="HIGH"
):
    """Function to run booking with default values; can be imported for pytest"""
    cm = CameraManager()
    cm.book_camera(camera, used_hours)
    decision = cm.booking_decision(camera, requested_hours, capacity, priority)

    print("Camera:", camera)
    print("Used Hours:", used_hours)
    print("Requested Hours:", requested_hours)
    print("Capacity:", capacity)
    print("Priority:", priority)
    print("Decision:", decision)

    return decision, cm  # Return objects for pytest validation


# ---- Docker Entry Point ----
if __name__ == "__main__":
    # Runs automatically in Docker with default values
    run_camera_booking()
