import threading
import time

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel

@receiver(post_save, sender=TestModel)
def signal_for_questions(sender, instance, **kwargs):
    print("Signal started")
    
    # Simulate long running task. Added intentionally to prove synchronous behavior
    time.sleep(5)
    
    print("Signal completed")
    
    # Print current thread ID
    print("Signal Thread ID: ", threading.get_ident())
    