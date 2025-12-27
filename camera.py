import pytest
from camera import CameraManager, run_camera

def test_approve():
    decision, _ = run_camera_booking(camera="Camera-A", used_hours=3, requested_hours=2, capacity=8, priority="LOW")
    assert decision == "APPROVE"

def test_conditionally_approve():
    decision, _ = run_camera_booking(camera="Camera-B", used_hours=6, requested_hours=3, capacity=8, priority="HIGH")
    assert decision == "CONDITIONALLY_APPROVE"

def test_reject():
    decision, _ = run_camera_booking(camera="Camera-C", used_hours=6, requested_hours=4, capacity=8, priority="LOW")
    assert decision == "REJECT"

def test_best_camera():
    cm = CameraManager()
    cm.book_camera("Camera-A", 5)
    cm.book_camera("Camera-B", 2)
    assert cm.best_available_camera() == "Camera-B"
